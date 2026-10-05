---
id: "sds-board-arm-v2m-mps3-sse-300-fvp-board-layer-for-corstone-300-fvp"
type: "concept"
domain: "test"
title: "Board: Arm V2M-MPS3-SSE-300-FVP: Board Layer for Corstone-300 FVP"
summary: "VIO driver interfaces with the arm_vio.py Python stub implementation which stores and loads signal values."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:template/Board/Corstone-300/README.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/template/Board/Corstone-300/README.md#board-layer-for-corstone-300-fvp"
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
| Heap                    | 768 kB (configured in linker file)
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

### VSI3 Interface

The board layer includes in the `arm_vsi3.py` interface that implements a playback 
interface for SDS data files using a [Virtual Streaming Interface](https://arm-software.github.io/AVH/main/simulation/html/group__arm__vsi.html). Refer to [Using FVP Simulation Models](https://arm-software.github.io/SDS-Framework/main/sdsio.html#layer-sdsio_fvp) for more information.

### FVP Configuration File

| File               | Description
|:-------------------|:-------------
| fvp_config.txt     | Corstone-300 FVP without Ethos-U or with Ethos-U55/U65
