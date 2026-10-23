---
id: "zep-scheduling-querying-preemptibility"
type: "concept"
domain: "rtos"
title: "Scheduling: Concepts / Querying Preemptibility"
summary: "Code whose behavior depends on whether it can be preempted can query the current context with k_is_preempt_thread."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Concepts_

Code whose behavior depends on whether it can be preempted can query the current
context with `k_is_preempt_thread`. This returns a non-zero value only
when the caller is a thread (not an ISR), the thread's priority is in the
preemptible range, and the thread has not locked the scheduler.

The related `k_can_yield` routine reports whether the current context is
able to yield or invoke blocking APIs at all. It returns false in contexts such
as ISRs, the pre-kernel initialization phase, or the idle thread, where yielding
is not possible.
