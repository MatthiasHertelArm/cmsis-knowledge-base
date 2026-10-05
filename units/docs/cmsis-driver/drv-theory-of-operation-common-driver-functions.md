---
id: "drv-theory-of-operation-common-driver-functions"
type: "concept"
domain: "drivers"
title: "Theory of Operation: Common Driver Functions"
summary: "Each CMSIS-Driver contains these functions:"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/operation.md#common-driver-functions"
license: "Apache-2.0"
mode: "V"
---

Each CMSIS-Driver contains these functions:

 - `GetVersion`: can be called at any time to obtain version information of the driver interface.

 - `GetCapabilities`: can be called at any time to obtain capabilities of the driver interface.

 - `Initialize`: must be called before powering the peripheral using `PowerControl`. This function performs the following:
     - allocate I/O resources.
     - register an optional `SignalEvent` callback function.

 - `SignalEvent`: is an optional callback function that is registered with the `Initialize` function. This callback function is initiated from interrupt service routines and indicates hardware events or the completion of a data block transfer operation.

 - `PowerControl`: Controls the power profile of the peripheral and needs to be called after `Initialize`. Typically, three power options are available (see ARM_POWER_STATE):
     - `ARM_POWER_FULL`: Peripheral is turned on and fully operational. The driver initializes the peripheral registers, interrupts, and (optionally) DMA.
     - `ARM_POWER_LOW` : (optional) Peripheral is in low power mode and partially operational; usually, it can detect external events and wake-up.
     - `ARM_POWER_OFF`: Peripheral is turned off and not operational (pending operations are terminated). This is the state after device reset.

 - `Uninitialize`: Complementary function to Initialize. Releases the I/O pin resources used by the interface.

 - `Control`: Several drivers provide a control function to configure communication parameters or execute miscellaneous control functions.

The section CallSequence contains more information on the operation of each function. Additional functions are specific to each driver interface and are described in the individual sections of each driver.
