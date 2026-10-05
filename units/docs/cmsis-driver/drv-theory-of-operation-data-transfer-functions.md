---
id: "drv-theory-of-operation-data-transfer-functions"
type: "concept"
domain: "drivers"
title: "Theory of Operation: Data Transfer Functions"
summary: "A CMSIS-Driver implements non-blocking functions to transfer data to a peripheral. This means that the driver configures the read or write access to the peripheral and instantly returns to the calling application. The function names for data transfer end with:"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/operation.md#data-transfer-functions"
license: "Apache-2.0"
mode: "V"
---

A CMSIS-Driver implements non-blocking functions to transfer data to a peripheral. This means that the driver configures the read or write access to the peripheral and instantly returns to the calling application. The function names for data transfer end with:

 - `Send` to write data to a peripheral.
 - `Receive` to read data from a peripheral.
 - `Transfer` to indicate combined read/write operations to a peripheral.

During a data transfer, the application can query the number of transferred data items using functions named **Get_xxx_Count**. On completion of a data transfer, the driver calls a callback function with a specific event code.

During the data exchange with the peripheral, the application can decide to:

 - Wait (using an RTOS scheduler) for the callback completion event. The RTOS is controlled by the application code which makes the driver itself RTOS independent.
 - Use polling functions that return the number of transferred data items to show progress information or partly read or fill data transfer buffers.
 - Prepare another data transfer buffer for the next data transfer.

The following diagram shows the basic communication flow when using the `_Send` function in an application.

(figure: Non-blocking Send Function)
