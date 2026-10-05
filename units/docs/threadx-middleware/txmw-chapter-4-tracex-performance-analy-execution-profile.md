---
id: "txmw-chapter-4-tracex-performance-analy-execution-profile"
type: "concept"
domain: "trace"
title: "Chapter 4 - TraceX performance analysis: Execution Profile"
summary: "Selecting the Generate Execution Profile button or View -Execution Profile presents the TraceX execution profile for the currently loaded trace file. The execution profile associated with the sample ThreadX demonstration trace is shown in Figure 19."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter4.md#execution-profile"
license: "MIT"
mode: "V"
---

Selecting the ***Generate Execution Profile*** button or ***View -Execution Profile*** presents the TraceX execution profile for the currently loaded trace file. The execution profile associated with the sample ThreadX demonstration trace is shown in **Figure 19**.

(figure: Screenshot of the execution profile associated with the sample ThreadX demonstration trace.)

**FIGURE 19**

The example shown in **Figure 19** indicates that nearly 45% of the processing time is inside of ***thread 2*** and nearly 51% of the processing time is inside of ***thread 1*** This is logical since the bulk of the trace shows these threads sending and receiving messages. The remaining execution contexts have only a small amount of execution time in this example.
