---
id: "threadx-chapter-3-functional-components-of-priority-inheritance"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Thread Execution / Priority Inheritance"
summary: "ThreadX also supports optional priority inheritance within its mutex services described later in this chapter."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#priority-inheritance"
license: "MIT"
mode: "V"
---

_Part of: Thread Execution_

ThreadX also supports optional priority inheritance within its mutex services described later in this chapter. Priority inheritance allows a lower priority thread to temporarily assume the priority of a high priority thread that is waiting for a mutex owned by the lower priority thread. This capability helps the application to avoid nondeterministic priority inversion by eliminating preemption of intermediate thread priorities. Of course, *preemption-threshold* may be used to achieve a similar result.
