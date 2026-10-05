---
id: "drv-theory-of-operation"
type: "concept"
domain: "drivers"
title: "Theory of Operation"
summary: "This section gives an overview of the general operation of CMSIS-Drivers. It explains the DriverFunctions that are common in all CMSIS-Drivers along with the CallSequence. The topic Data_Xfer_Functions describes how data read/write operations to the peripheral are implemented."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/operation.md"
license: "Apache-2.0"
mode: "V"
---

This section gives an overview of the general operation of CMSIS-Drivers. It explains the DriverFunctions that are common in all CMSIS-Drivers along with the CallSequence. The topic Data_Xfer_Functions describes how data read/write operations to the peripheral are implemented.

Each CMSIS-Driver defines an AccessStruct for calling the various driver functions and each peripheral (that is accessed via a CMSIS-Driver) has one Driver Instance.
