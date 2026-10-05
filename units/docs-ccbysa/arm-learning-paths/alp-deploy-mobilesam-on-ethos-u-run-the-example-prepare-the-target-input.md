---
id: "alp-deploy-mobilesam-on-ethos-u-run-the-example-prepare-the-target-input"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Build and run MobileSAM on the Corstone-320 FVP: Prepare the target input"
summary: "Copy the preprocessed image tensor into the directory used for target input and output. Remove any output from an earlier run so that validation uses a fresh result:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/run-the-example.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/run-the-example/#prepare-the-target-input"
license: "CC-BY-SA-4.0"
mode: "V"
---

Copy the preprocessed image tensor into the directory used for target input and output. Remove any output from an earlier run so that validation uses a fresh result:

```bash
mkdir -p arm_test/mobilesam/io
cp arm_test/mobilesam/export/input.bin arm_test/mobilesam/io/input.bin
rm -f arm_test/mobilesam/io/output-0.bin
```

The runner reads `input.bin` at runtime. The image is not compiled into the ELF.
