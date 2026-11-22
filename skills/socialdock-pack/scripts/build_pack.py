#!/usr/bin/env python3
"""Build a SocialDock pack ZIP from a JSON brief and local video files.

The brief holds the texts an assistant wrote (titles, descriptions, captions per
network and language) and the paths of the edits. The script lays out the pack
format v1 (common/<lang>/video.mp4, youtube/post.json, <network>/<lang>/caption.txt),
checks the limits the extension enforces, and writes videos uncompressed.

Usage: build_pack.py brief.json output.zip
"""
import json
import re
import sys
import zipfile
from pathlib import Path

LANGUAGE = re.compile(r'^[a-z]{2,3}(?:-[A-Za-z0-9]+)*$')
SOCIAL_NETWORKS = ('instagram', 'facebook', 'linkedin', 'tiktok', 'pinterest', 'threads')
CAPTION_LIMITS = {'instagram': 2200, 'tiktok': 2200, 'linkedin': 3000, 'facebook': 63206, 'pinterest': 800}
THREADS_CAPTION_BYTES = 500
YOUTUBE_TITLE_CHARS = 100
YOUTUBE_DESCRIPTION_BYTES = 5000
YOUTUBE_TAGS_CHARS = 450
PINTEREST_TITLE_CHARS = 100
THUMBNAIL_BYTES = 50 * 1024 * 1024


class BriefError(ValueError):
    """The brief does not satisfy the pack format or a network limit."""


def check_language(language):
    if not isinstance(language, str) or not LANGUAGE.match(language):
        raise BriefError(f'invalid language code: {language!r}')
    return language


def check_mp4(path):
    path = Path(path)
    if not path.is_file() or path.suffix.lower() != '.mp4':
        raise BriefError(f'missing MP4 video: {path}')
    with path.open('rb') as handle:
        header = handle.read(12)
    if len(header) < 12 or header[4:8] != b'ftyp':
        raise BriefError(f'not an MP4 file (no ftyp header): {path}')
    return path


def check_text(text, where):
    if not isinstance(text, str) or not text.strip():
        raise BriefError(f'{where}: text is missing')
    if '<' in text or '>' in text:
        raise BriefError(f'{where}: angle brackets are not allowed')
    return text.strip()


def social_entry(value, network, language):
    entry = {'caption': value} if isinstance(value, str) else value
    if not isinstance(entry, dict):
        raise BriefError(f'{network}/{language}: expected a caption or an object')
    caption = check_text(entry.get('caption'), f'{network}/{language} caption')
    if network == 'threads':
        if len(caption.encode('utf-8')) > THREADS_CAPTION_BYTES:
            raise BriefError(f'threads/{language}: caption over {THREADS_CAPTION_BYTES} UTF-8 bytes')
    elif len(caption) > CAPTION_LIMITS[network]:
        raise BriefError(f'{network}/{language}: caption over {CAPTION_LIMITS[network]} characters')
    title = entry.get('title')
    if title is not None:
        title = check_text(title, f'{network}/{language} title')
        if network == 'pinterest' and len(title) > PINTEREST_TITLE_CHARS:
            raise BriefError(f'pinterest/{language}: title over {PINTEREST_TITLE_CHARS} characters')
    return caption, title


def plan(brief):
    """Returns the list of (archive path, bytes or source Path) for a valid brief."""
    if not isinstance(brief, dict):
        raise BriefError('the brief must be a JSON object')
    videos = brief.get('videos')
    if not isinstance(videos, dict) or not videos:
        raise BriefError('videos: give one MP4 per language, e.g. {"en": "/path/en.mp4"}')
    entries = []
    for language, path in videos.items():
        entries.append((f'common/{check_language(language)}/video.mp4', check_mp4(path)))
    targets = 0

    youtube = brief.get('youtube')
    if youtube:
        texts = youtube.get('texts')
        if not isinstance(texts, dict) or not texts:
            raise BriefError('youtube.texts: give a title (and description) per language')
        source = check_language(youtube.get('sourceLanguage', next(iter(texts))))
        if source not in texts or source not in videos:
            raise BriefError('youtube.sourceLanguage needs texts and a video')
        for language, text in texts.items():
            check_language(language)
            title = check_text((text or {}).get('title'), f'youtube/{language} title')
            if len(title) > YOUTUBE_TITLE_CHARS:
                raise BriefError(f'youtube/{language}: title over {YOUTUBE_TITLE_CHARS} characters')
            description = (text or {}).get('description', '') or ''
            if description:
                description = check_text(description, f'youtube/{language} description')
            if len(description.encode('utf-8')) > YOUTUBE_DESCRIPTION_BYTES:
                raise BriefError(f'youtube/{language}: description over {YOUTUBE_DESCRIPTION_BYTES} UTF-8 bytes')
            entries.append((f'youtube/{language}/title.txt', title.encode('utf-8')))
            if description:
                entries.append((f'youtube/{language}/description.txt', description.encode('utf-8')))
        tags = youtube.get('tags', [])
        if not isinstance(tags, list) or any(not isinstance(tag, str) or '<' in tag or '>' in tag for tag in tags) or len(','.join(tags)) > YOUTUBE_TAGS_CHARS:
            raise BriefError(f'youtube.tags: strings, {YOUTUBE_TAGS_CHARS} characters in total')
        category = str(youtube.get('categoryId', '28'))
        if not re.fullmatch(r'\d{1,3}', category):
            raise BriefError('youtube.categoryId: a numeric YouTube category')
        post = {'version': 1, 'video': f'{source}/video.mp4', 'sourceLanguage': source, 'languages': list(texts), 'categoryId': category, 'tags': tags}
        thumbnail = youtube.get('thumbnail')
        if thumbnail:
            thumbnail = Path(thumbnail)
            if not thumbnail.is_file() or thumbnail.suffix.lower() not in ('.png', '.jpg', '.jpeg') or thumbnail.stat().st_size > THUMBNAIL_BYTES:
                raise BriefError('youtube.thumbnail: PNG or JPEG, 50 MiB maximum')
            name = 'thumbnail' + ('.png' if thumbnail.suffix.lower() == '.png' else '.jpg')
            entries.append((f'youtube/{name}', thumbnail))
            post['thumbnail'] = name
        entries.append(('youtube/post.json', (json.dumps(post, ensure_ascii=False, indent=2) + '\n').encode('utf-8')))
        targets += 1

    networks = brief.get('networks') or {}
    if not isinstance(networks, dict):
        raise BriefError('networks: an object of {network: {language: caption}}')
    for network, variants in networks.items():
        if network not in SOCIAL_NETWORKS:
            raise BriefError(f'unknown network: {network} (expected one of {", ".join(SOCIAL_NETWORKS)})')
        if not isinstance(variants, dict) or not variants:
            raise BriefError(f'{network}: give a caption per language')
        for language, value in variants.items():
            check_language(language)
            if language not in videos:
                raise BriefError(f'{network}/{language}: no video for this language (add it to videos)')
            caption, title = social_entry(value, network, language)
            entries.append((f'{network}/{language}/caption.txt', caption.encode('utf-8')))
            if title:
                entries.append((f'{network}/{language}/title.txt', title.encode('utf-8')))
        targets += 1
    if not targets:
        raise BriefError('add youtube and/or networks: common/ alone publishes nothing')
    return entries


def build(brief, output):
    entries = plan(brief)
    output = Path(output)
    with zipfile.ZipFile(output, 'w', allowZip64=True) as archive:
        for name, content in entries:
            if isinstance(content, Path):
                # Videos and images are already compressed: store them.
                archive.write(content, name, compress_type=zipfile.ZIP_STORED)
            else:
                archive.writestr(zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0)), content, compress_type=zipfile.ZIP_DEFLATED)
    return output


def main(argv):
    if len(argv) != 3:
        print(__doc__.strip().splitlines()[-1], file=sys.stderr)
        return 2
    try:
        brief = json.loads(Path(argv[1]).read_text(encoding='utf-8'))
        output = build(brief, argv[2])
    except (BriefError, json.JSONDecodeError, OSError) as error:
        print(f'error: {error}', file=sys.stderr)
        return 1
    with zipfile.ZipFile(output) as archive:
        print(f'{output}: {len(archive.namelist())} files')
        for name in archive.namelist():
            print('  ' + name)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
