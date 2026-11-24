# Connected ChatGPT package

`chatgpt-mcp/` is the connected authoring directory. Keep `chatgpt/` as the
standalone version. The MCP implementation belongs to `decryptus/socialdock-core`
and is not copied into this public package. Do not add runtimes or scripts here.

The connected skill wraps the shared workflow: package the tracked shared
`skills/socialdock-pack/SKILL.md` unchanged as its reference. This avoids separate
copies of pack-format instructions in the source repository.

## Assemble

Run this from the repository root; the archive is an intermediate build outside
the repository, not a release or an upload:

```python
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path.cwd()
manifest = json.loads((root / "chatgpt-mcp/plugin.json").read_text())
files = {
    "chatgpt-mcp/plugin.json": "plugin.json",
    "chatgpt-mcp/mcp.json": "mcp.json",
    "chatgpt-mcp/README.md": "README.md",
    "chatgpt-mcp/SKILL.md": "skills/socialdock-pack/SKILL.md",
    "skills/socialdock-pack/SKILL.md": "skills/socialdock-pack/references/pack-format.md",
    "assets/icon.png": "assets/icon.png",
    "LICENSE": "LICENSE",
}
archive = root.parent / f"socialdock-chatgpt-mcp-{manifest['version']}.zip"
with ZipFile(archive, "w", ZIP_DEFLATED) as output:
    for source, destination in files.items():
        output.write(root / source, destination)
with ZipFile(archive) as output:
    assert output.testzip() is None
    assert set(output.namelist()) == set(files.values())
    for source, destination in files.items():
        assert output.read(destination) == (root / source).read_bytes()
print(archive)
```

`mcp.json` declares Streamable HTTP and `auth.type: none` for the public read-only
tools. Never reuse extension OAuth tokens or insert a secret into the package.
Five positive and three negative review cases are prepared in `plugin.json`;
these are expected behaviors to test, not results already observed.

## Acceptance before submission

1. Pass the core's actual OpenResty/HTTP tests and deploy through its existing
   workflow. Confirm HTTPS `initialize`, `tools/list` and all three tool calls at
   `https://api.socialdock.studio/mcp`, including non-ASCII text.
2. Update the public site's privacy and skill pages to describe the connected
   version's text/metadata transfer. Verify that the published disclosures match
   both this README and the actual service. Keep standalone privacy distinct.
3. Run the repository's Claude validation and portal structure checks before
   merging to main. The connected directory contains only allowed text/JSON
   source; it is not a Claude runtime or a new root MCP configuration.
4. Test the assembled package in ChatGPT with real edits and a brief. Inspect
   the resulting ZIP with SocialDock. Exercise all review cases and record a
   reviewer-accessible walkthrough; no demo recording URL is invented here.
5. Create a **new plugin draft including MCP from its first upload**. The
   [current OpenAI guide](https://developers.openai.com/plugins/deploy/submission)
   says an MCP server cannot be added to an existing skills-only plugin. The
   connected package uses identity `socialdock-mcp`, distinct from `socialdock`.
6. Select the verified **Le New Deal** developer identity. Manifest labels alone
   do not replace the portal's verified publishing identity. Complete the API
   domain verification and connect/scan the no-auth MCP server in the portal.
7. Resolve findings, supply the demonstration, review the required attestations
   and submit. Approval and public publication remain separate outcomes.

Do not remove the old draft or claim a public release while these checks remain
outstanding. Local ZIP validation is not portal approval.

References: [packaging](https://developers.openai.com/plugins/build/plugins),
[submission](https://developers.openai.com/plugins/deploy/submission).
