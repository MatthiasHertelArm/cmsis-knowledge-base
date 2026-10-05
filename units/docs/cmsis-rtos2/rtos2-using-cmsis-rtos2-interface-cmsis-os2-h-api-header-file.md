---
id: "rtos2-using-cmsis-rtos2-interface-cmsis-os2-h-api-header-file"
type: "concept"
domain: "rtos"
title: "Using CMSIS-RTOS2 Interface: cmsis_os2.h API header file"
summary: "The CMSIS-RTOS2 interface is provided in cmsis_os2.h file - a standard C header file that user applications and middleware components need to include to access CMSIS-RTOS2 API. It contains all the function declarations, as well as type and macro definitions."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/using.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/using.md#cmsis-os2-h-api-header-file"
license: "Apache-2.0"
mode: "V"
---

The **CMSIS-RTOS2** interface is provided in **cmsis_os2.h** file - a standard C header file that user applications and middleware components need to include to access CMSIS-RTOS2 API. It contains all the function declarations, as well as type and macro definitions.

An implementation specific header file (*rtos*.h in the picture below) provides access to such definitions. Using the **cmsis_os2.h** along with dynamic object allocation allows to create source code or libraries that require no modifications when using on a different CMSIS-RTOS2 implementation.

(figure: CMSIS-RTOS File Structure)

Once the files are added to a project, the user can start working with the CMSIS-RTOS functions.

CMSIS-RTOS2 is especially easy use to integrate in projects that support [CMSIS-Pack format](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html). CMSIS-RTOS2 is provided in the [CMSIS 6 Software Pack](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/../General/cmsis_pack.html) as a software component in form of [a central API defintion](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/cp_Packs.html#cp_APIDef) It is part of component class **CMSIS** and belongs to component group **RTOS2**.
