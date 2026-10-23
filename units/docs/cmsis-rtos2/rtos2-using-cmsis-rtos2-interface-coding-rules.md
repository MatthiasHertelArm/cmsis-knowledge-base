---
id: "rtos2-using-cmsis-rtos2-interface-coding-rules"
type: "concept"
domain: "rtos"
title: "Using CMSIS-RTOS2 Interface: Coding Rules"
summary: "CMSIS-RTOS2 follows the general CMSIS coding rules. Additionally following Namespace prefixes are used in CMSIS-RTOS2 API:"
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/using.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/using.md#coding-rules"
license: "Apache-2.0"
mode: "V"
---

CMSIS-RTOS2 follows [the general CMSIS coding rules](https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/../General/index.html#coding_rules). Additionally following Namespace prefixes are used in CMSIS-RTOS2 API:

 - `os` for all definitions and function names. Examples: osThreadPrivileged, osKernelStart.
 - `os` with postfix `_t` for all typedefs. Examples: osStatus_t, osThreadAttr_t.
