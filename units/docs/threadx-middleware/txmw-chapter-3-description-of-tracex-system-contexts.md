---
id: "txmw-chapter-3-description-of-tracex-system-contexts"
type: "concept"
domain: "trace"
title: "Chapter 3 - Description of TraceX: System Contexts"
summary: "TraceX lists the system contexts on the left-hand side of the display, as shown in Figure 11. Events that occur in a particular context are displayed on the horizontal line to the right of that context."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter3.md#system-contexts"
license: "MIT"
mode: "V"
---

TraceX lists the system contexts on the left-hand side of the display, as shown in **Figure 11**. Events that occur in a particular context are displayed on the horizontal line to the right of that context. In this way, you can easily ascertain which context the event occurred as well as follow that context line to see all the events that occurred in a particular context.

The first tow context entries are always the ***Interrupt*** and ***Initialize/Idle*** contexts. ***Interrupt*** context represents all system events made from Interrupt Service Routines (IRS). ***Initialize/Idle*** context represents two contexts in ThreadX. Events that occur during ***tx_application_define***, are ***Initialize/Idle*** context. If the system is idle and thus no events are occurring, the green bar representing ***Running*** in the time view is drawn on the ***Initialize/Idle*** context.

(figure: Screenshot of the system contexts on the left-hand side of the display.)

**FIGURE 11**

In the example in **Figure 11**, there are nine thread contexts, starting from the ***System Timer Thread*** context. Additional information about an individual context is available by placing the mouse on that context. The additional information includes the thread's starting stack address, ending stack address, total size, percent used, relative execution percentage, number of suspension, resumptions, and its highest and lowest priority during the trace. **Figure 12** shows information for ***thread 0***.

(figure: Screenshot of the information for thread 0.)


**FIGURE 12**

Contexts may also be moved to group those of greater interest. This is accomplished by dragging and dropping the context or right-clicking on the context. Right-clicking on the context yields a dialog for moving the context to the top or the bottom. 

Selecting ***Move to top*** results in the ***thread 3*** context being moved to the top of the context list, as shown in **Figure 13**.

(figure: Screenshot of the context being moved to the top of the context list.)


**FIGURE 13**
