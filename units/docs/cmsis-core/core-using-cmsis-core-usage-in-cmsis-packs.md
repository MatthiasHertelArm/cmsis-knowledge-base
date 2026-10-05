---
id: "core-using-cmsis-core-usage-in-cmsis-packs"
type: "concept"
domain: "core"
title: "Using CMSIS-Core: Usage in CMSIS-Packs"
summary: "The easiest way to use CMSIS-Core in a project is with CMSIS Packs."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/using.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/using.md#usage-in-cmsis-packs"
license: "Apache-2.0"
mode: "V"
---

The easiest way to use CMSIS-Core in a project is with CMSIS Packs.

The cmsis_device_files are typically provided in a [CMSIS Device Family Pack (DFP)](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/cp_PackTutorial.html#createPack_DFP) that is maintained by the chip vendor for the target device family. The list of public CMSIS packs (including DFPs) can be found at [keil.arm.com/packs](https://www.keil.arm.com/packs/).

A Device Family Pack (DFP) usually has a requirement for using the **CMSIS:CORE** component from the [CMSIS Software pack](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/../General/cmsis_pack.html) that contains the cmsis_standard_files. In such case the CMSIS Software pack needs to be installed as well.

The files startup_c_pg and system_c_pg are typically provided in the DFP as part of **Device** class in the **Startup** group and are defined as configuration files, meaning they are copied from the pack into a project folder and can be modifed there if necessary.

The use of device_h_pg can be abstracted with the `#define CMSIS_header_file` provided in [RTE_Components.h](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/cp_Packs.html#cp_RTECompH). This allows to have uniform include code in the application independent of the target device.

```c
#include "RTE_Components.h"                      // include information about project configuration
#include CMSIS_device_header                     // include <Device>.h file
```

Thereafter, the functions described under [API Reference](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/modules.html) can be used in the application.

For example, the following files are provided by the STM32F10x device family pack:

File                         | Description
:---------------------------------|:------------------------------------------------------------------------
".\Device\Source\ARM\startup_stm32f10x_cl.s" | startup_c_pg for the STM32F10x device variants
".\Device\Source\system_stmf10x.c"  | system_c_pg for the STM32F10x device families
".\Device\Include\stm32f10x.h"      | device_h_pg for the STM32F10x device families

cmsis_files_dfps provides more information on how CMSIS-Core files can be delivered in CMSIS Packs.
