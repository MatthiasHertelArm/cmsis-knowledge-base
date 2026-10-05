---
id: "mcuboot-bootloader-downgrade-prevention"
type: "concept"
domain: "boot-update"
title: "Bootloader: Downgrade prevention"
summary: "Downgrade prevention is a feature which enforces that the new image must have a higher version/security counter number than the image it is replacing, thus preventing the malicious downgrading of the device to an older and possibly vulnerable …"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#downgrade-prevention"
license: "Apache-2.0"
mode: "V"
---

Downgrade prevention is a feature which enforces that the new image must have a
higher version/security counter number than the image it is replacing, thus
preventing the malicious downgrading of the device to an older and possibly
vulnerable version of its firmware.

### [Software-based downgrade prevention](#sw-downgrade-prevention)

During the software based downgrade prevention the image version numbers are
compared. This feature is enabled with the `MCUBOOT_DOWNGRADE_PREVENTION`
option. In this case downgrade prevention is only available when the
overwrite-based image update strategy is used (i.e. `MCUBOOT_OVERWRITE_ONLY`
is set).

### [Hardware-based downgrade prevention](#hw-downgrade-prevention)

Each signed image can contain a security counter in its protected TLV area, which
can be added to the image using the `-s` option of the [imgtool](https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/imgtool.md) script.
During the hardware based downgrade prevention (alias rollback protection) the
new image's security counter will be compared with the currently active security
counter value which must be stored in a non-volatile and trusted component of
the device. It is beneficial to handle this counter independently from image
version number:

  * It does not need to increase with each software release,
  * It makes it possible to do software downgrade to some extent: if the
    security counter has the same value in the older image then it is accepted.

It is an optional step of the image validation process and can be enabled with
the `MCUBOOT_HW_ROLLBACK_PROT` config option. When enabled, the target must
provide an implementation of the security counter interface defined in
`boot/bootutil/include/security_cnt.h`.
