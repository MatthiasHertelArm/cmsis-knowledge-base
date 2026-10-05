---
id: "ethint-board-arm-sse-320-board-layer-for-corstone-320-fvp"
type: "concept"
domain: "edge-ai"
title: "Board: Arm SSE-320: Board Layer for Corstone-320 FVP"
summary: "VIO driver interfaces with the arm_vio.py Python stub implementation which stores and loads signal values."
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@529e966:Board/Corstone-320/README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/Board/Corstone-320/README.md#board-layer-for-corstone-320-fvp"
license: "Apache-2.0"
mode: "V"
---

This layer works for:

```yml
  board: ARM::SSE-320
  device: ARM::SSE-320-FVP
```

### System Configuration

| System Component        | Setting
|:------------------------|:----------------------------------
| Heap                    |  96 kB (configured in linker file)
| Stack (MSP)             |  32 kB (configured in linker file)

### STDIO mapping

**STDIO** is routed to terminal via **UART0** peripheral

### CMSIS-Driver mapping

| CMSIS-Driver           | Peripheral | Connection
|:-----------------------|:-----------|:----------------------
| Driver_USART0          | UART0      | STDIN, STDOUT, STDERR
| CMSIS-Driver VIO       | VIO        | CMSIS_VIO

### CMSIS-Driver Virtual I/O mapping

VIO driver interfaces with the `arm_vio.py` Python stub implementation which
stores and loads signal values.

### FVP Configuration File

| File               | Description
|:-------------------|:-------------
| fvp_config_u85.txt | Corstone-320 FVP with an Ethos-U85-256
