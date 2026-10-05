---
id: "alp-alif-dual-npu-vision-prepare-workspace-connect-the-target-hardware"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Prepare the board and workspace: Connect the target hardware"
summary: "Power off the E8 DevKit before changing camera or display connections. Then, to connect the hardware:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/prepare-workspace.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/prepare-workspace/#connect-the-target-hardware"
license: "CC-BY-SA-4.0"
mode: "V"
---

Power off the E8 DevKit before changing camera or display connections. Then, to connect the hardware:

1. Connect the MT9M114 camera module to the bottom-side J16 connector.
2. Connect the MW405 display to the display connector.
3. Connect the board's USB ports for power, SE UART, and U4 UART.
4. Confirm that the board runs SEROM 1.105.65 and SERAM 1.110.0.
5. Move the boot switch to the SE position before flashing.

**Note:**
- The supplied overlay targets the J16 selfie-camera connection. J22 uses a different I2C address and device-tree route. Don't combine a J16 overlay with a camera connected to J22.
- If the camera reports chip ID `0000` or I2C error `-5`, power off the board and check the camera connection. The supplied overlay expects the MT9M114 on J16 at the selfie-camera I2C address. Reseat the flex cable and confirm that its contacts face the correct direction.
