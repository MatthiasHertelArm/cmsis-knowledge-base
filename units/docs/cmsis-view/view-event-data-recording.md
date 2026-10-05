---
id: "view-event-data-recording"
type: "concept"
domain: "trace"
title: "Event Data Recording"
summary: "Functions that record events along with data information"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_evr.txt"
license: "Apache-2.0"
mode: "V"
---

Functions that record events along with data information

This section describes the functions that are called from the user application or middleware libraries to record events.

Each event has an **id** that combines **level,** **component** **number,** and **message** **number:**
  - **level** is a **EventLevelXxxx** value that is used for filtering of the event recording (see EventRecorder_Setup).
  - **component** **number** identifies the software component and is used for filtering of event recording (see EventRecorder_Setup).
  - **message** **number** identifies the event.

can have an additional event level that is used for filtering.  The event level value is defined by EventLevelError, EventLevelAPI, EventLevelOp, or EventLevelDetail and added
to the event ID number.

**Note:** Before using these functions, the Event Recorder must be initialized with EventRecorderInitialize.

**Code example**
  - Refer to Event_Annotations
