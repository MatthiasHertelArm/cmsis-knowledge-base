---
id: "tfm-rp2350-erasing-the-flash"
type: "concept"
domain: "security"
title: "RP2350: Erasing the flash"
summary: "Generating flash sized image of zeros can be done with the truncate command, then it can be converted to the uf2 format with the uf2conv.py utility. The resulting uf2 file then needs to be copied to the board."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/rpi/rp2350/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/rpi/rp2350/.html#erasing-the-flash"
license: "BSD-3-Clause"
mode: "V"
---

Generating flash sized image of zeros can be done with the truncate command,
then it can be converted to the ``uf2` format with the `uf2conv.py` utility. The
resulting `uf2` file then needs to be copied to the board. Current platform flash
size is 2 MB, please adjust size based on your board specs, i.e. `PICO_FLASH_SIZE_BYTES`:

```bash

truncate -s 2M nullbytes2M.bin
uf2conv.py nullbytes2M.bin --base 0x10000000 --convert --output nullbytes2M.uf2 --family 0xe48bff59
```
-------------

 *SPDX-License-Identifier: BSD-3-Clause*

 *SPDX-FileCopyrightText: Copyright The TrustedFirmware-M Contributors*
