---
id: "frb-8-resource-management-8-3-2-priority-inversion"
type: "concept"
domain: "rtos"
title: "8 Resource Management: 8.3 Mutexes (and Binary Semaphores) / 8.3.2 Priority Inversion"
summary: "Part of: 8.3 Mutexes (and Binary Semaphores)"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch08.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch08.md#8-3-2-priority-inversion"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 8.3 Mutexes (and Binary Semaphores)_

Figure 8.3 demonstrates one of the potential pitfalls of using a mutex to
provide mutual exclusion. The sequence of execution depicted shows the
higher priority Task 2 having to wait for the lower priority Task 1 to
give up control of the mutex. A higher priority task being delayed by a
lower priority task in this manner is called 'priority inversion'. This
undesirable behavior would be exaggerated further if a medium priority
task started to execute while the high priority task was waiting for the
semaphore—the result would be a high priority task waiting for a low
priority task—without the low priority task even being able to execute.
This is most often referred to as _unbounded priority inversion_ because
the medium priority task could block the low and high priority tasks
indefinitely.
This worst case scenario is shown in Figure 8.4.




* * *
   
***Figure 8.4*** *A worst case priority inversion scenario*
* * *

Priority inversion can be a significant problem, but in small embedded
systems it can often be avoided at system design time by considering
how resources are accessed.
