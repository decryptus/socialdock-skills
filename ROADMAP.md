# Roadmap

## 1.0.0 — submitted November 22, 2026

- `socialdock-pack` skill: writes YouTube titles and descriptions and captions for
  Instagram, Facebook, LinkedIn, TikTok, Pinterest and Threads in several languages
  from video edits and a brief, then builds a SocialDock pack ZIP.
- Instruction-only plugin (directory rules for non-Verified organisations): no
  scripts, nothing to install.
- Submitted to Anthropic's plugin directory (portal validation passed; waiting for
  the security scan and review). Public page: https://socialdock.studio/skill.

## 1.0.2 — prepared November 28, 2026 (not released)

- The skill and the ChatGPT instructions can write optional `prompt.txt` files (root for
  every text, `<network>/prompt.txt` for one network) that SocialDock sends to the user's
  AI at import; web addresses always in full with `https://`; texts shortened at the end
  of a sentence or word, never in the middle. Release: copy to `release` per AGENTS.md.

## Next

- After approval: publish the first version, set up push updates on the plugin's
  page in the developer portal (Settings → Updates), check the listing.
- Short demo video (scenario to prepare) and a French README section.
- Compare output with and without the plugin (`claude plugin eval`) on a few real
  briefs; tune the per-network guidance.
- Keep the layout and limits in step with the SocialDock pack format; consider a
  second skill for reviewing or adapting existing captions.
- The same assistant now runs inside the SocialDock extension and app (pack
  creator "Suggest with AI", with the person's own Anthropic/OpenAI key, Ollama or
  SocialDock AI; November 23, 2026). Keep its per-network guidance in step with
  this skill.

## ChatGPT

- Custom GPT "SocialDock Pack" prepared in `chatgpt/` (November 23, 2026): instructions derived from the skill, settings and publication steps. Not yet created in ChatGPT (needs the owner's ChatGPT account and builder-profile domain verification).
