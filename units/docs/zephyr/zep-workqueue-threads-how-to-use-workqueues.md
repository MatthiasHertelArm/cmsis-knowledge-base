---
id: "zep-workqueue-threads-how-to-use-workqueues"
type: "concept"
domain: "rtos"
title: "Workqueue Threads: How to Use Workqueues"
summary: "A workqueue is defined using a variable of type k_work_q. The workqueue is initialized by defining the stack area used by its thread, initializing the k_work_q, either zeroing its memory or calling k_work_queue_init, and then calling k_work_queue_start."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/workqueue.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/workqueue.rst"
license: "Apache-2.0"
mode: "V"
---

### Defining and Controlling a Workqueue


A workqueue is defined using a variable of type `k_work_q`.
The workqueue is initialized by defining the stack area used by its
thread, initializing the `k_work_q`, either zeroing its
memory or calling `k_work_queue_init`, and then calling
`k_work_queue_start`. The stack area must be defined using
`K_THREAD_STACK_DEFINE` to ensure it is properly set up in
memory.

The following code defines and initializes a workqueue:

```c

#define MY_STACK_SIZE 512
#define MY_PRIORITY 5

K_THREAD_STACK_DEFINE(my_stack_area, MY_STACK_SIZE);

struct k_work_q my_work_q;

k_work_queue_init(&my_work_q);

k_work_queue_start(&my_work_q, my_stack_area,
                   K_THREAD_STACK_SIZEOF(my_stack_area), MY_PRIORITY,
           NULL);
```
In addition the queue identity and certain behavior related to thread
rescheduling can be controlled by the optional final parameter; see
`k_work_queue_start()` for details.

The following API can be used to interact with a workqueue:

* `k_work_queue_drain()` can be used to block the caller until the
  work queue has no items left.  Work items resubmitted from the workqueue
  thread are accepted while a queue is draining, but work items from any other
  thread or ISR are rejected.  The restriction on submitting more work can be
  extended past the completion of the drain operation in order to allow the
  blocking thread to perform additional work while the queue is "plugged".
  Note that draining a queue has no effect on scheduling or processing
  delayable items, but if the queue is plugged and the deadline expires the
  item will silently fail to be submitted.
* `k_work_queue_unplug()` removes any previous block on submission to
  the queue due to a previous drain operation.


### Submitting a Work Item


A work item is defined using a variable of type `k_work`.  It must
be initialized by calling `k_work_init`, unless it is defined using
`K_WORK_DEFINE` in which case initialization is performed at
compile-time.

An initialized work item can be submitted to the system workqueue by
calling `k_work_submit`, or to a specified workqueue by
calling `k_work_submit_to_queue`.

The following code demonstrates how an ISR can offload the printing
of error messages to the system workqueue. Note that if the ISR attempts
to resubmit the work item while it is still queued, the work item is left
unchanged and the associated error message will not be printed.

```c

struct device_info {
    struct k_work work;
    char name[16]
} my_device;

void my_isr(void *arg)
{
    ...
    if (error detected) {
        k_work_submit(&my_device.work);
}
...
}

void print_error(struct k_work *item)
{
    struct device_info *the_device =
        CONTAINER_OF(item, struct device_info, work);
    printk("Got error on device %s\n", the_device->name);
}

/* initialize name info for a device */
strcpy(my_device.name, "FOO_dev");

/* initialize work item for printing device's error messages */
k_work_init(&my_device.work, print_error);

/* install my_isr() as interrupt handler for the device (not shown) */
...
```
The following API can be used to check the status of or synchronize with the
work item:

* `k_work_busy_get()` returns a snapshot of flags indicating work item
  state.  A zero value indicates the work is not scheduled, submitted, being
  executed, or otherwise still being referenced by the workqueue
  infrastructure.
* `k_work_is_pending()` is a helper that indicates `true` if and only
  if the work is scheduled, queued, or running.
* `k_work_flush()` may be invoked from threads to block until the work
  item has completed.  It returns immediately if the work is not pending.
* `k_work_cancel()` attempts to prevent the work item from being
  executed.  This may or may not be successful. This is safe to invoke
  from ISRs.
* `k_work_cancel_sync()` may be invoked from threads to block until
  the work completes; it will return immediately if the cancellation was
  successful or not necessary (the work wasn't submitted or running).  This
  can be used after `k_work_cancel()` is invoked (from an ISR) to
  confirm completion of an ISR-initiated cancellation.


### Scheduling a Delayable Work Item


A delayable work item is defined using a variable of type
`k_work_delayable`. It must be initialized by calling
`k_work_init_delayable`.

For delayed work there are two common use cases, depending on whether a
deadline should be extended if a new event occurs. An example is collecting
data that comes in asynchronously, e.g. characters from a UART associated with
a keyboard.  There are two APIs that submit work after a delay:

* `k_work_schedule()` (or `k_work_schedule_for_queue()`)
  schedules work to be executed at a specific time or after a delay.  Further
  attempts to schedule the same item with this API before the delay completes
  will not change the time at which the item will be submitted to its queue.
  Use this if the policy is to keep collecting data until a specified delay
  since the **first** unprocessed data was received;
* `k_work_reschedule()` (or `k_work_reschedule_for_queue()`)
  unconditionally sets the deadline for the work, replacing any previous
  incomplete delay and changing the destination queue if necessary.  Use this
  if the policy is to keep collecting data until a specified delay since the
  **last** unprocessed data was received.

If the work item is not scheduled both APIs behave the same.  If
`K_NO_WAIT` is specified as the delay the behavior is as if the item
was immediately submitted directly to the target queue, without waiting for a
minimal timeout (unless `k_work_schedule()` is used and a previous
delay has not completed).

Both also have variants that allow
control of the queue used for submission.

The helper function `k_work_delayable_from_work()` can be used to get
a pointer to the containing `k_work_delayable` from a pointer to
`k_work` that is passed to a work handler function.

The following additional API can be used to check the status of or synchronize
with the work item:

* `k_work_delayable_busy_get()` is the analog to `k_work_busy_get()`
  for delayable work.
* `k_work_delayable_is_pending()` is the analog to
  `k_work_is_pending()` for delayable work.
* `k_work_flush_delayable()` is the analog to `k_work_flush()`
  for delayable work.
* `k_work_cancel_delayable()` is the analog to
  `k_work_cancel()` for delayable work; similarly with
  `k_work_cancel_delayable_sync()`.


### Synchronizing with Work Items


While the state of both regular and delayable work items can be determined
from any context using `k_work_busy_get()` and
`k_work_delayable_busy_get()` some use cases require synchronizing
with work items after they've been submitted.  `k_work_flush()`,
`k_work_cancel_sync()`, and `k_work_cancel_delayable_sync()`
can be invoked from thread context to wait until the requested state has been
reached.

These APIs must be provided with a `k_work_sync` object that has no
application-inspectable components but is needed to provide the
synchronization objects.  These objects should not be allocated on a stack if
the code is expected to work on architectures with
`CONFIG_KERNEL_COHERENCE`.
