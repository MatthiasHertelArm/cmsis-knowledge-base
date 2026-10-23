---
id: "core-cmsis-sw-pack-cmsis-software-pack"
type: "concept"
domain: "core"
title: "cmsis sw pack: CMSIS Software Pack"
summary: "The CMSIS Base Components are actively maintained in the CMSIS 6 GitHub repository and are released together in the CMSIS pack that follows the Open-CMSIS-Pack format."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/General/src/cmsis_sw_pack.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/General/src/cmsis_sw_pack.md#cmsis-software-pack"
license: "Apache-2.0"
mode: "V"
---

The **CMSIS Base Components** are actively maintained in the [**CMSIS 6 GitHub repository**](https://github.com/ARM-software/CMSIS_6) and are released together in the [**CMSIS pack**](https://www.keil.arm.com/packs/cmsis-arm/) that follows the [Open-CMSIS-Pack format](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html).

The table below shows the high-level structure of the **ARM::CMSIS** pack. Details about component folders can be found in the referenced component documentations.

File/Directory        | Content
:---------------------|:-------------------
📂 CMSIS               | CMSIS Base software components folder
   ┣ 📂 Core           | Processor files for the [CMSIS-Core (Cortex-M)](https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/General/src/../Core/index.html)
   ┣ 📂 Core_A         | Processor files for the [CMSIS-Core (Cortex-A)](https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/General/src/../Core_A/index.html)
   ┣ 📂 Documentation  | A local copy of this documentation
   ┣ 📂 Driver         | API header files and template implementations for the [CMSIS-Driver](https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/General/src/../Driver/index.html)
   ┗ 📂 RTOS2          | API header files and OS tick implementations for the [CMSIS-RTOS2](https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/General/src/../RTOS2/index.html)
📄 ARM.CMSIS.pdsc      | Package description file in CMSIS-Pack format
📄 LICENSE             | CMSIS License Agreement (Apache 2.0)

Section cmsis_components provides links to CMSIS packs and repositories of other CMSIS components that are delivered separately and are not part of ARM::CMSIS pack.
