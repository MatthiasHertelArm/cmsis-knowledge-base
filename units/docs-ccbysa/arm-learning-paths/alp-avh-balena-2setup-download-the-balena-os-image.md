---
id: "alp-avh-balena-2setup-download-the-balena-os-image"
type: "concept"
domain: "project"
title: "Deploy IoT applications with Balena Cloud and Arm Virtual Hardware: Prepare a custom Balena OS image: Download the Balena OS image"
summary: "Add a device to your fleet. Navigate to the Devices section of your fleet and click on the Add Device button. This opens a dialog to create a custom device image."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_balena/2setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_balena/2setup/#download-the-balena-os-image"
license: "CC-BY-SA-4.0"
mode: "V"
---

Add a device to your fleet. Navigate to the `Devices` section of your fleet and click on the `Add Device` button. This opens a dialog to create a custom device image.

(figure: Dialog window showing device configuration options including device type selection, edition settings, and network configuration for creating a custom Balena OS image#center)

You can use the Raspberry Pi 4 device on Arm Virtual Hardware (AVH) as the new device.

Select `Raspberry Pi 4 (using 64-bit OS)` as the device type.

Select `Development` for the edition. 

Leave the default values for everything else.

Download the image by clicking on the drop-down arrow on the right side of the `Flash` button and select `Download balenaOS`.

**Note:**
There's no need to install Balena Etcher, the tool used to write SD cards.


The file is large so the download may take some time.
