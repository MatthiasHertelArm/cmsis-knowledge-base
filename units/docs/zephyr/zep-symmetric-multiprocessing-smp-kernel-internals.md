---
id: "zep-symmetric-multiprocessing-smp-kernel-internals"
type: "concept"
domain: "rtos"
title: "Symmetric Multiprocessing: SMP Kernel Internals"
summary: "In general, Zephyr kernel code is SMP-agnostic and, like application code, will work correctly regardless of the number of CPUs available. But in a few areas there are notable changes in structure or behavior."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/smp/smp.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/smp/smp.rst"
license: "Apache-2.0"
mode: "V"
---

In general, Zephyr kernel code is SMP-agnostic and, like application
code, will work correctly regardless of the number of CPUs available.
But in a few areas there are notable changes in structure or behavior.



### Per-CPU data


Many elements of the core kernel data need to be implemented for each
CPU in SMP mode.  For example, the `_current` thread pointer obviously
needs to reflect what is running locally, there are many threads
running concurrently.  Likewise a kernel-provided interrupt stack
needs to be created and assigned for each physical CPU, as does the
interrupt nesting count used to detect ISR state.

These fields are now moved into a separate struct `_cpu` instance
within the `_kernel` struct, which has a `cpus[]` array indexed by ID.
Compatibility fields are provided for legacy uniprocessor code trying
to access the fields of `cpus[0]` using the older syntax and assembly
offsets.

Note that an important requirement on the architecture layer is that
the pointer to this CPU struct be available rapidly when in kernel
context.  The expectation is that `arch_curr_cpu` will be
implemented using a CPU-provided register or addressing mode that can
store this value across arbitrary context switches or interrupts and
make it available to any kernel-mode code.

Similarly, where on a uniprocessor system Zephyr could simply create a
global "idle thread" at the lowest priority, in SMP we may need one
for each CPU.  This makes the internal predicate test for "_is_idle()"
in the scheduler, which is a hot path performance environment, more
complicated than simply testing the thread pointer for equality with a
known static variable.  In SMP mode, idle threads are distinguished by
a separate field in the thread struct.


### Switch-based context switching


The traditional Zephyr context switch primitive has been `z_swap`.
Unfortunately, this function takes no argument specifying a thread to
switch to.  The expectation has always been that the scheduler has
already made its preemption decision when its state was last modified
and cached the resulting "next thread" pointer in a location where
architecture context switch primitives can find it via a simple struct
offset.  That technique will not work in SMP, because the other CPU
may have modified scheduler state since the current CPU last exited
the scheduler (for example: it might already be running that cached
thread!).

Instead, the SMP "switch to" decision needs to be made synchronously
with the swap call, and as we don't want per-architecture assembly
code to be handling scheduler internal state, Zephyr requires a
somewhat lower-level context switch primitives for SMP systems:
`arch_switch` is always called with interrupts masked, and takes
exactly two arguments.  The first is an opaque (architecture defined)
handle to the context to which it should switch, and the second is a
pointer to such a handle into which it should store the handle
resulting from the thread that is being switched out.
The kernel then implements a portable `z_swap` implementation on top
of this primitive which includes the relevant scheduler logic in a
location where the architecture doesn't need to understand it.

Similarly, on interrupt exit, switch-based architectures are expected
to call `z_get_next_switch_handle` to retrieve the next thread to
run from the scheduler. The argument to `z_get_next_switch_handle`
is either the interrupted thread's "handle" reflecting the same opaque type
used by `arch_switch`, or NULL if that thread cannot be released
to the scheduler just yet. The choice between a handle value or NULL
depends on the way CPU interrupt mode is implemented.

Architectures with a large CPU register file would typically preserve only
the caller-saved registers on the current thread's stack when interrupted
in order to minimize interrupt latency, and preserve the callee-saved
registers only when `arch_switch` is called to minimize context
switching latency. Such architectures must use NULL as the argument to
`z_get_next_switch_handle` to determine if there is a new thread
to schedule, and follow through with their own `arch_switch` or
derivative if so, or directly leave interrupt mode otherwise.
In the former case it is up to that switch code to store the handle
resulting from the thread that is being switched out in that thread's
"switch_handle" field after its context has fully been saved.

Architectures whose entry in interrupt mode already preserves the entire
thread state may pass that thread's handle directly to
`z_get_next_switch_handle` and be done in one step.

Note that while SMP requires `CONFIG_USE_SWITCH`, the reverse is not
true.  A uniprocessor architecture built with `CONFIG_SMP` set to No might
still decide to implement its context switching using
`arch_switch`.


### Thread Queue Ordering


When a thread is preempted by another thread of higher priority in an SMP
system, it is moved to the back of the queue for its priority level. In
contrast, on UP systems, a preempted thread does not move to the back of its
priority queue; it simply waits to regain the CPU, preserving its original
ordering relative to other threads of the same priority.
