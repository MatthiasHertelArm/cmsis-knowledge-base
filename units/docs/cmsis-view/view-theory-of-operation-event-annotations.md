---
id: "view-theory-of-operation-event-annotations"
type: "concept"
domain: "trace"
title: "Theory of operation: Event Annotations"
summary: "To to stream dynamic event information, insert calls to the EventRecorder_Data functions on relevant code locations:"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/event_recorder.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/event_recorder.md#event-annotations"
license: "Apache-2.0"
mode: "V"
---

To to stream dynamic event information, insert calls to the EventRecorder_Data functions on relevant code locations:

 - EventRecordData to record a data field with flexible length.
 - EventRecord2 to record up to two 32-bit integer values.
 - EventRecord4 to record up to four 32-bit integer values.

These EventRecorder_Data functions receive as first parameter an *id* event identifier used for filtering and displaying. The macro EventID may be used to compose *id* values to include *level* and *component* numbers.

**Example:**

```c
#include "EventRecorder.h"                                   // ARM::CMSIS-View:Event Recorder

int some_error = 0;                                          // error flag
char string[10] = "MyTest";                                  // some test string

void MyFunction (int parameter) {
  EventRecord2 (1+EventLevelAPI, parameter, 0);              // Event at Start
    ;
  if (some_error)  {
    EventRecord2 (2+EventLevelError, 0, 0);                  // Event at Error
    return;
  }
  EventRecordData (3+EventLevelOp, string, sizeof(string));  // Event at Finish
  return;
}

int main (void) {
  EventRecorderInitialize (EventRecordAll, 1);               // initialize and start Event Recorder

  MyFunction (0x10);
  some_error = 1;                                            // set error flag
  MyFunction (0x60);
}
```

When executing this example in the µVision debugger, use the menu command **View - Analysis Windows - Event Recorder** to open the Event Recorder window. This should show the following output:

(figure: Output shown in Event Recorder window)
