---
id: "zep-soc-porting-guide-soc-definitions"
type: "concept"
domain: "bring-up"
title: "SoC Porting Guide: SoC Definitions"
summary: "It is expected that you are familiar with the board concept in Zephyr. A high level overview of the hardware support hierarchy and terms used in the Zephyr documentation can be seen in hw_support_hierarchy."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/soc_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/soc_porting.rst"
license: "Apache-2.0"
mode: "V"
---

It is expected that you are familiar with the board concept in Zephyr.
A high level overview of the hardware support hierarchy and terms used in the
Zephyr documentation can be seen in hw_support_hierarchy.

For SoC porting, the most important terms are:

- SoC: the exact system on a chip the board's CPU is part of.
- SoC series: a group of tightly related SoCs.
- SoC family: a wider group of SoCs with similar characteristics.
- CPU cluster: a cluster of one or more CPU cores.
- CPU core: a particular CPU instance of a given architecture.
- Architecture: an instruction set architecture.


### Architecture


See architecture_porting_guide.
