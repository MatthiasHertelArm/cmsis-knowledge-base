---
id: "ethint-board-alifsemiconductor-appkit-e8-setools"
type: "concept"
domain: "edge-ai"
title: "Board: AlifSemiconductor AppKit-E8-AIML: SETOOLS"
summary: "Before using layers on the board it is required to program the ATOC of the device using the Alif SETOOLS. The required .vscode\\tasks.json commands are part of the Blinky examples. It is therefore recommended to start with such an example."
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@529e966:Board/AppKit-E8_M55_HP/README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/Board/AppKit-E8_M55_HP/README.md#setools"
license: "Apache-2.0"
mode: "V"
---

Before using layers on the board it is required to program the ATOC of the device
using the Alif SETOOLS. The required `.vscode\tasks.json` commands are part of the
Blinky examples. It is therefore recommended to start with such an example.

Refer to the section [Usage](https://www.keil.arm.com/packs/ensemble-alifsemiconductor)
in the overview page of the Alif Semiconductor Ensemble DFP/BSP for information on how
to setup these tools.

In VS Code use the menu command **Terminal - Run Tasks** and execute:

- "Alif: Install M55_HE or M55_HP debug stubs (single core configuration)"

> Note: For Windows ensure that the Terminal default is `Git Bash` or `PowerShell`.
> - Configure SW4 to position SE (Secure UART) to enable SETOOLS communication with the device.
