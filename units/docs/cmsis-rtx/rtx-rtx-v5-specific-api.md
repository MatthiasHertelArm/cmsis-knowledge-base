---
id: "rtx-rtx-v5-specific-api"
type: "concept"
domain: "rtos"
title: "RTX v5 Specific API"
summary: "RTX v5 implementation specific definitions and functions defined in %rtx_os.h."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

RTX v5 implementation specific definitions and functions defined in **%rtx_os.h**.


The RTX v5 implementation is using the following **Namespace** prefixes for public symbol definitions:
  - `osRtx` for all general definitions and function names that relate to the RTX kernel.
  - `osRtx` with postfix `_t` for all typedefs.
  - `OS_Tick_` for interface functions to the hardware system tick timer.
  - `EvrRtx` for event function annotations that interface to the Event Recorder.

The RTX5 kernel can be customized for different application requirements:

- The function osRtxIdleThread implements the idle thread and allows set the system into sleep modes for lowPower or
  TickLess for ultra-low power operation.
- The function osRtxErrorNotify may be extended to handle system runtime errors.

RTX5 interfaces to the **Event Recorder**
and provides event information that helps to analyze the operation. Refer to rtx_evr for more information.
