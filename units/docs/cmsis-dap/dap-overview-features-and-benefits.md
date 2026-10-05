---
id: "dap-overview-features-and-benefits"
type: "concept"
domain: "debug"
title: "Overview: Features and Benefits"
summary: "Overview: Features and Benefits"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/index.html"
license: "Apache-2.0"
mode: "V"
---

- Provides a standardized interface for debuggers. Interfaces to many standard debuggers is available.
- Access to CoreSight registers of all Cortex processor architectures (Cortex-A/R/M).
- Connects via 5-pin JTAG or 2-pin Serial Wire Debug (SWD).
- Supports multi-core debugging.
- Supports Serial Wire Output (SWO) of Cortex-M devices.
- Easy to deploy to debug units based on Cortex-M microcontrollers.
- Debug unit may be integrated on an evaluation board.
- Using USB bulk transfers avoids driver installation on host PC.
- Supports time-critical JTAG or SWD command execution.
- Supports Test Domain Timer for time measurement using the debug unit.
- Supports UART communication port, which can be routed to USB COM Port (optional) or native CMSIS-DAP commands (new in CMSIS-DAP Version 2.1.0).
- Flexible customization is possible with vendor-specific commands.
