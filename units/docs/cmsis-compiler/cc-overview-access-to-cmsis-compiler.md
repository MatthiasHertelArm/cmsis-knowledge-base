---
id: "cc-overview-access-to-cmsis-compiler"
type: "concept"
domain: "core"
title: "Overview: Access to CMSIS-Compiler"
summary: "CMSIS-View is actively maintained in CMSIS-Compiler GitHub repository and is released as a standalone CMSIS-Compiler pack in the CMSIS-Pack format."
status: "draft"
collection: "cmsis-compiler"
source: "ARM-software/CMSIS-Compiler@8cdaa0a:documentation/doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-Compiler/blob/8cdaa0a/documentation/doxygen/src/mainpage.md#access-to-cmsis-compiler"
license: "Apache-2.0"
mode: "V"
---

CMSIS-View is actively maintained in [**CMSIS-Compiler GitHub repository**](https://github.com/ARM-software/CMSIS-Compiler) and is released as a standalone [**CMSIS-Compiler pack**](https://www.keil.arm.com/packs/cmsis-compiler-arm/versions/) in the [CMSIS-Pack format](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html).

The table below explains the content of **ARM::CMSIS-Compiler** pack.

 Directory                             | Description
:--------------------------------------|:------------------------------------------------------
 📂 documentation                      | Folder with this CMSIS-Compiler documenation
 📂 example                            | rt_example
 📂 include                            | Header files with [**Retargeting functions**](https://github.com/ARM-software/CMSIS-Compiler/blob/8cdaa0a/documentation/doxygen/src/topics.html)
 📂 source                             | Compiler-specific implementations of regargeting functions
 📂 template                           | User Template files
 📄 ARM.CMSIS-Compiler.pdsc            | CMSIS-Pack description file
 📄 LICENSE                            | License Agreement (Apache 2.0)

See [CMSIS Documentation](https://arm-software.github.io/CMSIS_6/) for an overview of CMSIS software components, tools and specifications.
