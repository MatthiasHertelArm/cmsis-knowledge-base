---
id: "alp-deploy-mobilesam-on-ethos-u-prepare-the-environment-clone-the-executorch-source"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Prepare the ExecuTorch and Arm environment: Clone the ExecuTorch source"
summary: "Clone ExecuTorch, select the revision used by this Learning Path, and initialize its submodules:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/prepare-the-environment.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/prepare-the-environment/#clone-the-executorch-source"
license: "CC-BY-SA-4.0"
mode: "V"
---

Clone ExecuTorch, select the revision used by this Learning Path, and initialize its submodules:

```bash
git clone https://github.com/pytorch/executorch.git
cd executorch
git checkout 5c4d2c4a0150a0809bc77be9a67093f80f60a60f
git submodule sync
git submodule update --init --recursive
```

Run the remaining commands from the ExecuTorch repository root. The pinned revision keeps the commands aligned with the [MobileSAM example source](https://github.com/pytorch/executorch/tree/5c4d2c4a0150a0809bc77be9a67093f80f60a60f/examples/arm/mobilesam_prompt_segmentation_example_ethos_u).
