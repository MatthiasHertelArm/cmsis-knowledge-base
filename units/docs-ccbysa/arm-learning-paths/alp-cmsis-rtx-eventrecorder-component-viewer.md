---
id: "alp-cmsis-rtx-eventrecorder-component-viewer"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Using Event Recorder: Component Viewer"
summary: "To make these events more meaningful in the Event Recorder viewer, use the Component Viewer functionality."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/eventrecorder.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/eventrecorder/#component-viewer"
license: "CC-BY-SA-4.0"
mode: "V"
---

To make these events more meaningful in the Event Recorder viewer, use the Component Viewer functionality.

In a text editor, create a [Component Viewer Description File](https://www.keil.com/pack/doc/compiler/EventRecorder/html/SCVD_Format.html) (e.g. `rtos.scvd`) with the following:
```xml
<?xml version="1.0" encoding="utf-8"?>
 
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  <component name="MyExample" version="1.0.0"/>    <!-- name and version of the component  -->
 
    <events>
      <group name="My Events Group">
         <component name="EVR_Demo" brief="RTOS_Example" no="0x00" prefix="EvrNetMM_" info="Demo"/>
      </group>  
 
      <event id="1" level="API" property="Logging" value="goodbye from thread %d[val1]" info="Example output"  />
	  </events>
 
</component_viewer>
```
Exit the debugger, and return to `Target Options` > `Debug`, and click `Manage Component Viewer Description Files`.

Click `Add Component Viewer Description File`, and browse for the above. Save the settings.

Click `Debug` (`Ctrl+F5`), then `Run` (`F5`) to start the application.

This file has now defined event `0x0`, and this is reflected in the filter view:

(figure: Screenshot of the Event Viewer filter showing the custom EVR_Demo component with event 0x0 defined from the SCVD file#center)

These events are now processed into meaningful messages in the Event Recorder viewer:

(figure: Screenshot of the Event Viewer displaying decoded messages from the Component Viewer showing goodbye from thread messages instead of raw data#center)
