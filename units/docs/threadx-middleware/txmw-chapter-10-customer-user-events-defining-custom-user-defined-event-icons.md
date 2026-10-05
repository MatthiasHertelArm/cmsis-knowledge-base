---
id: "txmw-chapter-10-customer-user-events-defining-custom-user-defined-event-icons"
type: "concept"
domain: "trace"
title: "Chapter 10 - Customer user events: Defining Custom User-Defined Event Icons"
summary: "TraceX also provides the user the ability to create custom user-defined event icons and custom information field labels. This capability is achieved by adding event icon specifications to the tracex_custom.trxc configuration file."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter10.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter10.md#defining-custom-user-defined-event-icons"
license: "MIT"
mode: "V"
---

TraceX also provides the user the ability to create custom user-defined event icons and custom information field labels. This capability is achieved by adding event icon specifications to the ***tracex_custom.trxc*** configuration file. This file is located in the ***CustomEvents*** subdirectory of your user-defined TraceX installation directory. An example directory path is shown in Figure 30.

(figure: Screenshot of an example directory path.)
**FIGURE 30**

The ***tracex_custom.trxc*** custom event configuration file is a simple ASCII text file containing zero or more custom event definitions. The format of the file is as follows:

```c
//Comments
**Start **
[custom event definition(s)] **End **
```

Each line between Start and End is used to define a single custom event. TraceX provides a template version of this file with no custom events defined (nothing between the "Start" and "End" labels). The
format of a custom event definition is as follows:

**number, name, abbreviation, top_color, bottom_color, label1, label2, label2, label4**

where:

- number: Defines the user-defined event number, between 4096 and 65535, inclusive. | 
- name: Defines the logical name for the user-defined event. | 
- abbreviation: Defines the two-letter user-defined event abbreviation. | 
- top_color: Defines the RGB value for the top-half of the icon, which is a three-digit number in parenthesis. Some typical 
  RGB definitions are
  - BLACK = (0,0,0)       
  - WHITE = (255,255,255)
  - RED = (255,0,0)     
  - GREEN = (0,255,0)     
  - BLUE = (0,0,255)     
  - YELLOW = (255,255,0)   
  - CYAN = (0,255,255)   
  - MAGENTA = (255,0,255)   
  Using the RBG specification gives the user a broad range of colors for each user-defined icon. For more information on RBG color definition, see: https://en.wikipedia.org/wiki/RGB#Digital_representations
- bottom_color: Defines the RGB value for the bottom half of the icon, which is a three-digit number in parenthesis.
- label1: Label for ***info_field_1***, as specified in the ***tx_trace_user_event_insert*** call.
- label2: Label for ***info_field_2***, as specified in the ***tx_trace_user_event_insert*** call.
- label3: Label for ***info_field_3***, as specified in the ***tx_trace_user_event_insert*** call.
- label4: Label for ***info_field_4***, as specified in the ***tx_trace_user_event_insert*** call.

Example definitions for each of the two user-defined events used in this chapter are shown in Figure 10.4. The first definition is for event 4096 at line 5 of the ***tracex_custom.trxc*** file. This definition gives user-defined event 4096 the name **First_User_Event**, specifies a two-letter abbreviation of **FE**, makes the top portion of the icon red, the bottom portion of the icon green, and names the information fields as **First_Info1**, **First_Info2**, **First_Info3**, and **First_Info4**. User-defined event 4098 is defined similarly at line 6 of ***tracex_custom.trxc***.

(figure: Screenshot of the example definitions for the user-defined events.)
**FIGURE 31**

Since the ***tracex_custom.trxc*** file is read by TraceX during initialization, TraceX must be exited and restarted before the custom icon definitions can take effect. Figure 32 shows the TraceX display of user-defined events 452 and 453 with the custom event icons defined in ***tracex_custom.trxc***.

(figure: Screenshot of the TraceX display of user defined events with the custom event icons.)
**FIGURE 32**

The additional information in the custom event definition is shown when the event you select using a double-click, mouse-over, or clicking the current event button. Figure 33 shows the double-click selection on event 452. The event name and information fields all match the sample definition that was added to ***tracex_custom.trxc***.

(figure: Screenshot of the double-click selection on an event.)
**FIGURE 33**
