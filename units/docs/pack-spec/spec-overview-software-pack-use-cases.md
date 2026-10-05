---
id: "spec-overview-software-pack-use-cases"
type: "concept"
domain: "pack"
title: "Overview: Software pack use cases"
summary: "All these pack types can contain in addition:"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/General.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/Overview.html"
license: "Apache-2.0"
mode: "V"
---

A software pack can be used to deliver:

- **Device** **support:** a so called _Device Family Pack (DFP)_ contains CMSIS system/startup files, drivers, and flash
  algorithms for a microcontroller device family.
- **Board** **support:** a _Board Support Pack (BSP)_ contains documentation, schematics, and drivers for a certain
  development board.
- **Software** **components:** a pure _software pack_ can contain source code, libraries, and documentation for:
  - **middleware** **stacks** for public availability.
  - **in-house** **software** for distribution within a company and/or engineering group.

All these pack types can contain in addition:

- example projects,
- code templates,
- reference applications.

As shown in the image below, a software pack can address multiple use cases at the same time! The
XML elements in the PDSC file determine the use case(s).
CMSIS
itself is distributed in various software packs (CORE, DSP library, RTOS implementation, etc.) and is supplied by Arm.

 "Major use cases of software packs"

The following sections provide more information:

 - In the cp_Packs, learn the basics and the required steps for creating a pack.
 - packFormat describes all XML elements that can be used in a package description file.
 - configWizard can be used to create GUI-like elements in development tools for configuration files.
 - flashAlgorithm algorithms are used to erase or download applications to Flash devices.
 - coresight_setup allows to create tool-agnostic debug and trace configurations.
 - sdf_pg describes all XML elements that can be used in a system description file for debugging.

**Note:**
The CMSIS-Toolbox documentation provides in-depth
documentation about how to create a CMSIS-Pack. It contains links to pack tutorial repos (for DFP, BSP, and generic software
packs) and provides useful tips when creating a pack.
