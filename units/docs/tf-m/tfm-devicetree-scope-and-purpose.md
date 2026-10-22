---
id: "tfm-devicetree-scope-and-purpose"
type: "concept"
domain: "security"
title: "Devicetree: Scope and purpose"
summary: "The Devicetree (DT), is a data structure and language for describing hardware (inter dependencies between devices)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/stm/stm32mp2/technical/devicetree.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/stm/stm32mp2/technical/devicetree.html#scope-and-purpose"
license: "BSD-3-Clause"
mode: "V"
---

The Devicetree (DT), is a data structure and language for describing
hardware (inter dependencies between devices). More specifically, it is a
hardware description that is readable by an operating system
so that the operating system doesn't need to hard code details of the machine.

For general devicetree information, documentation is available:

* Devicetree specification
* Devicetree usage
* Devicetree reference

Usually, the DT representation is created and passed to the kernel as a binary
blob (dtb). At runtime the kernel uses a library to parse this blob to look up
the hardware informations. Like this, a kernel can be independant
of hardware description and same kenel can be compatible with several boards, SoC...

However, this way has 2 disadvantages for small systems:

* Increase embedded image size, which integrate parsing library and the blob.
* Increase boot time: each device looks up its information from the blob

In 2016, Zephyr offered an alternative for small systems, which uses the advantage of
DT description whitout the need to parse a blob. This devicetree is based on this alternative.
