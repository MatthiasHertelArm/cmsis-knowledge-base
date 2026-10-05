---
id: "txmw-chapter-4-tracex-performance-analy-popular-services"
type: "concept"
domain: "trace"
title: "Chapter 4 - TraceX performance analysis: Popular Services"
summary: "Selecting View ->Popular Services presents the popular services in the currently loaded trace file. By default, this information is displayed for the entire system. However, the popular services for specific threads are also available."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter4.md#popular-services"
license: "MIT"
mode: "V"
---

Selecting ***View ->Popular Services*** presents the popular services in the currently loaded trace file. By default, this information is displayed for the entire system. However, the popular services for specific threads are also available. The popular services in the sample ThreadX demonstration trace are shown in **Figure 20**.

(figure: Screenshot of the popular services in the sample ThreadX demonstration trace.)

**FIGURE 20**

The example shown in **Figure 20** indicates that ***tx_queue_send*** and ***tx_queue_receive*** are the two most popular services in this trace. This is consistent with the behavior of the standard ThreadX demonstration from which this trace was captured.

Specific threads can be selected for this analysis by using the drop down selection list at the top of this window. **Figure 21** shows this analysis for ***thread 3***.

(figure: Screenshot of the analysis for a TraceX popular services.)

**FIGURE 21**
