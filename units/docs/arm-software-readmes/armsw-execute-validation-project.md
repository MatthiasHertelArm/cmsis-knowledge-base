---
id: "armsw-execute-validation-project"
type: "concept"
domain: "rtos"
title: "Execute Validation Project"
summary: "Validation project uses CMSIS Project Manager to generate independent projects."
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/CMSIS-RTOS2_Validation@f5e2c7f:Project/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTOS2_Validation/blob/f5e2c7f/Project/README.md"
license: "Apache-2.0"
mode: "V"
---

Validation project uses CMSIS Project Manager to generate independent projects.

Independent project can be generated for specific RTOS, DEVICE and COMPILER. Possible values for all variables are listed below:

| RTOS     |  Device  | Compiler |
|----------|----------|----------|
| FreeRTOS |  CM0plus | AC6      |
| RTX5     |  CM3     | GCC      |
|          |  CM4     | CLANG    |
|          |  CM7     |          |
|          |  CM23    |          |
|          |  CM33    |          |
|          |  CM55    |          |
|          |  CM85    |          |

Input file for cbuild is Validation.csolution.yml
