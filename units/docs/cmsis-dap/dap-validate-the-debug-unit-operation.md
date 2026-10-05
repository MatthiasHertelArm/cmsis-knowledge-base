---
id: "dap-validate-the-debug-unit-operation"
type: "concept"
domain: "debug"
title: "Validate the debug unit operation"
summary: "A validation project for Arm Keil MDK is provided in the folder /Firmware/Validation/MDK5."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/dap_validate.md"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/dap_validate.html"
license: "Apache-2.0"
mode: "V"
---

A validation project for Arm Keil MDK is provided in the folder `/Firmware/Validation/MDK5`.

The `Validation.uvprojx` project contains a simple application that needs to be adapted to the target hardware connected to the debug unit. Once the adaptation is complete, you may open a Command window and call the batch file `test.bat` (optionally with the path to the µVision executable):

(figure: Validate debug unit using target hardware and Arm Keil MDK)

The batch file will create a `test_results.txt` and `test.log` file in the project directory.
