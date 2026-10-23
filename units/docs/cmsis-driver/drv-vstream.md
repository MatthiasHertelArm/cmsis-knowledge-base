---
id: "drv-vstream"
type: "concept"
domain: "drivers"
title: "vStream"
summary: "Driver API for Virtual Streaming interface using fixed-size data blocks (%cmsis_vstream.h)"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
license: "Apache-2.0"
mode: "V"
---

Driver API for Virtual Streaming interface using fixed-size data blocks (%cmsis_vstream.h)


The **vStream** software component provides an abstraction layer for streaming data using fixed-size blocks.
It offers a standardized interface to interact with various streaming devices such as sensors, cameras, microphones, speakers, or simulated devices.
It allows seamless development on one platform and deployment on another.

**vStream API**

The following header file defines the Application Programming Interface (API) for Virtual Streaming interface:
  - **%cmsis_vstream.h**: Driver API for Virtual Streaming interface

The driver implementation is typically a part of the Board Support Pack (BSP) for a specific board with streaming devices.

**Driver Functions**

All driver functions are grouped within the vStreamDriver_t access structure.

**User Code Template**

The **CMSIS Driver:vStream (API):Custom** component provides a stub implementation of all vStream driver functions.  
This template can be used to implement the vStream driver for your target hardware.

The default driver access structure is named **Driver_vStreamDevice**, but `Device` should be replaced with
a specific device name, such as `Driver_vStreamAccelerometer`. See vStreamDriver_t for more details.

**Code Example**

The following example demonstrates how to use the vStream driver for an accelerometer:

\include vStream_Example.c
