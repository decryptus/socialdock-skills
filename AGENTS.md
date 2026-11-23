# Repository scope

This public repository distributes the SocialDock plugin for Claude
(`socialdock`), listed in Anthropic's plugin directory and installable from
Claude Code with `/plugin install socialdock --marketplace decryptus/socialdock-skills`.
It holds the plugin manifest, the marketplace manifest, the listing icon and
banners, the `socialdock-pack` skill, and `chatgpt/`, the same builder as a custom
GPT for ChatGPT (instructions mirrored from the skill, Markdown only).

The SocialDock product lives elsewhere and owns the contracts this plugin
follows: the private [decryptus/socialdock](https://github.com/decryptus/socialdock)
repository owns the extension, the Android app, the pack format
(`docs/PACK-FORMAT.md`), the network limits, the `build_pack.py` helper and its
tests; [decryptus/socialdock-core](https://github.com/decryptus/socialdock-core)
owns the connection service and the public site (including `/skill`). Change a
shared contract in its owning repository first, then mirror it here.

# Engineering requirements

Adapted for this plugin from
[decryptus/monit-docker AGENTS.md](https://github.com/decryptus/monit-docker/blob/master/AGENTS.md)
(blob `efc17bc4913d528c1818be36ce3ee2652ca98c91`) and
[decryptus/socialdock AGENTS.md](https://github.com/decryptus/socialdock)
(blob `e325264444b066f4251e159d484e8aae6ea2aa18`, commit `50a03f3`), reviewed
November 22, 2026.

These are maintainer requirements, not optional preferences. Existing violations
are debt to remove, not examples to copy.

## Dependencies and responsibilities

- The plugin is instructions only. Skills tell Claude what to ask, what to write
  and how to lay out a pack; Claude does the work with its own file tools. Do not
  add runtime code, MCP servers, hooks or package installs to the plugin.
- The pack format, folder layout and per-network limits belong to SocialDock. The
  skill restates them; it never extends or reinterprets them. A pack the skill
  describes must be accepted by the SocialDock pack reader unchanged.
- Publication belongs to SocialDock, after the user's confirmation. A skill never
  publishes, schedules, uploads or connects to a social network account.
- Keep each skill focused on one task with explicit inputs, outputs and hand-over.
  A new capability is a new skill folder, not an extra mode hidden in an existing one.

## Style and validation

- Write repository files, manifests, skill instructions and developer messages in
  English. Content Claude writes for the user follows the user's languages; the
  interface language never rewrites imported or generated publication text.
- Declare each limit once per skill in a single table (name, unit, value) and keep
  units explicit: characters versus UTF-8 bytes. Keep values identical to the
  SocialDock pack reader.
- Name files, folders and identifiers with lowercase letters, digits and hyphens;
  keep paths valid on Windows and macOS. Treat network names and language codes as
  exact identifiers (`instagram`, `fr`, `pt-BR`), never as patterns.
- Tell Claude to refuse or shorten invalid input explicitly (over-long text,
  missing edit for a language, unknown network) rather than producing a pack that
  SocialDock will reject or, worse, partially accept.

## Product constraints

- Private by design: a skill reads only the local files the user names and writes
  the pack next to them. No network requests, no data sent, no account, key or
  token, no telemetry. Any change to this requires an explicit product decision
  and an updated README, listing answers and privacy page.
- Never store or relay customer video bytes on SocialDock servers (same rule as
  SocialDock); the plugin never handles hosting.
- Never invent facts, prices, dates, results or quotes in generated texts; a thin
  brief yields neutral texts and a note on what to add.
- Never present the plugin as official Anthropic software or use another brand's
  name or likeness. The listing name is `socialdock`, publisher DooWan.
- Contact for Anthropic and users: contact@socialdock.studio.

## Directory rules (blocking)

- From organisations that are not Verified, the directory accepts only Markdown,
  plain text, JSON, YAML and PNG/JPEG/GIF/WebP images. No scripts (`.py`, `.sh`,
  files starting with `#!`), no SVG other than the icon, no package manager files,
  no `__pycache__`, `.DS_Store` or other system files. Keep `.gitignore` current.
- Keep every non-image file under 256 KiB, the plugin under 512 files, and the
  repository well under the directory size limits.
- `.claude-plugin/plugin.json` keeps `name`, `displayName`, `version` (raised with
  every release), `description`, `author`, `license`, `keywords`, the listing links
  (`homepage`, `privacyPolicyUrl`, `termsOfServiceUrl`, `supportUrl`,
  `documentationUrl`) and `icon`. The directory froze the listing icon
  (`.claude-plugin/icon.png`) at the first submission.
- The README describes everything the plugin reads, writes, sends or fetches, and
  must stay at least 40 words outside code blocks.

## Review and verification

- Run `claude plugin validate .` before every push. Only the directory-only
  warnings (`icon` and listing-link fields) are acceptable.
- Validate in the developer portal (claude.ai/directory/manage) for changes to
  files, manifests or structure; fix every blocking finding before pushing to
  `main`, which the directory scans and, after the first approval, publishes.
- After a change to a skill, generate a pack from a real brief and read it with
  the SocialDock pack reader in the private repository
  (`tests/test_build_pack.py` there). Compare output with and without the plugin
  (`claude plugin eval`) before releasing behaviour changes.
- Report confirmed issues and remaining limits. A passing validation is not
  acceptance of the generated content; review sample outputs per network.

## Test discovery and execution

- This repository holds no executable tests by design (the directory refuses
  scripts). Tests for the pack contract run in `decryptus/socialdock`
  (`npm test`, `python3 -m unittest discover -s tests -p 'test_*.py'`).
- Do not add Python, shell or Node files here, even for tests or CI helpers. Keep
  any CI limited to YAML that runs public tools without committing scripts.

## Copyright review

- Review project-owned copyright notices and manifest metadata when preparing a
  release. Keep the original start year and attribution (DooWan, 2026) and update
  the end year for maintained material to reflect actual project work.
- Keep `plugin.json`, `marketplace.json`, the README and the LICENSE consistent.
  Do not alter the dates in the standard license text.

## Separate user and contributor documentation

- `README.md` is the user entry point (what the plugin does and does not do,
  install, example, limits, privacy, support). `AGENTS.md` and `ROADMAP.md` are
  contributor material; keep maintainer procedures, portal steps and account
  details out of the README and the listing.
- The public FR/EN page (`/skill`, in `decryptus/socialdock-core`) is user
  documentation: update it with the README when behaviour, install steps or
  contact change. Never include credentials or private infrastructure evidence.
- Before delivery, check links in the README, the listing and the public page.

## Internationalization

- Skills write natively in each language the user asks for, never by literal
  translation, and keep brand words and URLs as given.
- User-facing documentation exists in English (README, listing) and French and
  English (public page). A French README section is planned; keep both languages
  equivalent when it exists.

## Complete delivery and release synchronization

- Treat every release as a consistency check across: `plugin.json` version, the
  directory listing (validation, scan, review and published version in the
  developer portal), this README, the public `/skill` page, the SocialDock
  roadmap, and the private copy of the skill in `decryptus/socialdock`.
- Distinguish submitted, approved, published and deployed states in `ROADMAP.md`;
  never list a version as published before the portal shows it live.
- Never rewrite published history to change a released version; release a new
  version instead.
- Complete the authorized delivery work before reporting success, and list any
  surface still not updated with its concrete blocker.

## Shared component placement

- Pack-format and limit changes belong to `decryptus/socialdock`; site and
  contact changes to `decryptus/socialdock-core`. This repository only mirrors
  them. Record in the contribution which repository owns a new rule.

## Brand assets placement

- Keep brand assets under `assets/brand/`: `png/` for raster exports and
  `social/` for the GitHub social preview and Open Graph images. Do not add
  `svg/` or any SVG: the directory rules above allow no SVG other than the icon.
- The listing icon stays at `.claude-plugin/icon.png`; the directory froze it at
  the first submission. Never move or replace it.
- Name new files without the project prefix and, for raster exports, with the
  pixel width: `logo-horizontal-1024.png`, `logo-horizontal-dark-1024.png`.
- Keep the GitHub social preview at
  `assets/brand/social/social-preview-1280x640.png` (1280×640, under 1 MB),
  derived from the existing artwork. Do not redesign the brand.
- Do not move or rename an existing asset without updating every reference
  (README, plugin metadata, website) in the same change.

## Commit authorship

Write every commit as `decryptus <decryptus@users.noreply.github.com>`, as both author and committer (run `git config user.name decryptus` and `git config user.email decryptus@users.noreply.github.com` before committing, including when rebasing). Do not add `Co-Authored-By` lines, session links or any mention of an assistant or tool in commit messages. Do not rewrite history already published on the default branch to fix older commits.
