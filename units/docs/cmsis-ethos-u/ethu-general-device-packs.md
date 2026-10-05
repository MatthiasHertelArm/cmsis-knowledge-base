---
id: "ethu-general-device-packs"
type: "concept"
domain: "edge-ai"
title: "General: Device packs"
summary: "A CMSIS Device Family Pack (DFP) can simplify integration by including Ethos-U resources such as the vela.ini configuration file, linker scripts, and software components. Device packs are available from www.keil.arm.com/packs."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/general/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/general/src/main.md#device-packs"
license: "Apache-2.0"
mode: "V"
---

A CMSIS Device Family Pack (DFP) can simplify integration by including Ethos-U
resources such as the `vela.ini` configuration file, linker scripts, and
software components. Device packs are available from
[www.keil.arm.com/packs](https://www.keil.arm.com/packs). CMSIS-Toolbox uses
these resources for the selected device and build context and exposes the
relevant parameters through its [MLOps information](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#mlops-information).
See Publish Ethos-U configuration in a DFP
for the relevant DFP description entries.

When a DFP contains Ethos-U resources, embedded application developers can use
the validated device-specific files directly. The silicon vendor is responsible
for supplying and validating the platform configuration. This includes the Vela
system configuration and supported memory modes, matching NPU access settings,
and the physical memory requirements. A platform maintainer can package and
integrate this configuration for a board or software environment. If a suitable
DFP is unavailable, this documentation also supports manual integration.
