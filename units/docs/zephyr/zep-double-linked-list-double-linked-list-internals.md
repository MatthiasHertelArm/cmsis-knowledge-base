---
id: "zep-double-linked-list-double-linked-list-internals"
type: "concept"
domain: "rtos"
title: "Double-linked List: Double-linked List Internals"
summary: "Internally, the dlist implementation is minimal: the sys_dlist_t struct contains \"head\" and \"tail\" pointer fields, the sys_dnode_t contains \"prev\" and \"next\" pointers, and no other data is stored."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/data_structures/dlist.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/data_structures/dlist.rst"
license: "Apache-2.0"
mode: "V"
---

Internally, the dlist implementation is minimal: the `sys_dlist_t`
struct contains "head" and "tail" pointer fields, the `sys_dnode_t`
contains "prev" and "next" pointers, and no other data is stored.  But
in practice the two structs are internally identical, and the list
struct is inserted as a node into the list itself.  This allows for a
very clean symmetry of operations:

* An empty list has backpointers to itself in the list struct, which
  can be trivially detected.

* The head and tail of the list can be detected by comparing the
  prev/next pointers of a node vs. the list struct address.

* An insertion or deletion never needs to check for the special case
  of inserting at the head or tail.  There are never any NULL pointers
  within the list to be avoided.  Exactly the same operations are run,
  without tests or branches, for all list modification primitives.

Effectively, a dlist of N nodes can be thought of as a "ring" of "N+1"
nodes, where one node represents the list tracking struct.
