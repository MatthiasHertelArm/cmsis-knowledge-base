---
id: "rtos2-mutex-management"
type: "concept"
domain: "rtos"
title: "Mutex Management"
summary: "Synchronize resource access using Mutual Exclusion (Mutex)."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
license: "Apache-2.0"
mode: "V"
---

Synchronize resource access using Mutual Exclusion (Mutex).
 
**Mutual exclusion** (widely known as **Mutex)** is used in various operating systems for resource management. Many
resources in a microcontroller device can be used repeatedly, but only by one thread at a time (for example communication
channels, memory, and files). Mutexes are used to protect access to a shared resource. A mutex is created and then passed
between the threads (they can acquire and release the mutex).

" "CMSIS-RTOS Mutex"

A mutex is a special version of a semaphore. Like the semaphore, it is a container for
tokens. But instead of being able to have multiple tokens, a mutex can only carry one (representing the resource). Thus, a
mutex token is binary and bounded, i.e. it is either **available,** or **blocked** by a owning thread. The advantage of a
mutex is that it introduces thread ownership. When a thread acquires a mutex and becomes its owner, subsequent mutex acquires
from that thread will succeed immediately without any latency (if osMutexRecursive is specified). Thus, mutex acquires/releases
can be nested.

" "CMSIS-RTOS Mutex States"

**Note:** Mutex management functions cannot be called from Interrupt Service Routines (ISR), unlike a
binary semaphore that can be released from an ISR.
