---
id: "dv-report"
type: "concept"
domain: "drivers"
title: "Report"
summary: "The CMSIS-Driver Validation outputs the test report in a Plain Text format."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DriverValidation.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/report.html"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Driver Validation outputs the test report in a **Plain Text** format.

This report can be viewed on **STDOUT channel** (usually Virtual COM Port via Debug adapter).

A GPIO driver validation example report captured in a terminal application is shown below: 
```
CMSIS-Driver_Validation v3.1.0 CMSIS-Driver GPIO Test Report   Oct  9 2025   09:15:16 

TEST 01: GPIO_Setup                       PASSED
TEST 02: GPIO_SetDirection                PASSED
TEST 03: GPIO_SetOutputMode               PASSED
TEST 04: GPIO_SetPullResistor             PASSED
TEST 05: GPIO_SetEventTrigger             PASSED
TEST 06: GPIO_SetOutput                   PASSED
TEST 07: GPIO_GetInput                    PASSED

Test Summary: 7 Tests, 7 Passed, 0 Failed.
Test Result: PASSED

```

> **Note:** XML format was deprecated and removed, only **Plain Text** mode is available now.
