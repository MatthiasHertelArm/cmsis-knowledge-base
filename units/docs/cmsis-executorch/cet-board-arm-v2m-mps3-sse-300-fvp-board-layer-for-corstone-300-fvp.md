---
id: "cet-board-arm-v2m-mps3-sse-300-fvp-board-layer-for-corstone-300-fvp"
type: "concept"
domain: "bring-up"
title: "Board: Arm V2M-MPS3-SSE-300-FVP: Board Layer for Corstone-300 FVP"
summary: "VIO driver interfaces with the arm_vio.py Python stub implementation which stores and loads signal values."
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:board/Corstone-300/README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/board/Corstone-300/README.md#board-layer-for-corstone-300-fvp"
license: "Apache-2.0"
mode: "V"
---

This layer works for:

```yml
  board: ARM::V2M-MPS3-SSE-300-FVP
  device: ARM::SSE-300-MPS3
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
| fvp_config_u65.txt | Corstone-300 FVP with an Ethos-U65-256
| fvp_config_u55.txt | Corstone-300 FVP with an Ethos-U55-128
