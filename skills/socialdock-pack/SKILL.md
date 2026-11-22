---
name: socialdock-pack
description: Build a SocialDock pack ZIP (YouTube titles/descriptions and per-network captions in several languages) from a video and a short brief, ready to import into the SocialDock extension or app.
---

# SocialDock pack builder

Turn a video and a few words about it into a **SocialDock pack**: one ZIP that the
SocialDock Chrome extension or Android app imports to publish the same video on
YouTube, Instagram, Facebook, LinkedIn, TikTok, Pinterest and Threads, in several
languages. You write the texts; `scripts/build_pack.py` lays out the files and
checks every network limit. Nothing is published: the user reviews everything in
SocialDock before publishing.

## 1. Gather the inputs

Ask only for what is missing:

- **Video edits**: one MP4 per language with that language's voice (for example
  `en.mp4`, `fr.mp4`). One video for all languages is fine when it has no voice or
  burned-in text; a language without its own edit must not claim a dubbed voice.
- **What the video is about**: subject, audience, tone, links or call to action,
  hashtags the user wants or refuses, brand words to keep untranslated.
- **Networks** (default: YouTube, Instagram, Facebook, LinkedIn, TikTok) and
  **languages** (default: the languages of the edits).

Never invent facts, prices, dates, results or quotes. If the brief is thin, write
neutral texts and say what could be improved.

## 2. Write the texts

Write natively in each language (not a literal translation) and adapt to each network:

| Network | What to write | Hard limit |
| --- | --- | --- |
| YouTube | `title` (searchable, front-loaded) and `description` (summary, chapters if given, links) | title 100 characters, description 5,000 UTF-8 bytes, tags 450 characters in total |
| Instagram | Reel caption: hook in the first line, short paragraphs, 3–8 relevant hashtags at the end | 2,200 characters |
| TikTok | Short, conversational caption, 3–5 hashtags (the user pastes it in TikTok) | 2,200 characters |
| Facebook | Page Reel caption, one clear call to action | 63,206 characters (keep it short) |
| LinkedIn | Professional post: insight first, line breaks, 0–3 hashtags | 3,000 characters |
| Pinterest | `title` (keywords) and description as caption | title 100, caption 800 characters |
| Threads | Very short, conversational | 500 UTF-8 bytes |

No `<` or `>` characters anywhere. Keep URLs as given by the user.

## 3. Write the brief and build the ZIP

Save the texts as JSON (paths are local files):

```json
{
  "videos": {"en": "/path/en.mp4", "fr": "/path/fr.mp4"},
  "youtube": {
    "sourceLanguage": "en",
    "tags": ["monitoring", "docker"],
    "categoryId": "28",
    "thumbnail": "/path/thumbnail.png",
    "texts": {
      "en": {"title": "…", "description": "…"},
      "fr": {"title": "…", "description": "…"}
    }
  },
  "networks": {
    "instagram": {"en": "caption…", "fr": "légende…"},
    "linkedin": {"en": "…", "fr": "…"},
    "pinterest": {"en": {"title": "…", "caption": "…"}}
  }
}
```

Then run:

```sh
python3 scripts/build_pack.py brief.json my-pack.zip
```

The script refuses a brief that breaks a limit and says which text to shorten:
fix the text and run it again. `thumbnail` and `categoryId` are optional; YouTube
is optional too (a pack can target only social networks). The YouTube video is the
source language's edit; the other languages become YouTube translations of it.

### Without the script

When `scripts/build_pack.py` is not available, write the same layout with any ZIP
tool, checking the limits of step 2 yourself:

- `common/<lang>/video.mp4`: each edit, stored uncompressed.
- `youtube/post.json`: `{"version":1,"video":"<source>/video.mp4","sourceLanguage":"<source>","languages":[…],"categoryId":"28","tags":[…]}`
  (add `"thumbnail":"thumbnail.png"` with `youtube/thumbnail.png` if given).
- `youtube/<lang>/title.txt` and `youtube/<lang>/description.txt` for every language in `languages`.
- `<network>/<lang>/caption.txt` for each social network and language (UTF-8),
  plus `pinterest/<lang>/title.txt` when a Pin title is given. Every
  `<network>/<lang>/` needs a `common/<lang>/video.mp4`.
- Lowercase network and language folder names; no other files are needed.

## 4. Hand over

Give the user the ZIP and a short table of what it contains (network × language,
first words of each caption). Remind them to import it in SocialDock
(**Publications → Import a pack**), review the captions and destinations, then
publish. Local ZIPs can hold videos up to 16 GiB.

More about SocialDock and the pack format: https://app.socialdock.studio/skill
