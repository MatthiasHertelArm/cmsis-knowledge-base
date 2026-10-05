---
id: "core-cmsis-core-files-cmsis-core-standard-files"
type: "concept"
domain: "core"
title: "CMSIS-Core Files: CMSIS-Core Standard Files"
summary: "The CMSIS-Core Standard file implement all attributes specific to Arm processor cores and generally do not need any modifications."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/core_std_files.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/core_std_files.md#cmsis-core-standard-files"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Core Standard file implement all attributes specific to Arm processor cores and generally do not need any modifications.

The files are provided by Arm as CMSIS-Core software component that is part of the [CMSIS Software pack](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/../General/cmsis_pack.html). The CMSIS-Core standard files can be split into following categories explained below:

 - cmsis_processor_files
 - cmsis_compiler_files
 - cmsis_feature_files

### CMSIS-Core Processor Files

The CMSIS-Core processor files define the core peripherals and provide helper functions for their access.

The files have naming convention `core_<cpu>.h`, with one file available for each supported processor `<cpu>` as listed in the table below.

Header File            | Target Processor Core
:----------------------|:-------------------------------
📂 CMSIS/Core/Include  | CMSIS-Core include folder ([See on GitHub](https://github.com/ARM-software/CMSIS_6/tree/main/CMSIS/Core/Include/))
 ┣ 📄 core_cm0.h       | Cortex-M0 processor
 ┣ 📄 core_cm0plus.h   | Cortex-M0+ processor
 ┣ 📄 core_cm1.h       | Cortex-M1 processor
 ┣ 📄 core_cm3.h       | Cortex-M3 processor
 ┣ 📄 core_cm4.h       | Cortex-M4 processor
 ┣ 📄 core_cm7.h       | Cortex-M7 processor
 ┣ 📄 core_cm23.h      | Cortex-M23 processor
 ┣ 📄 core_cm33.h      | Cortex-M33 processor
 ┣ 📄 core_cm35p.h     | Cortex-M35P processor
 ┣ 📄 core_cm52.h      | Cortex-M52 processor
 ┣ 📄 core_cm55.h      | Cortex-M55 processor
 ┣ 📄 core_cm85.h      | Cortex-M85 processor
 ┣ 📄 core_starmc1.h   | STAR-MC1 processor
 ┣ 📄 core_sc000.h     | SC000 processor
 ┗ 📄 core_sc300.h     | SC300 processor

The files also include the cmsis_compiler_files and depending on the features supported by the core also correponding cmsis_feature_files.

### CMSIS-Core Compiler Files

The CMSIS-Core compiler files provide consistent implementations of `#define` symbols that allow toolchain-agnostic usage of CMSIS-Core. cmsis_processor_files rely on such toolchain-agnostic abstractions by including `cmsis_compiler.h` file that then selects the target compiler-specific implementatation depending on the toolchain used in the project.

CMSIS-Core compiler files are provided in `CMSIS/Core/Include/` directory, and define the supported compilers as listed in tested_tools_sec. compiler_conntrol_gr documents the functionalities provided by the CMSIS compliant toolchains.

Header File                            | Description
:--------------------------------------|:-------------------
📂 CMSIS/Core/Include    | CMSIS-Core include folder ([See on GitHub](https://github.com/ARM-software/CMSIS_6/tree/main/CMSIS/Core/Include/))
 ┣ 📄 cmsis_compiler.h                  | Main CMSIS-Core compiler header file
 ┗ 📂 m-profile                         | Directory for M-Profile specific files
 &emsp;  ┣ 📄 cmsis_armclang_m.h   | CMSIS-Core Arm Clang compiler file for Cortex-M
 &emsp;  ┣ 📄 cmsis_clang_m.h      | CMSIS-Core Clang compiler file for Cortex-M
 &emsp;  ┣ 📄 cmsis_gcc_m.h        | CMSIS-Core GCC compiler file for Cortex-M
 &emsp;  ┣ 📄 cmsis_iccarm_m.h     | CMSIS-Core IAR compiler file for Cortex-M
 &emsp;  ┗ 📄 cmsis_tiarmclang_m.h | CMSIS-Core TI Clang compiler file

### CMSIS-Core Architecture Feature Files

Several architecture-specific features are implemented in separate header files that then gets included by cmsis_processor_files if corresponding feature is supported. 

For Cortex-M cores following architecture feature files are provided in the `CMSIS/Core/Include/m-profile/` folder:

Header File         | Feature
:-------------------|:-------------------
📂 CMSIS/Core/Include    | CMSIS-Core include folder ([See on GitHub](https://github.com/ARM-software/CMSIS_6/tree/main/CMSIS/Core/Include/))
 ┣ 📂 m-profile                    | Directory for M-Profile specific files
 &emsp;  ┣ 📄 armv7m_cache1.h | cache_functions_m7
 &emsp;  ┣ 📄 armv7m_mpu.h    | mpu_functions
 &emsp;  ┣ 📄 armv8m_mpu.h    | mpu8_functions
 &emsp;  ┣ 📄 armv8m_pmu.h    | pmu8_functions
 &emsp;  ┗ 📄 armv81m_pac.h   | PAC functions
 ┗ 📄 tz_context.h                 | API header file for context_trustzone_functions

### CMSIS Version and Processor Information

__CM_CMSIS_VERSION is defined in the `cmsis_version.h` file and provides the version of the CMSIS-Core (Cortex-M). It is constructed as follows:

```c
#define __CM_CMSIS_VERSION_MAIN  ( 5U)                                    /* [31:16] CMSIS Core(M) main version */
#define __CM_CMSIS_VERSION_SUB   ( 7U)                                    /* [15:0]  CMSIS Core(M) sub version */
#define __CM_CMSIS_VERSION       ((__CM_CMSIS_VERSION_MAIN << 16U) | \
                                   __CM_CMSIS_VERSION_SUB           )     /* CMSIS Core(M) version number */

```

The `cmsis_version.h` is included by each `cpu_<core>.h` so the CMSIS version defines are available via them already.

The `cpu_<core>.h` files use specific defines (such as __CORTEX_M) that provide identification of the target processor core.

These defines can be used in the device_h_pg to verify a minimum CMSIS-Core version as well as the target processor. Read more at version_control_gr.
