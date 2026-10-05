---
id: "threadx-chapter-1-introduction-to-threadx-embedded-applications"
type: "concept"
domain: "rtos"
title: "Chapter 1 - Introduction to ThreadX: Embedded Applications"
summary: "Embedded applications execute on microprocessors buried within products such as wireless communication devices, automobile engines, laser printers, medical devices, etc. Another distinction of embedded applications is that their software and hardware have a dedicated purpose."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter1.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter1.md#embedded-applications"
license: "MIT"
mode: "V"
---

Embedded applications execute on microprocessors buried within products such as wireless communication devices, automobile engines, laser printers, medical devices, etc. Another distinction of embedded applications is that their software and hardware have a dedicated purpose.

### Real-time Software

When time constraints are imposed on the application software, it is called the _real-time_ software. Embedded applications are almost always real-time because of their inherent interaction with external events.

### Multitasking

As mentioned, embedded applications have a dedicated purpose. To fulfill this purpose, the software must perform a variety of _tasks_. A task is a semi-independent portion of the
application that carries out a specific duty. It is also the case that some tasks are more important than others. One of the major difficulties in an embedded application is the allocation of the processor between the various application tasks. This allocation of processing between competing tasks is the primary purpose of ThreadX.

### Tasks vs. Threads

Another distinction about tasks is that the term _task_ is used in a variety of ways. It sometimes means a separately loadable program. In other instances, it may refer to an
internal program segment. Therefore, in contemporary operating systems, there are two terms that more or less replace the use of task: _process_ and _thread_. A _process_ is a completely independent program that has its own address space, while a _thread_ is a semi-independent program segment that executes within a process. Threads share the same process address space. The overhead associated with thread management is minimal.

Most embedded applications cannot afford the overhead (both memory and performance) associated with a full-blown process-oriented operating system. In addition, smaller microprocessors don't have the hardware architecture to support a true process-oriented operating system. For these reasons, ThreadX implements a thread model, which is both extremely efficient and practical for most real-time embedded applications.

To avoid confusion, ThreadX does not use the term _task_. Instead, the more descriptive and contemporary name _thread_ is used.
