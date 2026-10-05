---
id: "x-start-zephyr-project-2"
type: "pattern"
domain: "project"
title: "Zephyr virtual environment for cbuild with west integration"
status: "draft"
extracted_from: "proc-start-zephyr-project"
source: "project/start-zephyr-project/SKILL.md"
---

Before running `cbuild`, configure the verified Zephyr virtual environment in the current shell. Activate the virtual environment for an interactive shell; for non-interactive execution, prepend its executable directory to `PATH`. Confirm that `west` resolves from that virtual environment and stop when it does not. Apply this environment to both `cbuild` commands because `cbuild` invokes `west` as a subprocess.
