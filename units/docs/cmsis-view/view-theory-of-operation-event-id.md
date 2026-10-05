---
id: "view-theory-of-operation-event-id"
type: "concept"
domain: "trace"
title: "Theory of operation: Event id"
summary: "The EventRecorderData functions get a parameter id that is composed of level, component number, and message number as shown below:"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/event_recorder.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/event_recorder.md#event-id"
license: "Apache-2.0"
mode: "V"
---

The EventRecorder_Data functions get a parameter `id` that is composed of *level*, *component number*, and *message number* as shown below:

| *id*               | bits   | Description
|--------------------|--------|----------------------------------------------------
| *message number*   |  0..7  | identifies the event message information of the software component
| *component number* |  8..15 | identifies the software component (also used for filtering, see table below)
| *level*            | 16..17 | specifies the class of the message for filtering (see table below)
| --- (reserved)     | 18..31 | set to 0

The *level* specifies the category of the event message and can be used for filtering:

| *level*                    | Message relates to ...
|----------------------------|----------------------------------------------------
| EventLevelError = 0   | Run-time error
| EventLevelAPI = 1     | API function call
| EventLevelOp = 2      | Internal operation
| EventLevelDetail = 3  | Additional detailed information of operations

The *component number* specifies the software component that the event message belongs to and can be also used for filtering:

| *component number*        | Relation to software components
|---------------------------|----------------------------------------------------
| 0x0  .. 0x3F (0 .. 63)    | software components of the user application
| 0x40 .. 0x7F (64 .. 127)  | third party middleware components
| 0x80 .. 0xED (128 .. 237) | MDK-Middleware components
| 0xEE (238)                | Fault component
| 0xEF (239)                | Start/Stop events for Event Statistic information
| 0xF0 .. 0xFC (240 .. 253) | RTOS kernel
| 0xFD (253)                | Inter-process communication layer (multiprocessor systems)
| 0xFE (254)                | printf-style debug outputs
| 0xFF (255)                | Event Recorder messages

The following sections describe:

 - er_config : explains the set-up of the Event Recorder and the configuration of a user provided timer.
 - er_filtering : shows how to limit the amount of data that is displayed in the Event Recorder window.
 - er_req : lists the technical data and explains the hardware and software requirements.
