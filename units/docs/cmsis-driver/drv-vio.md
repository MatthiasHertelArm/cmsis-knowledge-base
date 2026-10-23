---
id: "drv-vio"
type: "concept"
domain: "drivers"
title: "VIO"
summary: "API for Virtual I/O (VIO) (%cmsis_vio.h)"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/VIO.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/VIO.txt"
license: "Apache-2.0"
mode: "V"
---

API for Virtual I/O (VIO) (%cmsis_vio.h)
 

The VIO software component is a virtual I/O abstraction for peripherals that are typically used in example projects. It
enables developers to move from an evaluation kit to custom hardware and helps to scale project examples at large to many
development boards:

 "Virtual I/O provides a generic API for examples and testing"

**VIO API**

The following header file defines the Application Programming Interface (API) for VIO:
  - **%cmsis_vio.h** : API for VIO

**VIO User Code Templates**

The VIO software component contains two user code templates with different purposes:
  - VIO:Custom: This file is an empty stub with all functions that are defined in the header file that can be used to
    implement the VIO layer for the hardware that is used in the application.
  - VIO:Virtual: This file uses a fixed memory location to emulate the VIO functionality and can be used off-the-shelf.

**VIO Memory Location Structure**

For testing purposes, it is required to have fixed memory locations that are used to read/store values. In the VIO:Virtual
template file (**%vio.c),** an exemplary implementation is shown:

```
// Input, output variables
__USED uint32_t vioSignalIn;                // Memory for incoming signal
__USED uint32_t vioSignalOut;               // Memory for outgoing signal
__USED int32_t  vioValue[VIO_VALUE_NUM];    // Memory for value used in vioGetValue/vioSetValue
```

Use these memory locations to monitor or set the variables as required in the application.

Two defines are available that help to disconnect the actual peripherals and enable virtual I/Os: `CMSIS_VIN` and
`CMSIS_VOUT.` They help to write code that can be used in testing environments without real hardware access. The following
implementation example shows such code:

**Code Example (VIO Implementation)**
```
// Initialize test input, output.
void vioInit (void) {
#if !defined CMSIS_VIN
// Add user variables here:
 
#endif
#if !defined CMSIS_VOUT
// Add user variables here:
 
#endif
 
  vioSignalIn  = 0U;
  vioSignalOut = 0U;
 
  memset(vioValue, 0, sizeof(vioValue));
 
#if !defined CMSIS_VOUT
// Add user code here:
// <code vioInit output>
 
  BSP_LED_Init(LED_BLUE);
  BSP_LED_Init(LED_RED);
  BSP_LED_Init(LED_GREEN);
// </code>
#endif
 
#if !defined CMSIS_VIN
// Add user code here:
// <code vioInit input>
 
  BSP_PB_Init(BUTTON_USER, BUTTON_MODE_GPIO);
// </code>
#endif
 
  return;
}
```

**Memory display in IDEs**

Arm Keil MDK uses the provided SCVD file to display the VIO signals in Component Viewer:
