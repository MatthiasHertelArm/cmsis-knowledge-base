---
id: "view-fault-analysis-fault-information-analysis"
type: "concept"
domain: "trace"
title: "Fault Analysis: Fault information analysis"
summary: "To see and analyze the details of a fault, there are the following options:"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/fault.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/fault.md#fault-information-analysis"
license: "Apache-2.0"
mode: "V"
---

To see and analyze the details of a fault, there are the following options:

 - Fault information can be decoded and written to the Event Recorder by calling the function ARM_FaultRecord (Event Recorder has to be operational). This is an exemplary output in µVision:  
   (figure: Fault information with Event Recorder)
 - Fault information can be decoded and written to the standard output by calling the function ARM_FaultPrint (this function is implemented in a user template and can be changed by the user):  
   (figure: Fault information with STDIO)
 - Fault information can be inspected in a debug session by viewing it in the Component Viewer (screenshot showing µVision):  
   (figure: Fault information with Component Viewer)
