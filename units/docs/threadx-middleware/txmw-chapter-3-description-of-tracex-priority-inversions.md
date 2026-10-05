---
id: "txmw-chapter-3-description-of-tracex-priority-inversions"
type: "concept"
domain: "trace"
title: "Chapter 3 - Description of TraceX: Priority Inversions"
summary: "TraceX automatically displays priority inversions detected in the trace file. Priority inversions are defined as conditions where a higher-priority thread is blocked trying to obtain a mutex that is currently owned by a lower-priority thread."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter3.md#priority-inversions"
license: "MIT"
mode: "V"
---

TraceX automatically displays priority inversions detected in the trace file. Priority inversions are defined as conditions where a higher-priority thread is blocked trying to obtain a mutex that is currently owned by a lower-priority thread. This condition is termed *deterministic*, because the system was set up to operate in this manner. To inform the user, TraceX shows *deterministic* priority inversion ranges as a light salmon color.

TraceX also displays *non-deterministic* priority inversions. These priority inversions differ from the *deterministic* priority inversions in that another thread of a different priority level has executed in the middle of what was a *deterministic* priority inversion, thereby making the time within the priority inversion somewhat *non-deterministic*. This condition is often unknown to the user and can be very serious. In order to alert the user of this condition, TraceX shows *non-deterministic* priority inversions as a brighter salmon color. **Figure 18** shows both *deterministic* and *non-deterministic* priority inversions.

(figure: Screenshot of the priority inversion in a trace file.)

**FIGURE 18**

**Figure 18** shows a *deterministic* priority inversion from event 398 through event 402. In this range, the higher-priority ***thread 0*** blocks on a mutex owned by a lower-priority ***thread 1***. At event 402, ***thread 1*** releases the mutex and thus ends the priority
inversion.

The brighter shaded area shows a *non-deterministic* priority inversion between event 408 through event 420. What makes this *non-deterministic* is that while ***thread 1*** holds the mutex that higher-priority ***thread 0*** is blocked on, an interrupt occurs that resumes ***thread 2***, which then executes and lengthens the time the system is in priority inversion. This condition can be quite serious and difficult to identify; however, with TraceX it is easily identified.
