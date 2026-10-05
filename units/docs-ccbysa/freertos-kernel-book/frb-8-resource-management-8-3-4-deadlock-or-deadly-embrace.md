---
id: "frb-8-resource-management-8-3-4-deadlock-or-deadly-embrace"
type: "concept"
domain: "rtos"
title: "8 Resource Management: 8.3 Mutexes (and Binary Semaphores) / 8.3.4 Deadlock (or Deadly Embrace)"
summary: "Part of: 8.3 Mutexes (and Binary Semaphores)"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch08.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch08.md#8-3-4-deadlock-or-deadly-embrace"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 8.3 Mutexes (and Binary Semaphores)_

'Deadlock' is another potential pitfall of using mutexes for mutual
exclusion. Deadlock is sometimes also known by the more dramatic name
'deadly embrace'.

Deadlock occurs when two tasks cannot proceed because they are both
waiting for a resource that is held by the other. Consider the following
scenario where Task A and Task B both need to acquire mutex X *and*
mutex Y in order to perform an action:

1. Task A executes and successfully takes mutex X.

2. Task A is pre-empted by Task B.

3. Task B successfully takes mutex Y before attempting to also take
   mutex X—but mutex X is held by Task A so is not available to Task B.
   Task B opts to enter the Blocked state to wait for mutex X to be
   released.

4. Task A continues executing. It attempts to take mutex Y—but mutex Y
   is held by Task B, so is not available to Task A. Task A opts to
   enter the Blocked state to wait for mutex Y to be released.

At the end of this scenario, Task A is waiting for a mutex held by Task
B, and Task B is waiting for a mutex held by Task A. Deadlock has
occurred because neither task can proceed.

As with priority inversion, the best method of avoiding deadlock is to
consider its potential at design time, and design the system to ensure
that deadlock cannot occur. In particular, and as previously stated in
this book, it is normally bad practice for a task to wait indefinitely
(without a time out) to obtain a mutex. Instead, use a time out that is
a little longer than the maximum time it is expected to have to wait for
the mutex—then failure to obtain the mutex within that time will be a
symptom of a design error, which might be a deadlock.

In practice, deadlock is not a big problem in small embedded systems,
because the system designers can have a good understanding of the entire
application, and so can identify and remove the areas where it could
occur.
