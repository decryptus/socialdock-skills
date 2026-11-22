# SocialDock skills for Claude

This plugin teaches Claude to prepare a **SocialDock pack**: from your video edits
and a few words about the video, Claude writes YouTube titles and descriptions and
captions for Instagram, Facebook, LinkedIn, TikTok, Pinterest and Threads, natively
in each language you need, then builds one ZIP that the
[SocialDock](https://app.socialdock.studio/skill) Chrome extension or Android app
imports. You review every text and destination in SocialDock before anything is
published.

## Install

- **Claude (web, desktop, Cowork)**: add **SocialDock** from the plugin directory.
- **Claude Code**:

  ```
  /plugin install socialdock --marketplace decryptus/socialdock-skills
  ```

## Skill

- **socialdock-pack** — "Make a SocialDock pack for this video in French and
  English for YouTube, Instagram and LinkedIn." Claude asks for what is missing
  (edits, subject, tone, links), writes the texts within each network's limits and
  runs `scripts/build_pack.py` to lay out the pack and check every limit.

## What it does and does not do

- Reads only the local files you point it to (your MP4 edits and an optional
  thumbnail) and writes one ZIP file next to them.
- Makes **no network requests**, sends **no data** anywhere, needs **no account,
  API key or token**, and never publishes: publishing happens later, in SocialDock,
  after your confirmation.
- The script uses the Python standard library only (no package install).
- Videos are stored uncompressed in the ZIP; texts are UTF-8.

## Limits enforced

YouTube title 100 characters, description 5,000 UTF-8 bytes, tags 450 characters;
Instagram and TikTok 2,200 characters; LinkedIn 3,000; Facebook 63,206; Pinterest
caption 800 and title 100; Threads 500 UTF-8 bytes. Every network and language
folder needs a matching video edit.

## Pack format

`common/<lang>/video.mp4`, `youtube/post.json`, `youtube/<lang>/title.txt` and
`description.txt`, `<network>/<lang>/caption.txt`. Local packs can hold videos up
to 16 GiB.

## Support

DooWan · socialdock@doowan.net · https://app.socialdock.studio/skill

The source of this skill is maintained with SocialDock; this repository is its
public distribution.
