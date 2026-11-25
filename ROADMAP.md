# Roadmap

## 1.0.0 — submitted November 22, 2026

- `socialdock-pack` skill: writes YouTube titles and descriptions and captions for
  Instagram, Facebook, LinkedIn, TikTok, Pinterest and Threads in several languages
  from video edits and a brief, then builds a SocialDock pack ZIP.
- Instruction-only plugin (directory rules for non-Verified organisations): no
  scripts, nothing to install.
- Submitted to Anthropic's plugin directory (portal validation passed; waiting for
  the security scan and review). Public page: https://socialdock.studio/skill.

## Next

- After approval: publish the first version, set up push updates on the plugin's
  page in the developer portal (Settings → Updates), check the listing.
- Short demo video (scenario to prepare) and a French README section.
- Compare output with and without the plugin (`claude plugin eval`) on a few real
  briefs; tune the per-network guidance.
- Keep the layout and limits in step with the SocialDock pack format; consider a
  second skill for reviewing or adapting existing captions.
- Later, the same assistant inside the SocialDock extension and app (roadmap of
  `decryptus/socialdock`).

## ChatGPT — package prepared November 24, 2026

- Public skills-only plugin 1.0.0: `chatgpt/plugin.json`, English and French
  directory metadata, shared `assets/icon.png` and `skills/socialdock-pack/SKILL.md`.
- Provider-specific metadata and guides are separated: `.claude-plugin/` for
  the existing Claude integration, `chatgpt/` for OpenAI. Pack instructions remain
  shared; the obsolete custom GPT instruction copy now points to that source.
- Reproducible ZIP assembly and submission steps: `chatgpt/PUBLISHING.md`.
- Status: prepared, not uploaded to OpenAI, not submitted, not approved, not
  published. Local package checks do not replace directory review.
- Before release: validate the assembled package in the OpenAI portal, test it
  in a fresh ChatGPT conversation, and update the public skill page with the
  actual install link only after publication. Claude portal validation remains
  required before merging repository-structure changes to `main`.

## ChatGPT 1.0.1 — corrected draft, November 24, 2026

- Set author and displayed developer to Le New Deal and align the packaged guide
  and license with the publisher already recorded on main.
- The uploaded 1.0.0 draft shows Needs attention: the OpenAI portal reports that
  new skills-only submissions are not accepted, plus a category warning.
- The corrected 1.0.1 ZIP is prepared for manual upload, not submitted, approved
  or published. Changing publisher metadata does not remove the submission block.
# Connected ChatGPT variant — November 24, 2026

- Prepared `chatgpt-mcp/` as a separate development variant with Le New Deal
  publisher, no-auth Streamable HTTP metadata, a connected workflow wrapping the
  shared pack instructions, and five positive/three negative review cases.
- Server PR #68 is merged and deployment run 45476296916 succeeded. The endpoint
  `https://api.socialdock.studio/mcp` responds in production on the existing core
  port; initialization, discovery and all three tools passed live HTTPS checks.
  The host Nginx adjustment is verified: exactly 512 KiB passes and one extra
  byte returns 413. A 63,206-character accented Facebook caption passed the
  public text check.
- Keep `chatgpt/` maintained as the standalone version. No shared skill change.
- Core CI passed: 34 MCP Lua contracts and 6 actual HTTP tests. Package archive
  checks and Claude CLI validation passed. OpenAI portal ingestion must confirm
  its documented authentication extension (not recognized by the generic schema).
- Outstanding: public privacy/skill disclosure updates,
  ChatGPT acceptance and demo recording, Claude structural validation before
  main merge, new MCP draft, domain verification, review and publication.
- No connected package has been submitted or approved by these source changes.
