---
id: "rtx-tutorial-inter-thread-communication"
type: "concept"
domain: "rtos"
title: "tutorial: Inter-thread Communication"
summary: "So far, we have seen how application code can be defined as independent threads and how we can access the timing services provided by the RTOS."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#inter-thread-communication"
license: "Apache-2.0"
mode: "V"
---

So far, we have seen how application code can be defined as independent threads and how we can access the timing services
provided by the RTOS. In a real application, we need to be able to communicate between threads in order to make an
application useful. To this end, a typical RTOS supports several different communication objects which can be used to link
the threads together to form a meaningful program. The CMSIS-RTOS2 API supports inter-thread communication with thread and
event flags, semaphores, mutexes, mailboxes and message queues. In the first section, the key concept was concurrency. In
this section, the key concept is synchronizing the activity of multiple threads.
