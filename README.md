![SocialDock](assets/socialdock-skill-banner-light.png#gh-light-mode-only)
![SocialDock](assets/socialdock-skill-banner-dark.png#gh-dark-mode-only)

# SocialDock skill for Claude

**One video, every network, every language.** Give Claude your video edits and a
few words about the video: it writes the YouTube titles and descriptions and the
captions for Instagram, Facebook, LinkedIn, TikTok, Pinterest and Threads, natively
in each language you need, then builds a **SocialDock pack**, one ZIP that the
[SocialDock](https://app.socialdock.studio/skill) Chrome extension or Android app
imports. You review every text and destination in SocialDock before anything is
published.

## Install

- **Claude (web, desktop, Cowork)**: add **SocialDock** from the plugin directory.
- **Claude Code**:

  ```
  /plugin install socialdock --marketplace decryptus/socialdock-skills
  ```

## Try it

> Make a SocialDock pack for `fr.mp4` and `en.mp4` for YouTube, Instagram and
> LinkedIn. It's a tutorial on monitoring Docker containers, friendly tone, link
> to our website.

Claude asks only for what is missing, writes the texts within each network's
limits, builds the ZIP with its own file tools and hands it over with a table of
what it contains.

## What you get

| | |
| --- | --- |
| YouTube | Searchable title and description per language, tags, optional thumbnail; one video with translations |
| Instagram · Facebook · TikTok | Reel captions written for each network, hashtags where they help |
| LinkedIn | A professional post per language |
| Pinterest | Pin title and description |
| Threads | A short conversational post |

Limits checked before the ZIP is written: YouTube title 100 characters,
description 5,000 UTF-8 bytes, tags 450 characters; Instagram and TikTok 2,200
characters; LinkedIn 3,000; Facebook 63,206; Pinterest caption 800 and title 100;
Threads 500 UTF-8 bytes. Every network and language needs a matching video edit.

## Private by design

- Reads only the local files you point it to (your MP4 edits and an optional
  thumbnail) and writes one ZIP file next to them.
- Makes **no network requests**, sends **no data** anywhere, needs **no account,
  API key or token**, and **never publishes**: publishing happens later, in
  SocialDock, after your confirmation.
- The plugin is a single instruction file, `skills/socialdock-pack/SKILL.md`: no
  scripts, no dependencies, nothing to install. Read it: it is short.

## Pack format

`common/<lang>/video.mp4` (stored uncompressed), `youtube/post.json`,
`youtube/<lang>/title.txt` and `description.txt`, `<network>/<lang>/caption.txt`.
Local packs can hold videos up to 16 GiB.

## Support

Le New Deal · [contact@socialdock.studio](mailto:contact@socialdock.studio) ·
[app.socialdock.studio/skill](https://app.socialdock.studio/skill) · MIT licence

## ChatGPT

The same pack builder exists as a custom GPT for ChatGPT users: see
[`chatgpt/`](chatgpt/README.md) for its instructions and settings. It also only
prepares files, under the user's own ChatGPT account.

