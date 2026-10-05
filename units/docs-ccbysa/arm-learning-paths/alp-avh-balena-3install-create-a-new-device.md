---
id: "alp-avh-balena-3install-create-a-new-device"
type: "concept"
domain: "project"
title: "Deploy IoT applications with Balena Cloud and Arm Virtual Hardware: Install Balena OS on AVH: Create a new device"
summary: "To create a new device, you need a user account for Arm Virtual Hardware (AVH). If you don't have an account, you can create one using the Create an Arm account link below the LOGIN button."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_balena/3install.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_balena/3install/#create-a-new-device"
license: "CC-BY-SA-4.0"
mode: "V"
---

To create a new device, you need a user account for [Arm Virtual Hardware (AVH)](https://app.avh.arm.com/). If you don't have an account, you can create one using the `Create an Arm account` link below the `LOGIN` button. If you create a new account, you'll be automatically enrolled in a free 30-day trial. 

From the AVH dashboard, click on the `Create Device` button. Select Raspberry Pi 4 from the list of devices.

On the next screen you'll be asked to configure your device by choosing the firmware to use.

Use the `Upload your own firmwware` on the right side to drag or browse for the file  `balenaos_rpi4b.zip`.

(figure: AVH firmware upload screen showing drag-and-drop area for uploading custom firmware file with Raspberry Pi 4 device selected#center)

Uploading the file takes some time.

After the file is uploaded, click `NEXT`.

The final step is to name the AVH device. Select your own name or use `balena-testing-device`.

You don't need to set any advanced boot options.

Wait for the device to be created. It's ready to use when you see the ready message:

(figure: AVH console showing device status message indicating the Raspberry Pi 4 virtual device is ready and displaying boot completion logs#center)
