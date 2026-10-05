---
id: "core-overview-access-to-cmsis-core-cortex-m"
type: "concept"
domain: "core"
title: "Overview: Access to CMSIS-Core (Cortex-M)"
summary: "CMSIS-Core is actively maintained in the CMSIS 6 GitHub repository and released as part of the CMSIS Software Pack."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/mainpage.md#access-to-cmsis-core-cortex-m"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Core is actively maintained in the [**CMSIS 6 GitHub repository**](https://github.com/ARM-software/CMSIS_6) and released as part of the [**CMSIS Software Pack**](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/../General/cmsis_pack.html).

The following directories and files relevant to CMSIS-Core (Cortex-M) are present in the **ARM::CMSIS** Pack:

Directory                         | Content
:---------------------------------|:------------------------------------------------------------------------
📂 CMSIS                          | CMSIS Base software components folder
 ┣ 📂 Documentation/html/Core     | A local copy of this CMSIS-Core (M) documentation
 ┗ 📂 Core                        | CMSIS-Core files
 &emsp;  ┣ 📂 Include        | cmsis_processor_files.
 &emsp;&emsp;  ┗ 📂 m-profile| Header files specific for Arm M-Profile.
 See cmsis_compiler_files and cmsis_feature_files.
 &emsp;  ┗ 📂 Template       | cmsis_template_files
