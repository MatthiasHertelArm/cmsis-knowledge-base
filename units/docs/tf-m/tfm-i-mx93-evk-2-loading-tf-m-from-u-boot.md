---
id: "tfm-i-mx93-evk-2-loading-tf-m-from-u-boot"
type: "concept"
domain: "security"
title: "i.MX93 EVK: 2. Loading TF-M from u-boot"
summary: ".. i.MX93 EVK on the official NXP product page : https://www.nxp.com/design/design-center/development-boards-and-designs/i.MX93EVK"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/nxp/mcimx93evk/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/nxp/mcimx93evk/.html#2-loading-tf-m-from-u-boot"
license: "BSD-3-Clause"
mode: "V"
---

#. Copy the compiled tfm binaries to the first FAT partition of the SD card and plug the SD card
   into the board.
#. Power it up and stop the u-boot execution at prompt.
#. Use U-Boot to load the TFM binaries to memory.
   The TFM secure binary should be loaded to TCM and non secure binary to OCRAM.
#. Kick the Cortx-M33 core to start from u-boot prompt.

* Boot with secure binary on TCM and non secure binary on OCRAM:

```console

fatload mmc 1 0x80000000 tfm_s.bin;
cp.b 0x80000000 0x201e0000 0x20000
fatload mmc 1 0x80020000 tfm_ns.bin;
cp.b 0x80020000 0x20480000 0x18000;
dcache flush;
bootaux 0x1ffe0000 0
```
* Boot with secure and non secure binary on TCM:

#. Total TCM available for code is only 128K on this platform.
#. To shift both secure and non secure binaries to TCM, the code sizes of both binaries should not
   be more than 128K.
#. To enable both partitions to be on TCM, compile with config option NS_PARTITION_ON_OCRAM turned
   off i.e -DNS_PARTITION_ON_OCRAM=OFF. By default the option is enabled in platform's config.cmake.
#. Default size chosen for Secure and Non secure partition when NS_PARTITION_ON_OCRAM is turned off
   is 96K (IMAGE_S_CODE_SIZE) and 32K(IMAGE_NS_CODE_SIZE). You can change the MACROS based on your
   usecase and binary sizes in platform/ext/target/nxp/mcimx93evk/parttion/flash_layout.in file.
   The sizes should be on 4K boundry.

```console

fatload mmc 1 0x80000000 tfm_s.bin
fatload mmc 1 0x80018000 tfm_ns.bin
cp.b 0x80000000 0x201e0000 0x20000;
bootaux 0x1ffe0000 0
```
.. _i.MX93 EVK on the official NXP product page : https://www.nxp.com/design/design-center/development-boards-and-designs/i.MX93EVK

--------------

*Copyright 2025 NXP*
*SPDX-License-Identifier: BSD-3-Clause*
