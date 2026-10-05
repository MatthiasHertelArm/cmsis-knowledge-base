---
id: "frb-8-resource-management-8-3-mutexes-and-binary-semaphores"
type: "concept"
domain: "rtos"
title: "8 Resource Management: 8.3 Mutexes (and Binary Semaphores)"
summary: "A Mutex is a special type of binary semaphore that is used to control access to a resource that is shared between two or more tasks. The word MUTEX originates from 'MUTual EXclusion'."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch08.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch08.md#8-3-mutexes-and-binary-semaphores"
license: "CC-BY-SA-4.0"
mode: "V"
---

A Mutex is a special type of binary semaphore that is used to control
access to a resource that is shared between two or more tasks. The word
MUTEX originates from 'MUTual EXclusion'. `configUSE_MUTEXES` must be set
to 1 in FreeRTOSConfig.h for mutexes to be available.

When used in a mutual exclusion scenario, the mutex can be thought of as
a token that is associated with the resource being shared. For a task to
access the resource legitimately, it must first successfully 'take' the
token (be the token holder). When the token holder has finished with the
resource, it must 'give' the token back. Only when the token has been
returned can another task successfully take the token, and then safely
access the same shared resource. A task is not permitted to access the
shared resource unless it holds the token. This mechanism is shown in
Figure 8.1.

Even though mutexes and binary semaphores share many characteristics,
the scenario shown in Figure 8.1 (where a mutex is used for mutual
exclusion) is completely different to that shown in Figure 7.6 (where a
binary semaphore is used for synchronization). The primary difference is
what happens to the semaphore after it has been obtained:

- A semaphore that is used for mutual exclusion must always be
  returned.
- A semaphore that is used for synchronization is normally discarded
  and not returned.




* * *
   
***Figure 8.1*** *Mutual exclusion implemented using a mutex*
* * *

The mechanism works purely through the discipline of the application
writer. There is no reason why a task cannot access the resource at any
time, but each task 'agrees' not to do so, unless it is able to become
the mutex holder.
