---
id: "zep-threads-lifecycle"
type: "concept"
domain: "rtos"
title: "Threads: Lifecycle"
summary: "A thread must be created before it can be used. The kernel initializes the thread control block as well as one end of the stack portion. The remainder of the thread's stack is typically left uninitialized."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/index.rst"
license: "Apache-2.0"
mode: "V"
---

### Thread Creation


A thread must be created before it can be used. The kernel initializes
the thread control block as well as one end of the stack portion. The remainder
of the thread's stack is typically left uninitialized.

Specifying a start delay of `K_NO_WAIT` instructs the kernel
to start thread execution immediately. Alternatively, the kernel can be
instructed to delay execution of the thread by specifying a timeout
value -- for example, to allow device hardware used by the thread
to become available.

The kernel allows a delayed start to be canceled before the thread begins
executing. A cancellation request has no effect if the thread has already
started. A thread whose delayed start was successfully canceled must be
re-spawned before it can be used.


### Starting a Thread


A thread that is created with `K_FOREVER` as its start delay is not
added to the scheduler's ready queue and does not begin executing until it is
explicitly started. The `k_thread_start` function starts such an
inactive thread, making it eligible for scheduling. Starting a thread that has
already started has no effect.

This is useful when a thread object must be created at one point in time but its
execution deferred until the application has completed additional setup.


### Thread Termination


Once a thread is started it typically executes forever. However, a thread may
synchronously end its execution by returning from its entry point function.
This is known as **termination**.

A thread that terminates is responsible for releasing any shared resources
it may own (such as mutexes and dynamically allocated memory)
prior to returning, since the kernel does *not* reclaim them automatically.

In some cases a thread may want to sleep until another thread terminates.
This can be accomplished with the `k_thread_join` API. This
will block the calling thread until either the timeout expires, the target
thread self-exits, or the target thread aborts (either due to a
`k_thread_abort` call or triggering a fatal error).

Once a thread has terminated, the kernel guarantees that no use will
be made of the thread struct.  The memory of such a struct can then be
reused for any purpose, including spawning a new thread.  Note that
the thread must be fully terminated, which presents race conditions
where a thread's own logic signals completion which is seen by another
thread before the kernel processing is complete.  Under normal
circumstances, application code should use `k_thread_join` or
`k_thread_abort` to synchronize on thread termination state
and not rely on signaling from within application logic.


### Thread Aborting


A thread may asynchronously end its execution by **aborting**. The kernel
automatically aborts a thread if the thread triggers a fatal error condition,
such as dereferencing a null pointer.

A thread can also be aborted by another thread (or by itself)
by calling `k_thread_abort`. However, it is typically preferable
to signal a thread to terminate itself gracefully, rather than aborting it.

As with thread termination, the kernel does not reclaim shared resources
owned by an aborted thread.


**Note:** The kernel does not currently make any claims regarding an application's ability to respawn a thread that aborts.


### Thread Suspension


A thread can be prevented from executing for an indefinite period of time
if it becomes **suspended**. The function `k_thread_suspend`
can be used to suspend any thread, including the calling thread.
Suspending a thread that is already suspended has no additional effect.

Once suspended, a thread cannot be scheduled until another thread calls
`k_thread_resume` to remove the suspension.


**Note:** A thread can prevent itself from executing for a specified period of time using `k_sleep`. However, this is different from suspending a thread since a sleeping thread becomes executable automatically when the time limit is reached.
