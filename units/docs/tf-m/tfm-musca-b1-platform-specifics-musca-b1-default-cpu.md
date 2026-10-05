---
id: "tfm-musca-b1-platform-specifics-musca-b1-default-cpu"
type: "concept"
domain: "security"
title: "Musca-B1 Platform Specifics: Musca B1 Default CPU"
summary: "Musca B1 is a dual core platform (being based on the SSE-200 subsystem), boot ROM code uses CPU0 running on 40.96MHz, while TF-M switches to CPU1 running on 163.84MHz."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/arm/musca_b1/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/arm/musca_b1/.html#musca-b1-default-cpu"
license: "BSD-3-Clause"
mode: "V"
---

Musca B1 is a dual core platform (being based on the [SSE-200 subsystem](https://developer.arm.com/documentation/101104/0200/introduction/about-the-sse-200)),
boot ROM code uses CPU0 running on 40.96MHz, while TF-M switches to CPU1 running on 163.84MHz.
An additional benefit to switching the default core is that CPU1 can access SRAM3
as Tightly Coupled Memory (TCM), while CPU0 can't.
When the core switch happens, CPU0 sleeps in a WFI loop to save power.

More information can be found in the following [patchset](https://review.trustedfirmware.org/c/TF-M/trusted-firmware-m/+/39616).

--------------

*Copyright (c) 2017-2025, Arm Limited. All rights reserved.*
