---
id: "zep-workqueue-threads-system-workqueue"
type: "concept"
domain: "rtos"
title: "Workqueue Threads: System Workqueue"
summary: "The kernel defines a workqueue known as the system workqueue, which is available to any application or kernel code that requires workqueue support. The system workqueue is optional, and only exists if the application makes use of it."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/workqueue.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/workqueue.rst"
license: "Apache-2.0"
mode: "V"
---

The kernel defines a workqueue known as the *system workqueue*, which is
available to any application or kernel code that requires workqueue support.
The system workqueue is optional, and only exists if the application makes
use of it.


**Important:** Additional workqueues should only be defined when it is not possible to submit new work items to the system workqueue, since each new workqueue incurs a significant cost in memory footprint. A new workqueue can be justified if it is not possible for its work items to co-exist with existing system workqueue work items without an unacceptable impact; for example, if the new work items perform blocking operations that would delay other system workqueue processing to an unacceptable degree. Also note: The system workqueue has the lowest cooperative priority by default. This means that draining the system workqueue takes precedence over *all preemptible threads*. Configuring the system workqueue's priority to be preemptible is risky, because subsystems and drivers may implicitly rely on work items being executed in a cooperative context. Therefore, a separate workqueue with lower priority may be appropriate for low-priority tasks.
