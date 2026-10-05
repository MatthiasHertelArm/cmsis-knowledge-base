---
id: "alp-avh-balena-2setup-convert-the-download-to-an-avh"
type: "concept"
domain: "project"
title: "Deploy IoT applications with Balena Cloud and Arm Virtual Hardware: Prepare a custom Balena OS image: Convert the download to an AVH custom image"
summary: "When the download finishes, you can convert the Balena OS device image into a custom AVH image that you can upload to the AVH service and run on a Raspberry Pi 4 device."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_balena/2setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_balena/2setup/#convert-the-download-to-an-avh-custom-image"
license: "CC-BY-SA-4.0"
mode: "V"
---

When the download finishes, you can convert the Balena OS device image into a custom AVH image that you can upload to the AVH service and run on a Raspberry Pi 4 device. 

The conversion can be done using a Linux shell script. 

[Download the script](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_balena/mkbalenaosimg.sh) and save it as `mkbalenaosimg.sh` on your computer.

**Note:**
The conversion script requires a Linux environment with root access. If needed, copy the script and the Balena OS image .zip file to a Linux machine and log in to the machine. The `zip` and `unzip` commands are also required. Install them using your Linux package manager.


On a Linux machine, execute the script as root with the downloaded Balena OS image file as the only parameter:

```bash
bash ./mkbalenaosimg.sh balena-cloud-AVH-Testing-raspberrypi4-64-2.115.7+rev4-v14.11.2.img.zip
```

If successful, the conversion script creates a new file named `balenaos_rpi4b.zip` in the same directory. 

**Note:**
If needed, copy the `balenaos_rpi4b.zip` file back to your original machine. 


You are now ready to install Balena OS on a Raspberry Pi 4 in AVH.
