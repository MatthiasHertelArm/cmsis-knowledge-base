---
id: "alp-yolo-on-himax-build-firmware-clone-the-himax-github-project"
type: "concept"
domain: "edge-ai"
title: "Run a computer vision model on a Himax microcontroller: Build the firmware: Clone the Himax GitHub project"
summary: "Himax maintains a repository containing a few examples that can be used with the Seeed Grove Vision AI V2 board."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/yolo-on-himax/build-firmware.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/yolo-on-himax/build-firmware/#clone-the-himax-github-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

Himax maintains a repository containing a few examples that can be used with the Seeed Grove Vision AI V2 board. 

It contains third-party software and scripts to build and flash the image with the object detection application. By recursively cloning the Himax examples repository, git includes the necessary subrepositories that have been configured for the project.

Clone the repository:

```bash
git clone --recursive https://github.com/HimaxWiseEyePlus/Seeed_Grove_Vision_AI_Module_V2.git
cd Seeed_Grove_Vision_AI_Module_V2
```
