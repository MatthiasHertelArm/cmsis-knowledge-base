---
id: "tfm-numaker-pfm-m2354-flashing-image-with-nuvoton-nulink-tool"
type: "concept"
domain: "security"
title: "NuMaker-PFM-M2354: Flashing Image with Nuvoton NuLink Tool"
summary: "NuMaker-PFM-M2354 board supports on board ICE called NuLink. Connect NuLink to PC with USB cable and using NuLink Command Tool to flashing the image."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/nuvoton/m2354/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/nuvoton/m2354/.html#flashing-image-with-nuvoton-nulink-tool"
license: "BSD-3-Clause"
mode: "V"
---

NuMaker-PFM-M2354 board supports on board ICE called NuLink.
Connect NuLink to PC with USB cable and using
[NuLink Command Tool](https://github.com/OpenNuvoton/Nuvoton_Tools)
to flashing the image.

The commands are as follows:

```doscon

> NuLink_M2354 -C
> NuLink_M2354 -E ALL
> NuLink_M2354 -W NSCBA 0x80000 0
> NuLink_M2354 -S
> NuLink_M2354 -C
> NuLink_M2354 -W APROM .\build_spe\bin\bl2.bin 0
> NuLink_M2354 -W APROM .\build_spe\bin\tfm_s_signed.bin 0 0x20000 0
> NuLink_M2354 -W APROMNS .\build_test\bin\tfm_ns_signed.bin 0
```
--------------

*Copyright (c) 2021-2023, Nuvoton Technology Corp. All rights reserved.*
