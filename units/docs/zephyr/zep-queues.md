---
id: "zep-queues"
type: "concept"
domain: "rtos"
title: "Queues"
summary: "A Queue in Zephyr is a kernel object that implements a traditional queue, allowing threads and ISRs to add and remove data items of any size."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/data_passing/queues.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/data_passing/queues.rst"
license: "Apache-2.0"
mode: "V"
---

A Queue in Zephyr is a kernel object that implements a traditional queue, allowing
threads and ISRs to add and remove data items of any size. The queue is similar
to a FIFO and serves as the underlying implementation for both :ref:`k_fifo
<fifos_v2>` and k_lifo. For more information on usage see
k_fifo.
