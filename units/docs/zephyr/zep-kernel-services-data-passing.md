---
id: "zep-kernel-services-data-passing"
type: "concept"
domain: "rtos"
title: "Kernel Services: Data Passing"
summary: "These pages cover kernel objects which can be used to pass data between threads and ISRs."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/index.rst"
license: "Apache-2.0"
mode: "V"
---

These pages cover kernel objects which can be used to pass data between
threads and ISRs.

The following table summarizes their high-level features.

===============   ==============      ===================    ================    =================   =================  ==============  ===============================
Object            Bidirectional?      Data structure         Data item size      Data Alignment      ISRs can receive?  ISRs can send?  Overrun handling
===============   ==============      ===================    ================    =================   =================  ==============  ===============================
FIFO              No                  Queue                  Arbitrary [#f1]_    4 B [#f2]_          Yes [#f3]_         Yes             N/A
LIFO              No                  Queue                  Arbitrary [#f1]_    4 B [#f2]_          Yes [#f3]_         Yes             N/A
Stack             No                  Array                  Word                Word                Yes [#f3]_         Yes             Undefined behavior
Message queue     No                  Ring buffer            Arbitrary [#f6]_    Power of two        Yes [#f3]_         Yes             Pend thread or return -errno
Mailbox           Yes                 Queue                  Arbitrary [#f1]_    Arbitrary           No                 No              N/A
Pipe              No                  Ring buffer [#f4]_     Arbitrary           Arbitrary           Yes [#f5]_         Yes [#f5]_      Pend thread or return -errno
===============   ==============      ===================    ================    =================   =================  ==============  ===============================

.. [#f1] Callers allocate space for queue overhead in the data
         elements themselves.

.. [#f2] Objects added with `k_fifo_alloc_put()` and `k_lifo_alloc_put()`
         do not have alignment constraints, but use temporary memory from the
         calling thread's resource pool.

.. [#f3] ISRs can receive only when passing K_NO_WAIT as the timeout
         argument.

.. [#f4] Optional.

.. [#f5] ISRs can send and/or receive only when passing K_NO_WAIT as the
         timeout argument.

.. [#f6] Data item size must be a multiple of the data alignment.
