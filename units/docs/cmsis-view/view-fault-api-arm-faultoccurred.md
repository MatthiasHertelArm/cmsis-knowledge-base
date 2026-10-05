---
id: "view-fault-api-arm-faultoccurred"
type: "concept"
domain: "trace"
title: "Fault API: ARM_FaultOccurred"
summary: "Call during startup to check if a fault occurred and if fault information is available, for example decode the fault information using ARM_FaultPrint or ARM_FaultRecord functions."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_fault.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_fault.txt"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_FaultOccurred
```


Call during startup to check if a fault occurred and if fault information is available, for example decode the fault information using ARM_FaultPrint or ARM_FaultRecord functions.

**Code** **Example**
```
#include "EventRecorder.h"
#include "ARM_Fault.h"

int main() {

  EventRecorderInitialize (EventRecordAll, 1U); // Initialize and start Event Recorder

  if (ARM_FaultOccurred() != 0U) {              // If fault information exists
    ARM_FaultPrint();                           // Output decoded fault information via STDIO
    ARM_FaultRecord();                          // Output decoded fault information via Event Recorder
    EventRecorderStop();                        // Stop Event Recorder
  }

  // ...
}
```
