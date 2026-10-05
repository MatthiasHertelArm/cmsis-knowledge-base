---
id: "threadx-chapter-6-demonstration-system-for-overview"
type: "concept"
domain: "rtos"
title: "Chapter 6 - Demonstration System for ThreadX: Overview"
summary: "Each ThreadX product distribution contains a demonstration system that runs on all supported microprocessors."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter6.md#overview"
license: "MIT"
mode: "V"
---

Each ThreadX product distribution contains a demonstration system that
runs on all supported microprocessors.

This example system is defined in the distribution file
***demo_threadx.c*** and is designed to illustrate how ThreadX is
used in an embedded multithread environment. The demonstration
consists of initialization, eight threads, one byte pool, one block
pool, one queue, one semaphore, one mutex, and one event flags group.

> **Note:** *Except for the thread's stack size, the demonstration application is
identical on all ThreadX supported processors.*

The complete listing of
***demo_threadx.c***, including the line numbers referenced
throughout the remainder of this chapter.
