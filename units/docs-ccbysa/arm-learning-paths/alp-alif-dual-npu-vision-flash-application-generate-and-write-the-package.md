---
id: "alp-alif-dual-npu-vision-flash-application-generate-and-write-the-package"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Package and flash the application: Generate and write the package"
summary: "Close serial terminals connected to the board. Confirm that the boot switch is in the SE position, then run:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/flash-application.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/flash-application/#generate-and-write-the-package"
license: "CC-BY-SA-4.0"
mode: "V"
---

Close serial terminals connected to the board. Confirm that the boot switch is in the SE position, then run:

```bash
cd "$ALIF_SE_TOOLS_DIR"
./app-gen-toc -f build/config/dual-npu-vision.json
./app-write-mram -p
```

Wait until `app-write-mram` reports that the write completed. Don't reset or disconnect the board during this operation.
