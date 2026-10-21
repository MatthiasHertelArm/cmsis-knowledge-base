---
id: "x-fvp-debug-setup-5"
type: "concept"
domain: "debug"
title: "How the CMSIS Solution extension regenerates CMSIS tasks and launch configurations"
status: "draft"
extracted_from: "proc-fvp-debug-setup"
source: "fvp-debug-setup/SKILL.md"
license: "Apache-2.0"
---

On regeneration the extension rewrites every `CMSIS *` task and every launch config carrying `"cmsis": {"updateConfiguration": "auto"}`, and *removes* auto configs that are not in the generated set. `"manual"` survives both. Regeneration also fires on a plain file-watch of the csolution yml — useful for testing: `touch <name>.csolution.yml`, wait, re-read `.vscode/launch.json`.
