---
id: "view-theory-of-operation-resource-requirements"
type: "concept"
domain: "trace"
title: "Theory of operation: Resource requirements"
summary: "Target: Cortex-M3 using DWT cycle counter as timer"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/event_recorder.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/event_recorder.md#resource-requirements"
license: "Apache-2.0"
mode: "V"
---

**Technical data of Event Recorder firmware**

Target: Cortex-M3 using DWT cycle counter as timer

|Parameter                         | ARMCC V6.13.1 | ARMCC V6.13.1
|:---------------------------------|---------------|--------------
|Compiler options                  | -Os           | -O3
|ROM size                          | < 1.7k bytes  | < 3.4k bytes
|RAM size @8 records (min)         | 292 bytes     | 292 bytes
|RAM size @64 records (default)    | 1188 bytes    | 1188 bytes
|EventRecord2 (id+8bytes)     | 197 cycles    | 184 cycles
|EventRecord4 (id+16bytes)    | 343 cycles    | 319 cycles
|EventRecordData (id+8bytes)  | 276 cycles    | 252 cycles
|EventRecordData (id+16bytes) | 425 cycles    | 397 cycles
|EventRecordData (id+24bytes) | 554 cycles    | 519 cycles
|EventRecordData (id+32bytes) | 685 cycles    | 643 cycles

> **Note**
> - ROM size is specified for image with all Event Recorder functions being used.
> - RAM size can be calculated as `164 + 16 * <Number of Records> (defined by EVENT_RECORD_COUNT in EventRecorderConf.h)`.
> - Timing was measured in simulator (zero cycle memory, no interrupts). Function parameter in application is not considered.

**Usage of records by Event Recorder functions**

|Function                          | Number of Records used
|:---------------------------------|-----------------------------
|EventRecord2                 | 1
|EventRecord4                 | 2
|EventRecordData              | (event data length + 7) / 8
# Using Event Recorder

> **Note**
> - The following steps explain how to enable views for static information _and_ dynamic events in the µVision debugger. Other tools might use different ways to accomplish this.

**For User Code:**

 1. Add_Event_Recorder.
 2. [Optional] Locate the Event Recorder data to uninitialized memory to avoid overwriting the entries on program reset.
 3. [Optional] Set the correct initial time stamp.
 4. [Optional] Create a heartbeat to avoid timer overflow problems.
 5. Add Event_Annotations in the C source to be able to stream dynamic event information.
 6. Create an SCVD file to Format_Event_Information that matches with application code.

**For Pre-annotated Software Components:**

The software packs for MDK-Middleware, CMSIS, CMSIS-FreeRTOS already contain the relevant *.SCVD files and the related event annotations in the C source code.

 1. Add_Event_Recorder to the project.
 2. Select a Debug variant for the middleware component to enable event information (for RTX5 select **Source** variant).
