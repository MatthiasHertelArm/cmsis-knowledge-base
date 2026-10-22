---
id: "view-elemhead-component-viewer-typedefs-elemhead-component-viewer-typedefs-typed-2"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/typedefs/typedef/member}: \\elemhead{component_viewer/typedefs/typedef/member/enum}"
summary: "Defines an enumeration name that is displayed as text instead of a value. A symbolic enumerator name represents a constant value that can be referenced using the syntax typedef_name:member_name:enum_name."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Defines an enumeration name that is displayed as text instead of a value.
A symbolic enumerator name represents a constant value that can be referenced using the syntax `typedef_name:member_name:enum_name`.



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<member>` | elem_member |  |  |
| Attributes | Description | Type | Use |
| name | Name of enumeration. Is shown as text in the \cviewer. | xs:string | required |
| value | Expression that specifies the enum value. | xs:string | optional |
| info | Descriptive text with additional information (comment). | xs:string | optional |


 
**Example:**
```
    <typedef name="Thread_CB"   size="52"   info="RTOS Task Control Block">
    
      <member name="Priority"      type="int8_t"     offset="2"    info="Thread Priority">
        <enum name="None"              value="0"                         info="No Priority"/>
        <enum name="Idle"              value="1"                         info="osPriorityIdle (lowest)"/>
        <enum name="Low"               value="2"                         info="osPriorityLow"/>
        <enum name="BelowNormal"       value="3"                         info="osPriorityBelowNormal"/>
        <enum name="Normal"            value="4"                         info="osPriorityNormal (default)"/>
        <enum name="AboveNormal"       value="5"                         info="osPriorityAboveNormal"/>
        <enum name="High"              value="6"                         info="osPriorityHigh"/>
        <enum name="Realtime"          value="7"                         info="osPriorityRealtime (highest)"/>
      </member>
      
    </typedef>
```
