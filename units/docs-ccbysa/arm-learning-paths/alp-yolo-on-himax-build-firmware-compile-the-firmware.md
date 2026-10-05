---
id: "alp-yolo-on-himax-build-firmware-compile-the-firmware"
type: "concept"
domain: "edge-ai"
title: "Run a computer vision model on a Himax microcontroller: Build the firmware: Compile the firmware"
summary: "Use Make to compile the source code for object detection."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/yolo-on-himax/build-firmware.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/yolo-on-himax/build-firmware/#compile-the-firmware"
license: "CC-BY-SA-4.0"
mode: "V"
---

Use Make to compile the source code for object detection. 

This can take up to 10 minutes depending on the number of CPU cores available on your host machine. 

```bash
cd EPII_CM55M_APP_S
make
```

When the build is complete, you will have an `.elf` file at `obj_epii_evb_icv30_bdv10/gnu_epii_evb_WLCSP65/EPII_CM55M_gnu_epii_evb_WLCSP65_s.elf`
