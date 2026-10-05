---
id: "frb-7-interrupt-management-7-4-binary-semaphores-used-for-synchroni"
type: "concept"
domain: "rtos"
title: "7 Interrupt Management: 7.4 Binary Semaphores Used for Synchronization"
summary: "The interrupt safe version of the Binary Semaphore API can be used to unblock a task each time a particular interrupt occurs, effectively synchronizing the task with the interrupt."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch07.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch07.md#7-4-binary-semaphores-used-for-synchronization"
license: "CC-BY-SA-4.0"
mode: "V"
---

The interrupt safe version of the Binary Semaphore API can be used to
unblock a task each time a particular interrupt occurs, effectively
synchronizing the task with the interrupt. This allows the majority of
the interrupt event processing to be implemented within the synchronized
task, with only a very fast and short portion remaining directly in the
ISR. As described in the previous section, the binary semaphore is used
to 'defer' interrupt processing to a task[^14].

[^14]: It is more efficient to unblock a task from an interrupt using a
direct to task notification than it is using a binary semaphore.
Direct to task notifications are not covered until Chapter 10, Task
Notifications.

As previously demonstrated in Figure 7.1, if the interrupt processing is
particularly time critical, then the priority of the deferred processing
task can be set to ensure the task always pre-empts the other tasks in
the system. The ISR can then be implemented to include a call to
`portYIELD_FROM_ISR()`, ensuring the ISR returns directly to the task to
which interrupt processing is being deferred. This has the effect of
ensuring the entire event processing executes contiguously (without a
break) in time, just as if it had all been implemented within the ISR
itself. Figure 7.2 repeats the scenario shown in Figure 7.1, but with the
text updated to describe how the execution of the deferred processing
task can be controlled using a semaphore.




* * *

***Figure 7.2*** *Using a binary semaphore to implement deferred interrupt processing*
* * *

The deferred processing task uses a blocking 'take' call to a semaphore
as a means of entering the Blocked state to wait for the event to occur.
When the event occurs, the ISR uses a 'give' operation on the same
semaphore to unblock the task so that the required event processing can
proceed.

'Taking a semaphore' and 'giving a semaphore' are concepts that have
different meanings depending on their usage scenario. In this interrupt
synchronization scenario, the binary semaphore can be considered
conceptually as a queue with a length of one. The queue can contain a
maximum of one item at any time, so is always either empty or full
(hence, binary). By calling `xSemaphoreTake()`, the task to which
interrupt processing is deferred effectively attempts to read from the
queue with a block time, causing the task to enter the Blocked state if
the queue is empty. When the event occurs, the ISR uses the
`xSemaphoreGiveFromISR()` function to place a token (the semaphore) into
the queue, making the queue full. This causes the task to exit the
Blocked state and remove the token, leaving the queue empty once more.
When the task has completed its processing, it once more attempts to
read from the queue and, finding the queue empty, re-enters the Blocked
state to wait for the next event. This sequence is demonstrated in
Figure 7.3.

Figure 7.3 shows the interrupt 'giving' the semaphore, even though it has
not first 'taken' it, and the task 'taking' the semaphore, but never
giving it back. This is why the scenario is described as being
conceptually similar to writing to and reading from a queue. It often
causes confusion as it does not follow the same rules as other semaphore
usage scenarios, where a task that takes a semaphore must always give it
back—such as the scenarios described in Chapter 8, Resource Management.




* * *

***Figure 7.3*** *Using a binary semaphore to synchronize a task with an interrupt*
* * *
