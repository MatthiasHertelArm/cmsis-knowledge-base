---
id: "zep-symmetric-multiprocessing-interprocessor-interrupts"
type: "concept"
domain: "rtos"
title: "Symmetric Multiprocessing: Interprocessor Interrupts"
summary: "When running in multiprocessor environments, it is occasionally the case that state modified on the local CPU needs to be synchronously handled on a different processor."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/smp/smp.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/smp/smp.rst"
license: "Apache-2.0"
mode: "V"
---

When running in multiprocessor environments, it is occasionally the
case that state modified on the local CPU needs to be synchronously
handled on a different processor.

One example is the Zephyr `k_thread_abort` API, which cannot return
until the thread that had been aborted is no longer runnable.  If it
is currently running on another CPU, that becomes difficult to
implement.

Another is low power idle.  It is a firm requirement on many devices
that system idle be implemented using a low-power mode with as many
interrupts (including periodic timer interrupts) disabled or deferred
as is possible.  If a CPU is in such a state, and on another CPU a
thread becomes runnable, the idle CPU has no way to "wake up" to
handle the newly-runnable load.

So where possible, Zephyr SMP architectures should implement an
interprocessor interrupt.  The current framework is very simple: the
architecture provides at least a `arch_sched_broadcast_ipi` call,
which when invoked will flag an interrupt on all CPUs (except the current one,
though that is allowed behavior). If the architecture supports directed IPIs
(see `CONFIG_ARCH_HAS_DIRECTED_IPIS`), then the
architecture also provides a `arch_sched_directed_ipi` call, which
when invoked will flag an interrupt on the specified CPUs. When an interrupt is
flagged on the CPUs, the `z_sched_ipi` function implemented in the
scheduler will get invoked on those CPUs. The expectation is that these
APIs will evolve over time to encompass more functionality (e.g. cross-CPU
calls), and that the scheduler-specific calls here will be implemented in
terms of a more general framework.

When directed IPIs are available, the scheduler signals only those CPUs that
actually need to reschedule when a thread becomes ready, rather than broadcasting
to every other CPU. This avoids disturbing CPUs whose currently running thread
does not need to be preempted, reducing the overall interrupt load.

Note that not all SMP architectures will have a usable IPI mechanism
(either missing, or just undocumented/unimplemented).  In those cases
Zephyr provides fallback behavior that is correct, but perhaps
suboptimal.

Using this, `k_thread_abort` becomes only slightly more
complicated in SMP: for the case where a thread is actually running on
another CPU (we can detect this atomically inside the scheduler), we
broadcast an IPI and spin, waiting for the thread to either become
"DEAD" or for it to re-enter the queue (in which case we terminate it
the same way we would have in uniprocessor mode).  Note that the
"aborted" check happens on any interrupt exit, so there is no special
handling needed in the IPI per se.  This allows us to implement a
reasonable fallback when IPI is not available: we can simply spin,
waiting until the foreign CPU receives any interrupt, though this may
be a much longer time!

Likewise idle wakeups are trivially implementable with an empty IPI
handler.  If a thread is added to an empty run queue (i.e. there may
have been idle CPUs), we broadcast an IPI.  A foreign CPU will then be
able to see the new thread when exiting from the interrupt and will
switch to it if available.

Without an IPI, however, a low power idle that requires an interrupt
will not work to synchronously run new threads.  The workaround in
that case is more invasive: Zephyr will **not** enter the system idle
handler and will instead spin in its idle loop, testing the scheduler
state at high frequency (not spinning on it though, as that would
involve severe lock contention) for new threads.  The expectation is
that power constrained SMP applications are always going to provide an
IPI, and this code will only be used for testing purposes or on
systems without power consumption requirements.


### IPI Cascades


The kernel can not control the order in which IPIs are processed by the CPUs
in the system. In general, this is not an issue and a single set of IPIs is
sufficient to trigger a reschedule on the N CPUs that results with them
scheduling the highest N priority ready threads to execute. When CPU masking
is used, there may be more than one valid set of threads (not to be confused
with an optimal set of threads) that can be scheduled on the N CPUs and a
single set of IPIs may be insufficient to result in any of these valid sets.


**Note:** When CPU masking is not in play, the optimal set of threads is the same as the valid set of threads. However when CPU masking is in play, there may be more than one valid set--one of which may be optimal. To better illustrate the distinction, consider a 2-CPU system with ready threads T1 and T2 at priorities 1 and 2 respectively. Let T2 be pinned to CPU0 and T1 not be pinned. If CPU0 is executing T2 and CPU1 executing T1, then this set is is both valid and optimal. However, if CPU0 is executing T1 and CPU1 is idling, then this too would be valid though not optimal.

In those cases where a single set of IPIs is not sufficient to generate a valid
set, the resulting set of executing threads are expected to be close to a valid
set, and subsequent IPIs can generally be expected to correct the situation
soon. However, for cases where neither the approximation nor the delay are
acceptable, enabling `CONFIG_SCHED_IPI_CASCADE` will allow the
kernel to generate cascading IPIs until the kernel has selected a valid set of
ready threads for the CPUs.

There are three types of costs/penalties associated with the IPI cascades--and
for these reasons they are disabled by default. The first is a cost incurred
by the CPU producing the IPI when a new thread preempts the old thread as checks
must be done to compare the old thread against the threads executing on the
other CPUs. The second is a cost incurred by the CPUs receiving the IPIs as
they must be processed. The third is the apparent sputtering of a thread as it
"winks in" and then "winks out" due to cascades stemming from the
aforementioned first cost.


### IPI Work Items


The kernel allows developers to execute functions on other CPUs at ISR level
using one or more IPI work items. After IPI work items have been added to the
specified CPUs' work queues using `k_ipi_work_add`, the targeted CPUs
will process them after receiving an IPI. Signaling an IPI is done by calling
`k_ipi_work_signal`. Waiting for an IPI work item to be completed by
the targeted CPUs is done by calling `k_ipi_work_wait`. Only a single
waiter is permitted at a time.


**Note:** IPI work items will only be added to the IPI work queues of other CPUs. If adding IPI work items at thread level, the developer must ensure that the current thread does not change CPUs until after signaling the IPIs.


#### Sample Use


The following code outlines how to use IPI work items to update status
information across a set of CPUs as a result of one CPU handling an ISR.

```c

struct k_ipi_work my_work;

void remote_cpu_action(struct k_ipi_work *arg)
{
    ...
}

void my_isr(void)
{
    /*
     * Wait for previous use of <my_work> to complete.
     * It assumes that <my_work> was initialized elsewhere.
     */

    uint32_t cpu_mask = <bitmask identifying CPUs to update>;

    while (k_ipi_work_wait(&my_work, K_NO_WAIT) == -EAGAIN) {
    }

    /* Add and signal the new work */

    k_ipi_work_add(&my_work, cpu_mask, remote_cpu_action);

    k_ipi_work_signal();
}
```
