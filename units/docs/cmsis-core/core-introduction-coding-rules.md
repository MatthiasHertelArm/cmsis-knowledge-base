---
id: "core-introduction-coding-rules"
type: "concept"
domain: "core"
title: "Introduction: Coding Rules"
summary: "The CMSIS uses the following essential coding rules and conventions:"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/General/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/General/src/mainpage.md#coding-rules"
license: "Apache-2.0"
mode: "V"
---

The CMSIS uses the following essential coding rules and conventions:

 - Compliant with ANSI C (C99) and C++ (C++03).
 - Uses ANSI C standard data types defined in **`<stdint.h>`**.
 - Variables and parameters have a complete data type.
 - Expressions for `#define` constants are enclosed in parenthesis.
 - Conforms to MISRA 2012 (but does not claim MISRA compliance). MISRA rule violations are documented.

In addition, the CMSIS recommends the following conventions for identifiers:

 - **CAPITAL** names to identify Core Registers, Peripheral Registers, and CPU Instructions.
 - **CamelCase** names to identify function names and interrupt functions.
 - **Namespace_** prefixes avoid clashes with user identifiers and provide functional groups (i.e. for peripherals, RTOS, or DSP Library).

The CMSIS is documented within the source files with:

 - Comments that use the C or C++ style.
 - [Doxygen](https://www.doxygen.nl/) compliant **function comments** that provide:
    - brief function overview.
    - detailed description of the function.
    - detailed parameter explanation.
    - detailed information about return values.

Doxygen comment example:

```c
/**
 * @brief  Enable Interrupt in NVIC Interrupt Controller
 * @param  IRQn  interrupt number that specifies the interrupt
 * @return none.
 * Enable the specified interrupt in the NVIC Interrupt Controller.
 * Other settings of the interrupt such as priority are not affected.
 */
```
