---
id: "rtx-mainpage-access-to-cmsis-rtx"
type: "concept"
domain: "rtos"
title: "mainpage: Access to CMSIS-RTX"
summary: "CMSIS-RTX kernel is actively maintained in CMSIS-RTX GitHub repository and is also provided as a standalone CMSIS-RTX pack in the CMSIS-Pack format."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/mainpage.md#access-to-cmsis-rtx"
license: "Apache-2.0"
mode: "V"
---

CMSIS-RTX kernel is actively maintained in [**CMSIS-RTX GitHub repository**](https://github.com/ARM-software/CMSIS-RTX) and is also provided as a standalone [**CMSIS-RTX pack**](https://www.keil.arm.com/packs/cmsis-rtx-arm/versions/) in the [CMSIS-Pack format](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html).

> **Note**
>
> - CMSIS-RTX replaces and extends RTX5 implementation previously provided as part of *ARM::CMSIS* pack.
> - See [Migrating projects from CMSIS v5 to CMSIS v6](https://learn.arm.com/learning-paths/microcontrollers/project-migration-cmsis-v6) for a guidance on updating existing projects to CMSIS-RTX.

The table below explains the content of the **ARM::CMSIS-RTX** Pack.

 File/Directory        | Content
:----------------------|:---------------------------------------------------------
 📂 Config             | RTX configuration files **RTX_Config.h** and **RTX_Config.c**
 📂 Documentation      | A local copy of this documentation
 📂 Examples           | Example projects (MDK uVision and CMSIS-Toolbox)
 📂 Include            | Public header files of RTX software component
 📂 Library            | Library project files and pre-built libraries
 📂 Source             | Private header and source files of RTX software component
 📂 Template           | User code templates for creating application projects with CMSIS-RTX
 📄 ARM.CMSIS-RTX.pdsc | Pack description file in CMSIS-Pack format
 📄 LICENSE            | License Agreement (Apache 2.0)
 📄 RTX5.scvd          | SCVD file for RTOS-aware debugging with [Component Viewer and Event Recorder](https://arm-software.github.io/CMSIS-View/latest/index.html)

See [CMSIS Documentation](https://arm-software.github.io/CMSIS_6/) for an overview of CMSIS software components, tools and specifications.
