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

## ChatGPT

- Custom GPT "SocialDock Pack" prepared in `chatgpt/` (November 23, 2026): instructions derived from the skill, settings and publication steps. Not yet created in ChatGPT (needs the owner's ChatGPT account and builder-profile domain verification).
