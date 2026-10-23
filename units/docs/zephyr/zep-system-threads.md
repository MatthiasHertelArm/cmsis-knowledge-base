---
id: "zep-system-threads"
type: "concept"
domain: "rtos"
title: "System Threads"
summary: "A system thread is a thread that the kernel spawns automatically during system initialization."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/threads/system_threads.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/threads/system_threads.rst"
license: "Apache-2.0"
mode: "V"
---

A `system thread` is a thread that the kernel spawns automatically
during system initialization.

The kernel spawns the following system threads:

**Main thread**
    This thread performs kernel initialization, then calls the application's
    `main` function (if one is defined).

    By default, the main thread uses the highest configured preemptible thread
    priority (i.e. 0). If the kernel is not configured to support preemptible
    threads, the main thread uses the lowest configured cooperative thread
    priority (i.e. -1).

    The main thread is an essential thread while it is performing kernel
    initialization or executing the application's `main` function;
    this means a fatal system error is raised if the thread aborts. If
    `main` is not defined, or if it executes and then does a normal
    return, the main thread terminates normally and no error is raised.

**Idle thread**
    This thread executes when there is no other work for the system to do.
    If possible, the idle thread activates the board's power management support
    to save power; otherwise, the idle thread simply performs a "do nothing"
    loop. The idle thread remains in existence as long as the system is running
    and never terminates.

    The idle thread always uses the lowest configured thread priority.

    The idle thread is an essential thread, which means a fatal system error
    is raised if the thread aborts.

Additional system threads may also be spawned, depending on the kernel
and board configuration options specified by the application. For example,
enabling the system workqueue spawns a system thread
that services the work items submitted to it. (See workqueues_v2.)
