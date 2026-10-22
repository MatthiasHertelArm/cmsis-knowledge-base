---
id: "view-elemhead-component-viewer-typedefs-2"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/typedefs/typedef/member}"
summary: "Define the member of a <typedef>; typically a struct, class member, or enumeration."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Define the member of a `<typedef>`; typically a **struct,** **class** member, or enumeration.



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<typedef>` | elem_typedef |  |  |
| Attributes | Description | Type | Use |
| name | Name of member variable. Is shown as text in the \cviewer. | xs:string | required |
| type | scalar_data_type or pointer to complex_data_type to access chained lists. | xs:string | required |
| offset | Offset to base address in `[Bytes]`. Use the uVision debug dialog **Symbols** to find the offset. You can use scvd_expression. For imported members, the offset is recalculated. Refer to the description of \attr{import} in `<typedef>`. | xs:string | required |
| size | Size in target memory in `[Bytes]`. | xs:string | optional |
| info | Descriptive text with additional information (comment). | xs:string | optional |
| Child Element | Description | Type | Occurrence |
| `<enum>` | Name of an enumeration that is displayed as text instead of a value. | EnumType | 0..* |


 
**Example:**
```
    <typedef name="Thread_CB"      size="52"                             info="RTOS Task Control Block">
   
      <member name="p_lnk"         type="*Thread_CB" offset="4"          info="Pointer to linked list"/>
  
      <member name="Entry"         type="uint32_t"   offset="40 + 8"     info="Calculated Entry Address"/>
     
      <member name="Priority"      type="int8_t"     offset="2"          info="Thread Priority">
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
