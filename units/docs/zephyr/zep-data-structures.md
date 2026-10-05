---
id: "zep-data-structures"
type: "concept"
domain: "rtos"
title: "Data Structures"
summary: "Zephyr provides a library of common general purpose data structures used within the kernel, but useful by application code in general."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/data_structures/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/data_structures/index.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr provides a library of common general purpose data structures
used within the kernel, but useful by application code in general.
These include list and balanced tree structures for storing ordered
data, and a ring buffer for managing "byte stream" data in a clean
way.

Note that in general, the collections are implemented as "intrusive"
data structures.  The "node" data is the only struct used by the
library code, and it does not store a pointer or other metadata to
indicate what user data is "owned" by that node.  Instead, the
expectation is that the node will be itself embedded within a
user-defined struct.  Macros are provided to retrieve a user struct
address from the embedded node pointer in a clean way.  The purpose
behind this design is to allow the collections to be used in contexts
where dynamic allocation is disallowed (i.e. there is no need to
allocate node objects because the memory is provided by the user).

Note also that these libraries are generally unsynchronized; access to
them is not threadsafe by default.  These are data structures, not
synchronization primitives.  The expectation is that any locking
needed will be provided by the user.  Some of the provided data
structures are thread safe in specific usage scenarios (see
spsc_lockfree and mpsc_lockfree).
