---
id: "intr-how-to-transition-from-nrf5-sdk-to-4-creating-ncs-image-and-dfu"
type: "concept"
domain: "debug"
title: "How to Transition from nRF5 SDK to Zephyr NCS － Lessons from Ultrahuman’s Journey: Behind the Solution / 4\\. Creating NCS Image and DFU"
summary: "Create an NCS image using DFUbatch script, replacing the SoftDevice with the application and the bootloader with MCUboot:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-12-11-upgrading-from-nrf5-sdk-to-ncs.md"
doc_source: "https://interrupt.memfault.com/blog/upgrading-from-nrf5-sdk-to-ncs#4-creating-ncs-image-and-dfu"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Behind the Solution_

Create an NCS image using DFUbatch script, replacing the SoftDevice with the
application and the bootloader with MCUboot:

```bash
BOOTLOADER_HEX=../build/mcuboot/zephyr/zephyr.hex
APPLICATION_HEX=../build/zephyr/app_signed.hex

nrfutil pkg generate --hw-version 52 \
--bootloader-version 102 \
--sd-req 0x123
--softdevice ${APPLICATION_HEX} \
--bootloader ${BOOTLOADER_HEX} \
--key-file ../child_image/mcuboot/boards/key/my_key.pem migration_dfu_test.zip
```

Use the nRFConnect application to DFU the new image, and it will be successfully
applied, allowing the NCS image to advertise.
