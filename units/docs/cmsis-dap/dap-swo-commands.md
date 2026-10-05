---
id: "dap-swo-commands"
type: "concept"
domain: "debug"
title: "SWO Commands"
summary: "CMSIS-DAP SWO (Serial Wire Output) ----------------------------------"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_swo_gr.html"
license: "Apache-2.0"
mode: "V"
---

Configure the parameters for SWO mode.

CMSIS-DAP SWO (Serial Wire Output)
----------------------------------

CMSIS-DAP (CoreSight Debug Access Port) specifies debug protocol and interface for devices with CoreSight Debug and Trace.

**Note:**
The DAP_swo_gr are only available when DAP_Info with ID=0xF0 (Capabilities) returns in **Info** - Bit 2: **1 = SWO UART** or Bit 3: **1 = SWO Manchester**.

The following extension adds support for trace over SWO (Serial Wire Output).

SWO add-on is a compatible extension of the existing CMSIS-DAP specification.
Existing debugger implementations on PC do not require any modifications for debugging. They only need to be extended in order to support trace.

The following new commands are added:
 - DAP_SWO_Transport
 - DAP_SWO_Mode
 - DAP_SWO_Baudrate
 - DAP_SWO_Control
 - DAP_SWO_Status
 - DAP_SWO_ExtendedStatus
 - DAP_SWO_Data

Format of the new commands is specified below using CMSIS-DAP documentation style.
Note: 16-bit values (SHORT) and 32-bit values (WORD) are encoded as little-endian.

The following existing commands are extended:
 - DAP_Info
