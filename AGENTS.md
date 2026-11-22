# Repository scope

Public distribution of the SocialDock plugin for Claude (`socialdock`), listed in
Anthropic's plugin directory and installable from Claude Code with
`/plugin install socialdock --marketplace decryptus/socialdock-skills`.

SocialDock itself (extension, Android app, pack format, the `build_pack.py`
helper and its tests) lives in the private repository `decryptus/socialdock`;
the connection service lives in `decryptus/socialdock-core`. The pack format,
network limits and product wording are owned there: change them there first,
then mirror them here.

# Requirements

## Directory rules (blocking)

- The directory accepts only Markdown, plain text, JSON, YAML and PNG/JPEG/GIF/WebP
  images from organisations that are not Verified. No scripts (`.py`, `.sh`, files
  starting with `#!`), no SVG other than the icon, no package manager files, no
  `__pycache__`, `.DS_Store` or other system files. Keep `.gitignore` up to date.
- Keep every non-image file under 256 KiB, the plugin under 512 files, and every
  path valid on Windows and macOS.
- `.claude-plugin/plugin.json` keeps `name: socialdock`, `version` (raise it with
  every release), `description`, `author`, `license`, the listing links
  (`homepage`, `privacyPolicyUrl`, `termsOfServiceUrl`, `supportUrl`,
  `documentationUrl`) and `icon` (`.claude-plugin/icon.png`, square PNG; the
  directory froze the listing icon at the first submission).
- README of at least 40 words, describing everything the plugin reads, writes,
  sends or fetches. Today: it reads the local files the user names and writes one
  ZIP; no network, no data sent, no account or key, no publication.

## Content

- Write repository files in English. Skill texts that Claude produces follow the
  user's languages.
- `skills/socialdock-pack/SKILL.md` must stay self-sufficient: Claude builds the
  ZIP with its own file tools from the layout and limits written there. Keep its
  limits identical to the SocialDock pack reader (YouTube title 100 characters,
  description 5,000 UTF-8 bytes, tags 450; Instagram and TikTok 2,200; LinkedIn
  3,000; Facebook 63,206; Pinterest 800 / title 100; Threads 500 UTF-8 bytes).
- Never add credentials, tokens, private infrastructure details or customer data.
- Never present the plugin as official Anthropic software.

## Verification and release

- Run `claude plugin validate .` before pushing; it must pass without warnings
  other than the directory-only `icon` and listing-link fields.
- After a change to the skill, check a generated pack with the SocialDock pack
  reader from the private repository (`tests/test_build_pack.py` there).
- Pushes to `main` are scanned by the directory and published automatically once
  the first version is approved. Raise `version` in `plugin.json`, then record the
  release in `ROADMAP.md`.
- Contact for Anthropic and users: contact@socialdock.studio.
