---
id: "intr-securing-firmware-updates-with-aes"
type: "concept"
domain: "debug"
title: "Securing Firmware Updates With AES Encryption"
summary: "Connected devices require a secure point-to-point channel to ensure that there is no possibility of exposing important data for the integrity of an embedded system."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-23-firmware-encryption-with-python.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-encryption-with-python"
license: "CC-BY-SA-4.0"
mode: "V"
---

Connected devices require a secure point-to-point channel to ensure that there is no possibility of exposing important data for the integrity of an embedded system. This is especially true when we talk about over-the-air (OTA) software updates, where the new firmware has a long way to go before reaching its destination and being installed by our bootloader.


In this publication, we will explore a simple method to encrypt the firmware using the AES algorithm, using open-source libraries in Python. Of course, we will also see how to decrypt the firmware from the MCU using the AES encryption engine.
