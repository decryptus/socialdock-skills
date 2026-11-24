# Publishing the ChatGPT plugin

The source repository separates provider metadata while sharing pack instructions:

| Repository path | Role |
| --- | --- |
| `.claude-plugin/` | Existing Claude manifest, marketplace and frozen listing icon |
| `chatgpt/plugin.json` | OpenAI portable plugin manifest and EN/FR listing |
| `chatgpt/README.md` | ChatGPT user guide |
| `skills/socialdock-pack/SKILL.md` | Shared pack builder, included unchanged |
| `assets/icon.png` | Shared distribution icon, initially identical to the frozen Claude icon |
| `LICENSE` | Shared MIT license |

`chatgpt/` is an authoring directory, not a standalone installable plugin directory.
Do not zip only `chatgpt/`: the skill and icon would be missing. The assembled ZIP
has `plugin.json`, `skills/` and `assets/` at its root. Leave `.claude-plugin/` in
place because the current Claude submission uses the repository root.

## Assemble the ZIP

From the repository root, run the following with Python 3. This command only
packages tracked public files and writes the ZIP outside the repository. It
does not install dependencies, change the skill, upload anything or publish.

```python
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path.cwd()
manifest = json.loads((root / "chatgpt/plugin.json").read_text(encoding="utf-8"))
assert manifest["name"] == "socialdock"
files = {
    "chatgpt/plugin.json": "plugin.json",
    "chatgpt/README.md": "README.md",
    "skills/socialdock-pack/SKILL.md": "skills/socialdock-pack/SKILL.md",
    "assets/icon.png": "assets/icon.png",
    "LICENSE": "LICENSE",
}
for source in files:
    assert (root / source).is_file(), source
interface = manifest["extensions"]["com.openai"]["interface"]
for field in ("composerIcon", "logo"):
    assert interface[field].removeprefix("./") in files.values(), field
archive = root.parent / f"socialdock-chatgpt-{manifest['version']}.zip"
with ZipFile(archive, "w", compression=ZIP_DEFLATED) as output:
    for source, destination in files.items():
        output.write(root / source, destination)
with ZipFile(archive) as output:
    assert output.testzip() is None
    assert set(output.namelist()) == set(files.values())
    for source, destination in files.items():
        assert output.read(destination) == (root / source).read_bytes()
print(archive)
```

Keep ZIPs, temporary build folders and executable scripts out of this
instruction-only repository. Source changes to the skill belong in the shared
skill, with the SocialDock pack-contract tests required by `AGENTS.md`.

## Review and submit

1. Run `claude plugin validate .` before pushing source changes. Validate the
   Claude directory submission before merging structural changes to `main`.
2. Assemble and inspect the ZIP above. Test the imported skill in a fresh ChatGPT
   environment with file execution available: use short MP4 edits and a real
   brief, check the generated pack with SocialDock, and review every caption.
3. Open <https://platform.openai.com/plugins>. Choose the owning organization,
   project and verified developer identity, then upload the ZIP as a skills-only
   plugin. Do not add an MCP connection: this package has none.
4. Review the imported metadata, EN/FR listing, logo and skill scan. Fix blocking
   findings in the source package and upload a corrected ZIP.
5. Submit for review after all required checks and attestations are complete.
   Approval and publication are separate steps; publish only the approved version.
6. Update `ROADMAP.md`, the README and the public SocialDock skill page with the
   actual status and install link. For later uploads, retain the plugin identity
   and increment the OpenAI manifest version; do not label a draft as published.

The shared skill's local 16 GiB pack capacity is not a ChatGPT attachment limit.
Test the complete workflow within the host's actual upload, execution and output
limits. No SocialDock account, social-network token or API key is needed here.

## References

- <https://developers.openai.com/plugins/build/plugins>
- <https://developers.openai.com/plugins/deploy/submission>
- <https://developers.openai.com/plugins/guides/submit-claude-plugin>

Status on November 24, 2026: the uploaded 1.0.0 draft shows Needs attention.
The portal reports that new skills-only submissions are not being accepted.
Version 1.0.1 corrects both publisher fields to Le New Deal and is prepared for
manual upload using Upload new version. This metadata correction does not resolve
the skills-only submission restriction. No MCP server is included. Approval and
publication remain outstanding.
