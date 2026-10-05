---
id: "aig-install-guides-fvps-on-macos-how-do-i-expose-the-models-to"
type: "concept"
domain: "project"
title: "AVH FVPs on macOS: How do I expose the models to my local environment?"
summary: "Add $(pwd)/FVPs-on-Mac/bin to PATH environment:"
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/fvps-on-macos.md"
doc_source: "https://learn.arm.com/install-guides/fvps-on-macos/#how-do-i-expose-the-models-to-my-local-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

Add `$(pwd)/FVPs-on-Mac/bin` to `PATH` environment:

```sh
export PATH=$PATH:$(pwd)/FVPs-on-Mac/bin
```

Put this to your `~/.zshrc` to make it permanent.

For further information, refer to the [repository's README.md file](https://github.com/Arm-Examples/FVPs-on-Mac).
