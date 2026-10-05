---
id: "tfm-bl1-immutable-bootloader-bl1-1-and-bl1-2-split-bootloaders"
type: "concept"
domain: "security"
title: "BL1 Immutable bootloader: BL1_1 and BL1_2 split bootloaders"
summary: "BL1 is split into two distinct boot stages, BL1_1 which is stored in ROM and BL1_2 which is stored in other non-volatile storage."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/bl1.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/bl1.html#bl1-1-and-bl1-2-split-bootloaders"
license: "BSD-3-Clause"
mode: "V"
---

BL1 is split into two distinct boot stages, BL1_1 which is stored in ROM and
BL1_2 which is stored in other non-volatile storage. This would usually be
either trusted or untrusted flash, but on platforms without flash memory can be
OTP. As BL1_2 is verified against a hash stored in OTP, it is immutable after
provisioning even if stored in mutable storage.

Bugs in ROM bootloaders usually cannot be fixed once a device is provisioned /
in the field, as ROM code is immutable the only option is fixing the bug in
newly manufactured devices.

However, it can be very expensive to change the ROM code of devices once
manufacturing has begun, as it requires changes to the photolithography masks
that are used to create the device. This cost varies depending on the complexity
of the device and of the process node that it is being fabricated on, but can be
large, both in engineering time and material/process costs.

By placing the majority of the immutable bootloader in other storage, we can
mitigate the costs associated with changing ROM code, as a new BL1_2 image can
be used at provisioning time with minimal changeover cost. BL1_1 contains a
minimal codebase responsible mainly for the verification of the BL1_2 image.

The bootflow is as follows. For simplicity this assumes that the boot stage
after BL1 is BL2, though this is not necessarily the case:

1) BL1_1 begins executing in place from ROM
2) BL1_1 copies BL1_2 into RAM
3) BL1_1 verifies BL1_2 against the hash stored in OTP
4) BL1_1 jumps to BL1_2, if the hash verification has succeeded
5) BL1_2 copies the primary BL2 image from flash into RAM
6) BL1_2 verifies the BL2 image using asymmetric cryptography
7) If verification fails, BL1_2 repeats 5 and 6 with the secondary BL2 image
8) BL1_2 jumps to BL2, if either image has successfully verified

The BL1_2 image is not encrypted, so if it is placed in untrusted flash it
will be possible to read the data in the image.
Some optimizations have been made specifically for the case where BL1_2 has been
stored in OTP:

OTP can be very expensive in terms of chip area, though new technologies like
antifuse OTP decrease this cost. Because of this, the code size of BL1_2 has
been minimized. Code-sharing has been configured so that BL1_2 can call
functions stored in ROM. Care should be taken that OTP is sized such that it is
possible to include versions of the functions used via code-sharing, in case the
ROM functions contain bugs, though less space is needed than if all code is
duplicated as it is assumed that most functions will not contain bugs.

As OTP memory frequently has low performance, BL1_2 is copied into RAM before it
it is executed. It also copies the next image stage into RAM before
authenticating it, which allows the next stage to be stored in untrusted flash.
This requires that the device have sufficient RAM to contain both the BL1_2
image and the next stage image at the same time. Note that this is done even if
BL1_2 is located in XIP-capable flash, as it both allows the use of untrusted
flash and simplifies the image upgrade logic.

BL1_2 enables TF-M to be used on devices that contain no secure flash, though
the ITS service will not be available. Other services that depend on ITS will
not be available without modification.
