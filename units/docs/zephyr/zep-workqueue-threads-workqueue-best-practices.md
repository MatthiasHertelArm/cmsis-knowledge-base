---
id: "zep-workqueue-threads-workqueue-best-practices"
type: "concept"
domain: "rtos"
title: "Workqueue Threads: Workqueue Best Practices"
summary: "Sometimes the data a work item must process is naturally thread-safe, for example when it's put into a k_queue by some thread and processed in the work thread."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/threads/workqueue.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/threads/workqueue.rst"
license: "Apache-2.0"
mode: "V"
---

### Avoid Race Conditions


Sometimes the data a work item must process is naturally thread-safe, for
example when it's put into a `k_queue` by some thread and processed
in the work thread. More often external synchronization is required to avoid
data races: cases where the work thread might inspect or manipulate shared
state that's being accessed by another thread or interrupt.  Such state might
be a flag indicating that work needs to be done, or a shared object that is
filled by an ISR or thread and read by the work handler.

For simple flags atomic_v2 may be sufficient.  In other cases spin
locks (`k_spinlock`) or thread-aware locks (`k_sem`,
`k_mutex` , ...) may be used to ensure data races don't occur.

If the selected lock mechanism can api_term_sleep then allowing the
work thread to sleep will starve other work queue items, which may need to
make progress in order to get the lock released. Work handlers should try to
take the lock with its no-wait path. For example:

```c

static void work_handler(struct work *work)
{
        struct work_context *parent = CONTAINER_OF(work, struct work_context,
                                               work_item);

        if (k_mutex_lock(&parent->lock, K_NO_WAIT) != 0) {
                /* NB: Submit will fail if the work item is being cancelled. */
                (void)k_work_submit(work);
        return;
    }

    /* do stuff under lock */
    k_mutex_unlock(&parent->lock);
    /* do stuff without lock */
}
```
Be aware that if the lock is held by a thread with a lower priority than the
work queue the resubmission may starve the thread that would release the lock,
causing the application to fail.  Where the idiom above is required a
delayable work item is preferred, and the work should be (re-)scheduled with a
non-zero delay to allow the thread holding the lock to make progress.

Note that submitting from the work handler can fail if the work item had been
cancelled.  Generally this is acceptable, since the cancellation will complete
once the handler finishes.  If it is not, the code above must take other steps
to notify the application that the work could not be performed.

Work items in isolation are self-locking, so you don't need to hold an
external lock just to submit or schedule them. Even if you use external state
protected by such a lock to prevent further resubmission, it's safe to do the
resubmit as long as you're sure that eventually the item will take its lock
and check that state to determine whether it should do anything.  Where a
delayable work item is being rescheduled in its handler due to inability to
take the lock, some other self-locking state, such as an atomic flag set by the
application/driver when the cancel is initiated, would be required to detect
the cancellation and avoid the cancelled work item being submitted again after
the deadline.


### Check Return Values


All work API functions return status of the underlying operation, and in many
cases it is important to verify that the intended result was obtained.

* Submitting a work item (`k_work_submit_to_queue`) can fail if the
  work is being cancelled or the queue is not accepting new items.  If this
  happens the work will not be executed, which could cause a subsystem that is
  animated by work handler activity to become non-responsive.
* Asynchronous cancellation (`k_work_cancel` or
  `k_work_cancel_delayable`) can complete while the work item is still
  being run by a handler.  Proceeding to manipulate state shared with the work
  handler will result in data races that can cause failures.

Many race conditions have been present in Zephyr code because the results of
an operation were not checked.

There may be good reason to believe that a return value indicating that the
operation did not complete as expected is not a problem.  In those cases the
code should clearly document this, by (1) casting the return value to `void`
to indicate that the result is intentionally ignored, and (2) documenting what
happens in the unexpected case.  For example:

```c

/* If this fails, the work handler will check pub->active and
 * exit without transmitting.
 */
(void)k_work_cancel_delayable(&pub->timer);
```
However in such a case the following code must still avoid data races, as it
cannot guarantee that the work thread is not accessing work-related state.


### Don't Optimize Prematurely


The workqueue API is designed to be safe when invoked from multiple threads
and interrupts. Attempts to externally inspect a work item's state and make
decisions based on the result are likely to create new problems.

So when new work comes in, just submit it. Don't attempt to "optimize" by
checking whether the work item is already submitted by inspecting snapshot
state with `k_work_is_pending` or `k_work_busy_get`, or
checking for a non-zero delay from
`k_work_delayable_remaining_get()`. Those checks are fragile: a "busy"
indication can be obsolete by the time the test is returned, and a "not-busy"
indication can also be wrong if work is submitted from multiple contexts, or
(for delayable work) if the deadline has completed but the work is still in
queued or running state.

A general best practice is to always maintain in shared state some condition
that can be checked by the handler to confirm whether there is work to be
done.  This way you can use the work handler as the standard cleanup path:
rather than having to deal with cancellation and cleanup at points where items
are submitted, you may be able to have everything done in the work handler
itself.

A rare case where you could safely use `k_work_is_pending` is as a
check to avoid invoking `k_work_flush` or
`k_work_cancel_sync`, if you are *certain* that nothing else might
submit the work while you're checking (generally because you're holding a lock
that prevents access to state used for submission).
