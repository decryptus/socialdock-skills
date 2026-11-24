# SocialDock for ChatGPT — connected version

Prepare multilingual video packs and check their texts and declared file paths
with the SocialDock MCP service. ChatGPT writes the captions and assembles the
ZIP using its file tools; SocialDock supplies pack rules and metadata checks.

**Status:** development draft 0.1.0. Source is prepared; endpoint deployment,
live ChatGPT connection, directory review and publication are separate steps.
Publisher: **Le New Deal**.

## What it does

- Retrieves the format and text-counting rules for the requested networks.
- Checks YouTube titles, descriptions and tags, and social captions.
- Checks declared post.json fields and relative file names.
- Helps create a ZIP to import and review in SocialDock before publishing.

Try: “Prepare a French and English SocialDock pack for YouTube and Instagram
from these two edits, and check the texts and declared paths.”

## Privacy and limits

The connected version sends the **selected text, manifest fields and file names**
to `https://api.socialdock.studio/mcp`. The server processes that metadata in
memory without storing it in Redis or logging its content. Do not send secrets
or sensitive names. Videos, audio, images and ZIP bytes are not sent to MCP.
Your ChatGPT environment processes the files under its own data controls.

No SocialDock account, API key or social token is required. The tools cannot
connect accounts, inspect remote media, import a pack or publish posts. A passing
metadata check does not mean the ZIP, its videos or a publication have been
validated. Inspect the actual pack in SocialDock before publishing.

ZIP creation requires file tools and stays subject to your ChatGPT environment's
upload and output limits. The server accepts one text per check, at most 256 KiB
of UTF-8, within a 512 KiB JSON request. Manifest checks accept up to 512 declared
paths of 240 UTF-8 bytes each. These are API limits, not SocialDock ZIP limits.

## Standalone version

The standalone ChatGPT package remains separate and supported. It uses the shared
pack instructions without calling the SocialDock MCP service. This connected
package uses the same pack workflow and adds remote metadata checks.

## Français

Cette version connectée prépare les packs et vérifie les textes ainsi que les
chemins déclarés. Seuls les textes, champs du manifeste et noms de fichiers
choisis sont transmis à l'API SocialDock. Aucune vidéo ni archive ZIP n'est envoyée
au serveur MCP. Aucun compte SocialDock n'est nécessaire, aucun réseau social
n'est connecté et aucune publication n'est effectuée. Les fichiers restent
traités dans votre environnement ChatGPT selon ses propres règles de données.

Les contrôles portent sur les métadonnées déclarées, pas sur les fichiers réels.
Importez le pack dans SocialDock pour relire les textes, inspecter les médias et
choisir les destinations avant de publier. La création du ZIP dépend des outils
et des limites de votre environnement ChatGPT. Cette version est un brouillon de
développement, pas un plugin déjà publié.

[SocialDock](https://socialdock.studio/skill) ·
[Privacy](https://socialdock.studio/privacy) ·
[Terms](https://socialdock.studio/terms) ·
[Support](https://github.com/decryptus/socialdock-skills/issues)
