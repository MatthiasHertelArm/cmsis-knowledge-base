---
id: "txmw-chapter-4-tracex-performance-analy-performance-statistics"
type: "concept"
domain: "trace"
title: "Chapter 4 - TraceX performance analysis: Performance Statistics"
summary: "Selecting the Generate Performance Statistics button or View -> Performance Statistics presents the performance statistics of the currently loaded trace file. By default, this information is displayed for the entire system."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter4.md#performance-statistics"
license: "MIT"
mode: "V"
---

Selecting the ***Generate Performance Statistics*** button or ***View -> Performance Statistics*** presents the performance statistics of the currently loaded trace file. By default, this information is displayed for the entire system. However, the performance statistics are also available for each specific thread.

The performance statistics of the sample ThreadX demonstration trace are shown in **Figure 23**.

(figure: Screenshot of the TraceX performance statistics.)

**FIGURE 23**

The example shown in **Figure 23** indicates that there were 18 context switches in this trace file, as well as five thread preemptions, 16 thread suspensions, 19 thread resumptions, and three interrupts. There were no priority inversions found in this trace file. Notice there are two categories of priority inversions, namely, *deterministic* and *nondeterministic*. Deterministic priority inversions are priority inversion in which a thread is blocked on a mutex owned by a lower priority thread. An nondeterministic priority inversion is where a different lower priority thread runs during a deterministic priority inversion. The later can cause unforeseen timing behavior in the application and should be studied carefully.
