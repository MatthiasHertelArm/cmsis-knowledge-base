---
id: "view-elemhead-component-viewer-events-elemhead-component-viewer-events-group-c-2"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/events}: \\elemhead{component_viewer/events/group/component/state}"
summary: "Define state information for an event group. This state information is used for: - graphic display of a time-line (for example in the System Analyzer of uVision). - collecting statistical information about an event group."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Define state information for an event group.  This state information is used for:
  - graphic display of a time-line (for example in the System Analyzer of uVision).
  - collecting statistical information about an event group.
  
The state information is referenced by the element \refelem{elem_event,event} and associated with an handle and a handle name.
State information is for example used to display the activity of RTOS threads. But this implementation is generic and allows it
to use also for any type of software component.



  | 
    Parent Element | 
    Element Chain | 
  

  | 
    group | 
    elem_component | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    name | 
    State name that is displayed and used for reference in \refelem{elem_event,event} | 
    xs:string | 
    required | 
  

  | 
    plot | 
    Output in graphic time-line display (System Analyzer) with values:\n
  "off" for empty display [no line or box] (default).\n
  "line" for display a line.\n
  "box" for display a box.
	 | 
    xs:string | 
    optional | 
  

  | 
    color | 
    Color for the line or box in graphic time-line display (System Analyzer) with values: "blue" (default), "red", "green", "black". | 
    xs:string | 
    optional | 
  

  | 
    unique | 
    "1" indicates that only handle from this group can have this state. Event handles that had this state previously are set to state that is marked with dormant="1". (default "0") | 
    xs:string | 
    optional | 
  

  | 
    dormant | 
    "1" indicates the state to fall back from the state that is marked with unique="1". (default "0") | 
    xs:string | 
    optional | 
  

  | 
    ssel | 
    "1" indicates the state is selected for top-level view of events and statistics. (default "0") | 
    xs:string | 
    optional | 
  


 
**Example:**
```
<events>	 
  <group>
    <component name="MyEventComponent1"  brief="MyC1"    no="0x0B"  prefix="EvrMyC1_"     info="My Component - Demo example">
      <state name="Clear"       plot="box"  color="red"    />
      <state name="Create"      plot="box"                 />
      <state name="Delete"      plot="off"                 />
      <state name="Waiting"     plot="box"  color="green"  />
      <state name="Active"      plot="box"  bold="1"       />
      <state name="Idle"        plot="line"                 />
      <state name="Stalled"     plot="line" color="black"  />
	</component>
    <component name="MyEventComponent2"  brief="MyC2"    no="0x0C"  prefix="EvrMyC2_"     info="My Component - Demo example"/>
  </group>
  <event id="0xB00" level="API"  property="Clear"     state="Clear"    handle="val1"                                    value="h=%x[val1]"            info="Event on Clear"/>
  <event id="0xB01" level="API"  property="Create"    state="Create"   handle="val1" hname="%N[val2]"  tracking="Start" value="h=%x[val1] n=%N[val2]" info="Event on Create"/>
  <event id="0xB02" level="API"  property="Delete"    state="Delete"   handle="val1"                   tracking="Stop"  value="h=%x[val1]"            info="Event on Delete"/>
  <event id="0xB03" level="API"  property="Active"    state="Active"   handle="val1"                                    value="h=%x[val1]"            info="Event on Active"/>
  <event id="0xB04" level="API"  property="Waiting"   state="Waiting"  handle="val1"                                    value="h=%x[val1]"            info="Event on Waiting"/>
  <event id="0xB05" level="API"  property="Idle"      state="Idle"     handle="val1"                                    value="h=%x[val1]"            info="Event on Idle"/>
  <event id="0xB06" level="API"  property="Stalled"   state="Stalled"  handle="val1"           
</events>
```
 


\page  elem_event \elemhead{component_viewer/events/event}

Define an event that can occur for the software component. The attributes **property** and **value** can consist of ASCII characters and format specifiers.



  | 
    Parent Element | 
    Element Chain | 
  

  | 
    events | 
    elem_events | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    id | 
    16-bit event id (message and component number) value. See er_theory. | 
    xs:anySimpleType | 
    required | 
  

  | 
    level | 
    Event severance level (OP, API, Error, Detail) used for filtering. See er_theory. | 
    xs:anySimpleType | 
    required | 
  

  | 
    property | 
    value_output shown in the **Event** **Property** column of the \erecorder window. | 
    xs:string | 
    required | 
  

  | 
    value | 
    value_output shown in the **Value** column of the \erecorder window. | 
    xs:anySimpleType | 
    optional | 
  

  | 
    info | 
    Descriptive text with additional information (comment). | 
    xs:string | 
    optional | 
  

  | 
    doc | 
    Explicit link to documentation. | 
    xs:string | 
    optional | 
  

    | 
    handle | 
    Specifies the value that identifies the object handle and is used to associated the state information. This refers for example a RTOS thread or IP socket. | 
    xs:string | 
    optional | 
  

  | 
    hname | 
    Specifies a human readable name that represents the handle. This could be a thread name or a file name. A name can referenced in two different ways:\n
  hname=\"%N[_val_]\"   _val_ is the pointer value that addresses a const string in the address space of the target.\n
  hname=\"%S[_val_]\"   _val_ is the address of a symbol name (for example a function) in a loaded ELF image.
	 | 
    xs:string | 
    optional | 
  

  | 
    state | 
    Reference to a state name in the element \refelem{elem_group_component_state,state}. When state is specified, a handle value is required. | 
    xs:string | 
    optional | 
  

  | 
    tracking | 
    Specifies the tracking for an event handle wiht the values:\n
  tracking="Start"; start the state tracking for an event handle.\n
  tracking="Stop"; stop the state tracking for an event handle.\n
  tracking="Reset"; initialize the tracking for all event handles of that component to "Stop".
	 | 
    xs:string | 
    optional | 
  

    | 
    Child Element | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    \spref{elem_event_print,print} | 
    Use different output formats for single line output lines. See print_spec.  | 
    PrintType | 
    0..* | 
  


 
**Example:**
```
<events>
  :
  :
    <event id="0xA00" level="API"   property="InitEntry"                             info="Event on MyComp_initialize start"/>
    <event id="0xA01" level="API"   property="InitStatus"                            info="Event on MyComp_initialize return"/>
    <event id="0xA0A" level="Error" property="SendNoData"                            info="Event on MyComp_initialize return"/>
    <event id="0xA0B" level="Op"    property="SendComplete"    value="size=%d[val1]" info="Event on MyComp_send - completed"/>
    <event id="0xA0C" level="Error" property="SendFailed"      value=""              info="Event on MyComp_send - send failed"/>
    <event id="0xA15" level="Error" property="ReceiveNoData"   value=""              info="Event on MyComp_receive - no data received"/>
    <event id="0xA16" level="Op"    property="ReceiveComplete" value="size=%d[val1]" info="Event on MyComp_receive - completed"/>
    <event id="0xA17" level="Error" property="ReceiveFailed"   value=""              info="Event on MyComp_receive - receive failed"/>
</events>
```
