---
id: "alp-deploy-mobilesam-on-ethos-u-export-the-model-prepare-the-mobilesam-source-a"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Export MobileSAM for Ethos-U85: Prepare the MobileSAM source and checkpoint"
summary: "Run all commands from the ExecuTorch repository root. Confirm that your Python environment is active and that you've sourced the Arm tools' setup_path.sh file in the current shell, as shown during environment setup."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/export-the-model.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/export-the-model/#prepare-the-mobilesam-source-and-checkpoint"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run all commands from the ExecuTorch repository root. Confirm that your Python environment is active and that you've sourced the Arm tools' `setup_path.sh` file in the current shell, as shown during environment setup.

Prepare the pinned MobileSAM source and checkpoint:

```bash
python3 examples/arm/mobilesam_prompt_segmentation_example_ethos_u/model_export/prepare_mobilesam.py
```

The script downloads the [pinned MobileSAM revision](https://github.com/ChaoningZhang/MobileSAM/tree/f706ad9c4eb7f219c00d9050e46328518ffb65d2), applies the patch needed for a configurable image size, and verifies the checkpoint's SHA-256 checksum. It stores the source in `source/` and the checkpoint in `mobile_sam.pt`, outside the ExecuTorch repository. The cache directory is:

```text
~/.cache/executorch/mobilesam/f706ad9c4eb7f219c00d9050e46328518ffb65d2/
```
