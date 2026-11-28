# SocialDock Pack for ChatGPT

The same pack builder as the Claude skill (`skills/socialdock-pack`), packaged as a
custom GPT so ChatGPT users can prepare a SocialDock pack too: they attach their video
edits and a short brief, the GPT writes the texts per network and language, builds the
ZIP with its code tool, and they import it in SocialDock (**Publications → Import a
pack**). Nothing is published from ChatGPT.

`instructions.md` is the GPT's instructions, derived from `skills/socialdock-pack/SKILL.md`;
change the skill first, then mirror the change here (under 8,000 characters).

## GPT settings

| Field | Value |
| --- | --- |
| Name | SocialDock Pack |
| Description | Turn a video and a short brief into a SocialDock pack: YouTube titles and descriptions, and captions for Instagram, TikTok, Facebook, LinkedIn, Pinterest and Threads, in several languages. |
| Instructions | Content of `instructions.md` |
| Conversation starters | "Here is my video, make a pack for YouTube, Instagram and TikTok in French and English" · "I have one video per language: build the SocialDock pack" · "Write the texts only, I will add the videos myself" · "What does a SocialDock pack contain?" |
| Knowledge | none (the format is in the instructions) |
| Capabilities | Code Interpreter & Data Analysis **on**; Web Search and image generation **off** |
| Actions | none (no account, key or network access) |
| Profile picture | `assets/brand/social/social-preview-1280x640.png` cropped to a square, or the orange SocialDock symbol |

## Publishing (owner, in ChatGPT)

1. In ChatGPT, open **Explore GPTs → Create**, switch to **Configure** and fill the
   fields above.
2. Builder profile: verify the domain `socialdock.studio` (DNS TXT record) so the GPT
   shows SocialDock as its builder, and add the support e-mail contact@socialdock.studio.
3. Privacy policy URL: https://socialdock.studio/privacy (required for a public GPT).
4. **Create → Everyone** (GPT Store), category *Productivity*.

The GPT runs under each user's own ChatGPT account: it costs SocialDock nothing.
