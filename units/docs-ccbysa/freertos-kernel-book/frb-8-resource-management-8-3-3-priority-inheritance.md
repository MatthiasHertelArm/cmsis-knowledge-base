---
id: "frb-8-resource-management-8-3-3-priority-inheritance"
type: "concept"
domain: "rtos"
title: "8 Resource Management: 8.3 Mutexes (and Binary Semaphores) / 8.3.3 Priority Inheritance"
summary: "Part of: 8.3 Mutexes (and Binary Semaphores)"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch08.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch08.md#8-3-3-priority-inheritance"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 8.3 Mutexes (and Binary Semaphores)_

FreeRTOS mutexes and binary semaphores are very similar—the difference
being that mutexes include a basic 'priority inheritance' mechanism,
whereas binary semaphores do not. Priority inheritance is a scheme that
minimizes the negative effects of priority inversion. It does not 'fix'
priority inversion, but merely lessens its impact by ensuring that the
inversion is always time bounded. However, priority inheritance
complicates system timing analysis, and it is not good practice to rely
on it for correct system operation.

Priority inheritance works by temporarily raising the priority of the
mutex holder to the priority of the highest priority task that is
attempting to obtain the same mutex. The low priority task that holds
the mutex 'inherits' the priority of the task waiting for the mutex.
This is demonstrated by Figure 8.5. The priority of the mutex holder is
reset automatically to its original value when it gives the mutex back.




* * *
   
***Figure 8.5*** *Priority inheritance minimizing the effect of priority inversion*
* * *

As just seen, priority inheritance functionality effects the priority of
tasks that are using the mutex. For that reason, mutexes must not be
used from interrupt service routines.

FreeRTOS implements a basic priority inheritance mechanism which was
designed with optimizing both space and execution cycles in mind. A full
priority inheritance mechanism requires significantly more data and
processor cycles to determine inherited priority at any moment,
especially when a task holds more than one mutex at a time.

Specific behaviors of the priority inheritance mechanism to keep in mind:
* A task can have its inherited priority raised further if it
  takes a mutex without first releasing mutexes it already holds.
* A task remains at its highest inherited priority until
  it has released all the mutexes it holds. This is regardless of
  the order the mutexes are released.
* A task will remain at the highest inherited priority if multiple
  mutexes are held regardless of tasks waiting on any of the held
  mutexes completing their wait (timing out).
