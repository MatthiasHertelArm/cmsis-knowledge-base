---
id: "alp-alif-dual-npu-vision-flash-application-boot-the-application"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Package and flash the application: Boot the application"
summary: "Move the switch from SE to U4. Open the U4 serial port at 115200 baud, 8 data bits, no parity, and 1 stop bit. Reset the board."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/flash-application.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/flash-application/#boot-the-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

Move the switch from SE to U4. Open the U4 serial port at 115200 baud, 8 data bits, no parity, and 1 stop bit. Reset the board.

The secure-enclave log shows entries for `HP_APP` and `U85MOD`. The U4 log starts with the Zephyr boot banner and the application name:

```output
*** dual ExecuTorch parallel SSD(U55) + MobileNetV2(U85) ***
```
