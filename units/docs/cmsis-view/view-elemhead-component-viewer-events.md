---
id: "view-elemhead-component-viewer-events"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/events}"
summary: "Is the enclosing element for objects that define the output for \\erecorder."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Is the enclosing element for objects that define the output for \erecorder.



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<component_viewer>` | elem_component_viewer |  |  |
| Child Element | Description | Type | Occurrence |
| \spref{elem_event,event} | Define an event. | EventType | 0..* |
| \spref{elem_group,group} | Create an event group. | GroupType | 0..* |


 
**Example:**
```
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
 
 


\page  elem_group \elemhead{component_viewer/events/group}

Define groups of software components that are shown together.



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| events | elem_events |  |  |
| Attributes | Description | Type | Use |
| name | Define the name of a group. This name is used for filtering. | xs:string | required |
| Child Element | Description | Type | Occurrence |
| \refelem{elem_group_component,component} | Component within the group. | ComponentType | 0..* |
