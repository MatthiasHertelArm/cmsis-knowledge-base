---
id: "drv-theory-of-operation-function-call-sequence"
type: "concept"
domain: "drivers"
title: "Theory of Operation: Function Call Sequence"
summary: "For normal operation of the driver, the API functions GetVersion, GetCapabilities, Initialize, PowerControl, Uninitialize are called in the following order:"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/operation.md#function-call-sequence"
license: "Apache-2.0"
mode: "V"
---

For normal operation of the driver, the API functions `GetVersion`, `GetCapabilities`, `Initialize`, `PowerControl`, `Uninitialize` are called in the following order:

\msc
 a [label="", textcolor="indigo", linecolor="indigo", arclinecolor="indigo"],
 b [label="", textcolor="blue", linecolor="blue", arclinecolor="blue"];

 a rbox a [label="Middleware", linecolor="indigo"],
 b rbox b [label="Driver", linecolor="blue"];
 --- [label="Verify API version"];
 a=>b [label="GetVersion ()", textcolor="gray", linecolor="gray"];
 --- [label="Obtain driver features"];
 a=>b [label="GetCapabilities (...)", textcolor="gray", linecolor="gray"];
 ---  [label="Setup software resources"];
 a=>b [label="Initialize (...)", textcolor="red", linecolor="red"];
 --- [label="Setup the peripheral"];
 a=>b  [label="PowerControl (ARM_POWER_FULL)", textcolor="red", linecolor="red"];
 --- [label="Operate with the peripheral"];
 a=>b [label="Data Transfer Functions"];
 a<=b  [label="SignalEvent (...)"];
 --- [label="Wait for external hardware events"];
 a=>b  [label="PowerControl (ARM_POWER_LOW)"];
 a<=b  [label="SignalEvent (...)"];
 --- [label="Stop working with peripheral"];
 a=>b [label="PowerControl (ARM_POWER_OFF)", textcolor="red", linecolor="red"];
 a=>b [label="Uninitialize (...)", textcolor="red", linecolor="red"];
\endmsc

The functions `GetVersion` and `GetCapabilities` can be called any time to obtain the required information from the driver. These functions return always the same information.


### Start Sequence

To start working with a peripheral the functions `Initialize` and `PowerControl` need to be called in this order:

```c
  drv->Initialize (...);                 // Allocate I/O pins
  drv->PowerControl (ARM_POWER_FULL);    // Power up peripheral, setup IRQ/DMA
```

 - `Initialize` typically allocates the I/O resources (pins) for the peripheral. The function can be called multiple times; if the I/O resources are already initialized it performs no operation and just returns with ARM_DRIVER_OK.
 - `PowerControl` (`ARM_POWER_FULL`) sets the peripheral registers including interrupt (NVIC) and optionally DMA. The function can be called multiple times; if the registers are already set it performs no operation and just returns with ARM_DRIVER_OK.

### Stop Sequence

To stop working with a peripheral the functions `PowerControl` and `Uninitialize` need to be called in this order:

```c
  drv->PowerControl (ARM_POWER_OFF);     // Terminate any pending transfers, reset IRQ/DMA, power off peripheral
  drv->Uninitialize (...);               // Release I/O pins
```

The functions `PowerControl` and `Uninitialize` always execute and can be used to put the peripheral into a **Safe State**, for example after any data transmission errors.  To restart the peripheral in a error condition, you should first execute the CS_stop and then the CS_start.

 - `PowerControl` (`ARM_POWER_OFF`) terminates any pending data transfers with the peripheral, disables the peripheral and leaves it in a defined mode (typically the reset state).
    - when DMA is used it is disabled (including the interrupts)
    - peripheral interrupts are disabled on NVIC level
    - the peripheral is reset using a dedicated reset mechanism (if available) or by clearing the peripheral registers
    - pending peripheral interrupts are cleared on NVIC level
    - driver variables are cleared
 - `Uninitialize` always releases I/O pin resources.
