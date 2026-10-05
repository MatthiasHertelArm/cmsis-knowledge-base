---
id: "dsp-overview-access-to-cmsis-dsp"
type: "concept"
domain: "optimization"
title: "Overview: Access to CMSIS-DSP"
summary: "CMSIS-DSP is actively maintained in the CMSIS-DSP GitHub repository and is released as a standalone CMSIS-DSP pack in the CMSIS-Pack format."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/mainpage.md#access-to-cmsis-dsp"
license: "Apache-2.0"
mode: "V"
---

CMSIS-DSP is actively maintained in the [**CMSIS-DSP GitHub repository**](https://github.com/ARM-software/CMSIS-DSP) and is released as a standalone [**CMSIS-DSP pack**](https://www.keil.arm.com/packs/cmsis-dsp-arm/versions/) in the [CMSIS-Pack format](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html).

The table below explains the content of **ARM::CMSIS-DSP** pack.

 Directory                             | Description
:--------------------------------------|:------------------------------------------------------
 📂 ComputeLibrary                     | Small Neon kernels when building on Cortex-A
 📂 Documentation                      | Folder with this CMSIS-DSP documentation
 📂 Example                            | Example projects demonstrating the usage of the library functions
 📂 Include                            | Include files for using and building the lib
 📂 PrivateInclude                     | Private include files for building the lib
 📂 Source                             | Source files
 📄 ARM.CMSIS-DSP.pdsc                 | CMSIS-Pack description file
 📄 LICENSE                            | License Agreement (Apache 2.0)

See [CMSIS Documentation](https://arm-software.github.io/CMSIS_6/) for an overview of CMSIS software components, tools and specifications.
