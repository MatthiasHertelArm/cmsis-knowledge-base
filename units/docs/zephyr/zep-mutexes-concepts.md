---
id: "zep-mutexes-concepts"
type: "concept"
domain: "rtos"
title: "Mutexes: Concepts"
summary: "Any number of mutexes can be defined (limited only by available RAM). Each mutex is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/synchronization/mutexes.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/synchronization/mutexes.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of mutexes can be defined (limited only by available RAM). Each mutex
is referenced by its memory address.

A mutex has the following key properties:

* A **lock count** that indicates the number of times the mutex has been locked
  by the thread that has locked it. A count of zero indicates that the mutex
  is unlocked.

* An **owning thread** that identifies the thread that has locked the mutex,
  when it is locked.

A mutex must be initialized before it can be used. This sets its lock count
to zero.

A thread that needs to use a shared resource must first gain exclusive rights
to access it by **locking** the associated mutex. If the mutex is already locked
by another thread, the requesting thread may choose to wait for the mutex
to be unlocked.

After locking a mutex, the thread may safely use the associated resource
for as long as needed; however, it is considered good practice to hold the lock
for as short a time as possible to avoid negatively impacting other threads
that want to use the resource. When the thread no longer needs the resource
it must **unlock** the mutex to allow other threads to use the resource.

A mutex must not be freed, or have its memory reused, while it is locked
or while threads are waiting on it. A mutex embedded in a dynamically
allocated object must be unlocked before that object is released;
otherwise the owning thread is left tracking a mutex in memory that no
longer belongs to it.

Any number of threads may wait on a locked mutex simultaneously.
When the mutex becomes unlocked it is then locked by the highest-priority
thread that has waited the longest.


**Note:** Mutex objects are *not* designed for use by ISRs.


### Reentrant Locking


A thread is permitted to lock a mutex it has already locked.
This allows the thread to access the associated resource at a point
in its execution when the mutex may or may not already be locked.

A mutex that is repeatedly locked by a thread must be unlocked an equal number
of times before the mutex becomes fully unlocked so it can be claimed
by another thread.


### Priority Inheritance


The thread that has locked a mutex is eligible for `priority inheritance`.
This means the kernel will *temporarily* elevate the thread's priority
if a higher priority thread begins waiting on the mutex. This allows the owning
thread to complete its work and release the mutex more rapidly by executing
at the same priority as the waiting thread. Once the mutex has been unlocked,
the unlocking thread resets its priority to the level it had before locking
that mutex.


**Note:** The `CONFIG_PRIORITY_CEILING` configuration option limits how high the kernel can raise a thread's priority due to priority inheritance. The default value of -128 permits unlimited. Setting this to a priority level that is at or lower than the priority of the idle thread disables it.

A thread's priority prior to any mutex-related boost is saved on the thread
itself the first time it is raised, and each mutex it holds is tracked in a
per-thread list. Each time a higher priority thread waits on a mutex, the
kernel adjusts the owning thread's priority. When the owning thread releases
a lock (or if the high priority waiting thread times out), the kernel
rescans the thread's remaining held mutexes and recalculates its priority
from the highest-priority waiter still pending on any of them, falling back
to the thread's original priority if none remain. This gives correct
results regardless of the order in which held mutexes are unlocked.

If the owner of a mutex is itself blocked waiting on another mutex, a
priority boost is propagated along that ownership chain so that every
thread blocking progress towards the waiter is raised in turn, up to an
implementation-defined limit on the number of chain hops walked per lock
attempt. Owners beyond that limit keep their pre-boost priority until a
later lock attempt walks the chain again.
