---
id: "zep-scheduling-concepts"
type: "concept"
domain: "rtos"
title: "Scheduling: Concepts"
summary: "The scheduler determines which thread is allowed to execute at any point in time; this thread is known as the current thread."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

The scheduler determines which thread is allowed to execute
at any point in time; this thread is known as the **current thread**.

There are various points in time when the scheduler is given an
opportunity to change the identity of the current thread, meaning
when the scheduler switches the CPU's execution from one thread
to another. These points are called **reschedule points**.
Some potential reschedule points are:

- transition of a thread from running state to a suspended or waiting
  state, for example by `k_sem_take` or `k_sleep`.
- transition of a thread to the ready state, for
  example by `k_sem_give` or `k_thread_start`
- return to thread context after processing an interrupt
- when a running thread invokes `k_yield`

A thread **sleeps** when it voluntarily initiates an operation that
transitions itself to a suspended or waiting state.

Whenever the scheduler changes the identity of the current thread,
or when execution of the current thread is replaced by an ISR,
the kernel first saves the current thread's CPU register values.
These register values get restored when the thread later resumes execution.
