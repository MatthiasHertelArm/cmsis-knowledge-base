---
id: "mcuboot-signed-images-building-the-bootloader"
type: "concept"
domain: "boot-update"
title: "signed images: Building the bootloader"
summary: "Enable the BOOTUTIL_SIGN_RSA syscfg setting in your app or target syscfg.yml file"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/signed_images.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/signed_images.md#building-the-bootloader"
license: "Apache-2.0"
mode: "V"
---

Enable the BOOTUTIL_SIGN_RSA syscfg setting in your app or target syscfg.yml
file

    syscfg.vals:
        BOOTUTIL_SIGN_RSA: 1

After you've created the key package, you must include it in the build
for bootloader. So modify the pkg.yml for apps/boot to include it.

The syscfg variable to enable ECDSA256 is BOOTUTIL_SIGN_EC256.
