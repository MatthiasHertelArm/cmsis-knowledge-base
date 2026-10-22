---
id: "view-theory-of-operation-format-event-information"
type: "concept"
domain: "trace"
title: "Theory of operation: Format Event Information"
summary: "You may create an .SCVD (Software Component View Description) file to format the event output so that matches the application. The event output is created using the elem_events."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/event_recorder.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/event_recorder.md#format-event-information"
license: "Apache-2.0"
mode: "V"
---

You may create an *.SCVD (Software Component View Description) file  to format the event output so that matches the application. The event output is created using the elem_events.

**SCVD file example**

```xml
<?xml version="1.0" encoding="utf-8"?>

<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  <component name="MyExample" version="1.0.0"/>    <!-- name and version of the component  -->

    <events>
      <group name="My Events Group">
         <component name="MyApp"      brief="My Application"    no="0x00" prefix="EvrNetMM_"    info="Network - System - Dynamic Memory Management"/>
      </group>

      <event id="1" level="API"   property="MyFunction"        value="parameter=%x[val1]"     info="Event on start of MyFunction"  />
      <event id="2" level="Error" property="MyFunctionError"                                  info="Event on error in MyFunction" />
      <event id="3" level="Op"    property="MyFunctionProcess" value="string=%t[val1]"        info="Event on operation in MyFunction"  />
    </events>

</component_viewer>
```

In the µVision debugger, this *.SCVD file is specified in the dialog **Options for Target - Debug - Manage Component Viewer Description Files**. Click on **Add Component Viewer Description File** and add the related *.SCVD file.

(figure: Manage *.SCVD files)

The Event Recorder displays the events as shown below.

(figure: Event Recorder output formatted with *.SCVD file)

The described groups and events also show up in the filter dialog.

(figure: Event Recorder Filter dialog)
