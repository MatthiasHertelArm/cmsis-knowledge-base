---
id: "frb-5-queue-management-5-6-1-queue-sets"
type: "concept"
domain: "rtos"
title: "5 Queue Management: 5.6 Receiving From Multiple Queues / 5.6.1 Queue Sets"
summary: "Part of: 5.6 Receiving From Multiple Queues"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch05.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch05.md#5-6-1-queue-sets"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 5.6 Receiving From Multiple Queues_

Often application designs require a single task to receive data of
different sizes, data with different meanings, and data from different
sources. The previous section demonstrated how to do this in a neat and
efficient way using a single queue that receives structures. However,
sometimes an application's designer is working with constraints that
limit their design choices, necessitating the use of a separate queue
for some data sources. For example, third party code being integrated
into a design might assume the presence of a dedicated queue. In such
cases a 'queue set' can be used.

Queue sets allow a task to receive data from more than one queue without
the task polling each queue in turn to determine which, if any, contains
data.

A design that uses a queue set to receive data from multiple sources is
less neat, and less efficient, than a design that achieves the same
functionality using a single queue that receives structures. For that
reason, it is recommended to only use queue sets if design constraints
make their use absolutely necessary.

The following sections describe how to use a queue set by:

- Creating a queue set.

- Adding queues to the set.

  Semaphores can also be added to a queue set. Semaphores are described later in this book.

- Reading from the queue set to determine which queues within the set contain data.

  When a queue that is a member of a set receives data, the handle of
  the receiving queue is sent to the queue set, and returned when a
  task calls a function that reads from the queue set. Therefore, if a
  queue handle is returned from a queue set, then the queue referenced
  by the handle is known to contain data, and the task can then read
  from that queue directly.

  > *Note: If a queue is a member of a queue set then you must read from
  > the queue each time its handle is received from the queue set, and you
  > must not read from the queue before its handle is received from the
  > queue set.*

Queue set functionality is enabled by setting the `configUSE_QUEUE_SETS`
compile time configuration constant to 1 in FreeRTOSConfig.h.
