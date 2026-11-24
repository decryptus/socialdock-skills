# SocialDock for ChatGPT

The public plugin is prepared but is not yet submitted, approved or published in the OpenAI directory.

Create multilingual SocialDock video packs from a video and a brief. The plugin bundles the existing SocialDock pack builder instructions for YouTube, Instagram, Facebook, LinkedIn, TikTok, Pinterest and Threads.

Provide the video edits, a short description, target networks and languages. The model writes network-specific texts, checks the format limits and creates an importable ZIP when file tools are available. Import it into SocialDock under **Publications → Import a pack**, review destinations and captions, then publish from SocialDock.

## Example

“Create a French and English SocialDock pack from these two edits. The video introduces our mosaic workshop. Target YouTube, Instagram and TikTok. Keep the tone warm and use only the facts in this brief.”

## Requirements and limits

The complete workflow needs an environment capable of reading files and creating ZIPs, such as ChatGPT Work. Actual attachment, execution and download limits depend on the host. SocialDock's local 16 GiB pack capacity does not imply ChatGPT accepts a 16 GiB upload. If a required video cannot be read or a ZIP cannot be created, the task is incomplete; text output alone is not an import-ready pack.

## Privacy and publishing

The plugin contains instructions and a logo only. It has no MCP server, account connection, API key, telemetry or publishing tool. Videos and briefs are handled by the ChatGPT environment in which you use it, subject to that service's data controls. The plugin does not send them to SocialDock servers or social networks. Publication takes place separately in SocialDock, after your review.

Publisher: DooWan. Support: contact@socialdock.studio.

[Documentation](https://socialdock.studio/skill) · [Privacy](https://socialdock.studio/privacy) · [Terms](https://socialdock.studio/terms)

## Shared instructions

The plugin uses [`../skills/socialdock-pack/SKILL.md`](../skills/socialdock-pack/SKILL.md) unchanged. ChatGPT-specific listing metadata lives in `plugin.json` in this directory. The same skill is shared with Claude; network limits and the pack format have one source.
