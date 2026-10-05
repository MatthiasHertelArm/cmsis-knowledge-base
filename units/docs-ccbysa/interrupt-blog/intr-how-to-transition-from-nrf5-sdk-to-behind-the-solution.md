---
id: "intr-how-to-transition-from-nrf5-sdk-to-behind-the-solution"
type: "concept"
domain: "debug"
title: "How to Transition from nRF5 SDK to Zephyr NCS － Lessons from Ultrahuman’s Journey: Behind the Solution"
summary: "We followed the path to change the older bootloader so that it could accommodate the new image from Zephyr NCS."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-12-11-upgrading-from-nrf5-sdk-to-ncs.md"
doc_source: "https://interrupt.memfault.com/blog/upgrading-from-nrf5-sdk-to-ncs#behind-the-solution"
license: "CC-BY-SA-4.0"
mode: "V"
---

We followed the path to change the older bootloader so that it could accommodate
the new image from Zephyr NCS.

The process works like this:

1. Perform a Device Firmware Update (DFU) of an nRF5 SDK bootloader to remove
   protection on the MBR and bootloader regions.

1. Create an NCS image that matches the memory layout of the older image,
   ensuring proper alignment to properly transfer the image with the older ones.

1. Sign the NCS image using the same private and public key as the nRF SDK
   image.
