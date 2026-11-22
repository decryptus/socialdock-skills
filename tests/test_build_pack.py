"""SocialDock pack skill: the builder lays out the pack format and enforces limits.

The SocialDock repository also reads the produced ZIP with the extension's pack
reader; that check is skipped in this public distribution."""
import importlib.util
import json
import shutil
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('build_pack', ROOT / 'skills/socialdock-pack/scripts/build_pack.py')
build_pack = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(build_pack)
MP4 = bytes([0, 0, 0, 24]) + b'ftypisom' + bytes(12)

READER = """
import {readFile} from 'node:fs/promises';
import {readPack} from '%s/extension/core/pack.js';
const pack = await readPack(new Blob([await readFile(process.argv[2])]));
console.log(JSON.stringify(pack.destinations.map(d => [d.network, d.variant || null, d.available, d.error || null, d.plan?.caption ?? d.plan?.translations?.fr?.title ?? null])));
"""


class BuildPackTest(unittest.TestCase):
    def setUp(self):
        self.directory = Path(tempfile.mkdtemp())
        for language in ('en', 'fr'):
            (self.directory / f'{language}.mp4').write_bytes(MP4)

    def tearDown(self):
        shutil.rmtree(self.directory)

    def brief(self, **changes):
        brief = {
            'videos': {'en': str(self.directory / 'en.mp4'), 'fr': str(self.directory / 'fr.mp4')},
            'youtube': {'sourceLanguage': 'en', 'tags': ['demo'], 'texts': {'en': {'title': 'Title', 'description': 'About'}, 'fr': {'title': 'Titre'}}},
            'networks': {'instagram': {'en': 'Hello #demo', 'fr': 'Bonjour #démo'}, 'threads': {'fr': 'Court'}, 'pinterest': {'en': {'title': 'Pin', 'caption': 'Pin text'}}},
        }
        brief.update(changes)
        return brief

    def test_layout_and_stored_videos(self):
        output = build_pack.build(self.brief(), self.directory / 'pack.zip')
        with zipfile.ZipFile(output) as archive:
            names = set(archive.namelist())
            self.assertTrue({'common/en/video.mp4', 'common/fr/video.mp4', 'youtube/post.json', 'youtube/en/title.txt', 'youtube/en/description.txt',
                             'youtube/fr/title.txt', 'instagram/fr/caption.txt', 'threads/fr/caption.txt', 'pinterest/en/title.txt'} <= names)
            self.assertEqual(archive.getinfo('common/en/video.mp4').compress_type, zipfile.ZIP_STORED)
            post = json.loads(archive.read('youtube/post.json'))
            self.assertEqual(post, {'version': 1, 'video': 'en/video.mp4', 'sourceLanguage': 'en', 'languages': ['en', 'fr'], 'categoryId': '28', 'tags': ['demo']})

    def test_limits_and_inconsistencies_are_refused(self):
        cases = [
            {'networks': {'threads': {'fr': 'é' * 251}}},
            {'networks': {'instagram': {'en': 'x' * 2201}}},
            {'networks': {'tiktok': {'de': 'Hallo'}}},
            {'networks': {'myspace': {'en': 'x'}}},
            {'networks': {'linkedin': {'en': '<script>'}}},
            {'youtube': {'texts': {'en': {'title': 'x' * 101}}}},
            {'youtube': {'texts': {'en': {'title': 'ok', 'description': 'é' * 2501}}}},
            {'youtube': None, 'networks': {}},
            {'videos': {'en': str(self.directory / 'missing.mp4')}},
        ]
        for change in cases:
            with self.subTest(change=change):
                with self.assertRaises(build_pack.BriefError):
                    build_pack.plan(self.brief(**change))
        (self.directory / 'fake.mp4').write_bytes(b'not a video at all')
        with self.assertRaises(build_pack.BriefError):
            build_pack.plan(self.brief(videos={'en': str(self.directory / 'fake.mp4')}, networks={}, youtube={'texts': {'en': {'title': 'T'}}}))

    @unittest.skipUnless(shutil.which('node') and (ROOT / 'extension/core/pack.js').exists(), 'The SocialDock reader is only in the SocialDock repository')
    def test_the_extension_reads_the_pack(self):
        output = build_pack.build(self.brief(), self.directory / 'pack.zip')
        script = self.directory / 'read.mjs'
        script.write_text(READER % ROOT.as_posix(), encoding='utf-8')
        result = subprocess.run(['node', str(script), str(output)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        destinations = json.loads(result.stdout)
        self.assertIn(['youtube', None, True, None, 'Titre'], destinations)
        self.assertIn(['instagram', 'fr', True, None, 'Bonjour #démo'], destinations)
        self.assertIn(['threads', 'fr', True, None, 'Court'], destinations)
        self.assertIn(['pinterest', 'en', True, None, 'Pin text'], destinations)
        self.assertEqual(len(destinations), 5)


if __name__ == '__main__':
    unittest.main()
