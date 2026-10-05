---
id: "view-fault-analysis-add-fault-storage-and-record-component"
type: "concept"
domain: "trace"
title: "Fault Analysis: Add Fault Storage (and Record) Component"
summary: "To use the Fault component in an application, you need to:"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/fault.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/fault.md#add-fault-storage-and-record-component"
license: "Apache-2.0"
mode: "V"
---

To use the Fault component in an application, you need to:

 - Select the software components **CMSIS-View:Fault:Storage**, **CMSIS-View:Fault:Record** and **CMSIS-View:Event Recorder** using the RTE management dialog.

   (figure: Select Fault)
 - Include the *ARM_Fault.h* header and *EventRecorder.h* header files in your source code
 - Add fault handlers that jump to ARM_FaultSave function
 - Check if a fault has occurred and output fault information to Event Recorder or STDIO and analyze it, or analyze fault information in a Component Viewer window in a debug session 

**Code example:**

```c
#include "EventRecorder.h"
#include "ARM_Fault.h"

__attribute__((naked)) void HardFault_Handler (void) {
  __ASM volatile (
    "b  ARM_FaultSave\n"
  );
}

int main() {
    SystemCoreClockUpdate();                      // System core clock update

    EventRecorderInitialize (EventRecordAll, 1U); // Initialize and start Event Recorder
    EventRecorderClockUpdate();                   // Update Event Recorder timestamp clock 

    if (ARM_FaultOccurred() != 0U) {              // If fault information exists
      ARM_FaultRecord();                          // Output decoded fault information via Event Recorder
      EventRecorderStop();                        // Stop Event Recorder
    }

    // ...

    while (1) {
       __NOP();
    }
}
```
