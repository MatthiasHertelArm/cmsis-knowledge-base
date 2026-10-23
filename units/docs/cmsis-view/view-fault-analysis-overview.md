---
id: "view-fault-analysis-overview"
type: "concept"
domain: "trace"
title: "Fault Analysis: Overview"
summary: "The software components CMSIS-View:Fault provide infrastructure and API function calls to store, record, and analyze the Cortex-M Exception Fault information."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/fault.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/fault.md#overview"
license: "Apache-2.0"
mode: "V"
---

The software components **CMSIS-View:Fault** provide infrastructure and API function calls to store, record, and analyze the Cortex-M Exception Fault information.

Arm Cortex-M processors raise an exception fault on critical system failures such as illegal memory write or read, access to an disabled peripheral, execution of an invalid instruction, or division by zero:

 - The component **CMSIS-View:Fault:Storage** can be used to save an exception fault information for later analysis.
 - The component **CMSIS-View:Fault:Record** decodes a saved exception fault information and records this information using the **Event Recorder**.

A typical execution flow is shown in the diagram below.

(figure: Exception Fault Analysis)

 - flt_theory explains in details how the Fault component stores fault information and how it can be used for further analysis.
 - flt_use provides instructions on how to enable Fault component in a project.

An application note is available that describes the Cortex-M fault exceptions from the programmers view and explains their usage during the software development cycle: [KAN209 - Using Cortex-M3/M4/M7 Fault Exceptions](https://developer.arm.com/documentation/kan209/latest).
# Theory of operation

This section describes how the **Fault** component operates and how the fault information can be analyzed.

The **Fault** component is implemented in the target application using the software component **CMSIS-View:Fault:Storage** which adds the source file *ARM_FaultStorage.c* to the application.

This source file provides an ARM_FaultSave function which is used to save the fault information into an uninitialized part of the RAM which can then be analyzed on-chip, or on a host computer using a debugger. When using semihosting, cloud storage, or another remote location for storing the log file, you can do post-processing using evntlst.
