---
id: "zep-workqueue-threads-suggested-uses"
type: "concept"
domain: "rtos"
title: "Workqueue Threads: Suggested Uses"
summary: "Use the system workqueue to defer complex interrupt-related processing from an ISR to a shared thread."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/workqueue.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/workqueue.rst"
license: "Apache-2.0"
mode: "V"
---

Use the system workqueue to defer complex interrupt-related processing from an
ISR to a shared thread. This allows the interrupt-related processing to be
done promptly without compromising the system's ability to respond to
subsequent interrupts, and does not require the application to define and
manage an additional thread to do the processing.
