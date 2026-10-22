---
id: "mcuboot-bootloader-equal-slots-direct-xip"
type: "concept"
domain: "boot-update"
title: "Bootloader: Image slots / Equal slots (direct-xip)"
summary: "When the direct-xip mode is enabled the active image flag is \"moved\" between the slots during image upgrade and in contrast to the above, the bootloader can run an image directly from either the primary or the secondary …"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/design.md#equal-slots-direct-xip"
license: "Apache-2.0"
mode: "V"
---

_Part of: Image slots_

When the direct-xip mode is enabled the active image flag is "moved" between the
slots during image upgrade and in contrast to the above, the bootloader can
run an image directly from either the primary or the secondary slot (without
having to move/copy it into the primary slot). Therefore the image update
client, which downloads the new images must be aware, which slot contains the
active image and which acts as a staging area and it is responsible for loading
the proper images into the proper slot. All this requires that the images be
built to be executed from the corresponding slot. At boot time the bootloader
first looks for images in the slots and then inspects the version numbers in the
image headers. It selects the newest image (with the highest version number) and
then checks its validity (integrity check, signature verification etc.). If the
image is invalid MCUboot erases its memory slot and starts to validate the other
image. After a successful validation of the selected image the bootloader
chain-loads it.

An additional "revert" mechanism is also supported. For more information, please
read the [corresponding section](#direct-xip-ram-load-revert).
Handling the primary and secondary slots as equals has its drawbacks. Since the
images are not moved between the slots, the on-the-fly image
encryption/decryption can't be supported (it only applies to storing the image
in an external flash on the device, the transport of encrypted image data is
still feasible).

The overwrite and the direct-xip upgrade strategies are substantially simpler to
implement than the image swapping strategy, especially since the bootloader must
work properly even when it is reset during the middle of an image swap. For this
reason, the rest of the document describes its behavior when configured to swap
images during an upgrade.
