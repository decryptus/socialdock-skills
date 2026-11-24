![SocialDock](assets/socialdock-skill-banner-light.png#gh-light-mode-only)
![SocialDock](assets/socialdock-skill-banner-dark.png#gh-dark-mode-only)

# SocialDock skills for Claude and ChatGPT

**One video, every network, every language.** Give the model your video edits and a
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

The model asks only for what is missing, writes the texts within each network's
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

- Reads the video edits and optional thumbnail you provide and creates a ZIP
  using the host's file tools. In hosted environments such as ChatGPT, files and
  prompts are processed under that service's data controls.
- The plugin makes **no network requests**, sends no data to SocialDock servers
  or social networks, needs **no SocialDock account, API key or token**, and
  **never publishes**. Publishing happens later in SocialDock after your review.
- The plugin is a single instruction file, `skills/socialdock-pack/SKILL.md`: no
  scripts, no dependencies, nothing to install. Read it: it is short.

## Pack format

`common/<lang>/video.mp4` (stored uncompressed), `youtube/post.json`,
`youtube/<lang>/title.txt` and `description.txt`, `<network>/<lang>/caption.txt`.
Local packs can hold videos up to 16 GiB.

## Support

DooWan · [contact@socialdock.studio](mailto:contact@socialdock.studio) ·
[app.socialdock.studio/skill](https://app.socialdock.studio/skill) · MIT licence

## ChatGPT

The public ChatGPT plugin is prepared but is **not yet submitted, approved or
published** in the OpenAI directory. See [`chatgpt/`](chatgpt/README.md) for its
capabilities and requirements. It uses the same shared skill and prepares files
under the user's own ChatGPT account. Creating the ZIP requires file tools;
attachment and output limits depend on the host, independently of SocialDock's
local pack capacity.

