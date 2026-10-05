---
id: "dap-atomic-commands"
type: "concept"
domain: "debug"
title: "Atomic Commands"
summary: "CMSIS-DAP command set is extended with two top level commands that allow the execution of multiple DAP commands further USB communication. Executing multiple CMSIS-DAP commands is typically a requirement at the reset time of some devices."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_atomic_gr.html"
license: "Apache-2.0"
mode: "V"
---

Execute atomic commands.

CMSIS-DAP command set is extended with two top level commands that allow the execution of multiple DAP commands further USB communication.
Executing multiple CMSIS-DAP commands is typically a requirement at the reset time of some devices. The sequence after reset can be time
critical and any USB communication would violate the available time window.
 - DAP_ExecuteCommands_gr : execute multiple DAP commands from a single command request
 - DAP_QueueCommands_gr : queue of multiple DAP commands before execution

These two DAP commands are used to collect several other DAP commands before execution.
Packet Size and Packet Count limitation (as reported via DAP_Info) must be respected by the debugger.

**Note:**
The DAP_atomic_gr are only available when DAP_Info with ID=0xF0 (Capabilities) returns in **Info** - Bit 4: **1 = Atomic Commands**.
