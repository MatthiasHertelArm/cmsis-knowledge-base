---
id: "alp-alif-image-classification-create-project-duplicate-the-blinky-project"
type: "concept"
domain: "edge-ai"
title: "create project: Duplicate the Blinky project"
summary: "Start by copying the working Blinky project as a template:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/create-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/create-project/#duplicate-the-blinky-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

Start by copying the working Blinky project as a template:

```bash
cd ~/alif/alif_vscode-template
cp -R blinky/ mv2_runner
```

Rename the project file inside the new directory:

```bash
mv mv2_runner/blinky.cproject.yml mv2_runner/mv2_runner.cproject.yml
```

Replace all internal references from `blinky` to `mv2_runner`:

```bash
perl -pi -e 's/\bblinky\b/mv2_runner/g' $(grep -RIl "blinky" mv2_runner)
```
