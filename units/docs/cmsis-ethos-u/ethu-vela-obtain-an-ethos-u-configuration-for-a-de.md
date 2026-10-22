---
id: "ethu-vela-obtain-an-ethos-u-configuration-for-a-de"
type: "concept"
domain: "edge-ai"
title: "Vela: Obtain an Ethos-U configuration for a device"
summary: "The Vela compiler requires the selected Ethos-U variant and MAC configuration, plus a vela.ini configuration file. The vela.ini file contains System_Config sections that model device memory performance and Memory_Mode sections that define where model data is placed."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/vela/src/main.md#obtain-an-ethos-u-configuration-for-a-device"
license: "Apache-2.0"
mode: "V"
---

The Vela compiler requires the selected Ethos-U variant and MAC configuration,
plus a `vela.ini` configuration file. The `vela.ini` file contains `System_Config`
sections that model device memory performance and `Memory_Mode` sections that define 
where model data is placed.

For an Edge AI MCU, a Device Family Pack (DFP), available from
[www.keil.arm.com/packs](https://www.keil.arm.com/packs), can provide the Ethos-U
configuration information, including the device-specific `vela.ini` file.
CMSIS-Toolbox exports these resources for the selected device and build context
through its
[MLOps information](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#mlops-information).

When the DFP does not provide this information, create the equivalent configuration
manually as described in Create device-specific `vela.ini` file.
