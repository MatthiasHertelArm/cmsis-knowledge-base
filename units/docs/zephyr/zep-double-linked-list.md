---
id: "zep-double-linked-list"
type: "concept"
domain: "rtos"
title: "Double-linked List"
summary: "Similar to the single-linked list in many respects, Zephyr includes a double-linked implementation."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/data_structures/dlist.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/data_structures/dlist.rst"
license: "Apache-2.0"
mode: "V"
---

Similar to the single-linked list in many respects, Zephyr includes a
double-linked implementation.  This provides the same algorithmic
behavior for all the existing slist operations, but also allows for
constant-time removal and insertion (at all points: before or after
the head, tail or any internal node).  To do this, the list stores two
pointers per node, and thus has somewhat higher runtime code and
memory space needs.

A `sys_dlist_t` struct may be instantiated by the user in any
accessible memory.  It must be initialized with `sys_dlist_init`
or `SYS_DLIST_STATIC_INIT` before use.  The `sys_dnode_t` struct
is expected to be provided by the user for any nodes added to the
list (typically embedded within the struct to be tracked, as described
above).  It must be initialized in zeroed/bss memory or with
`sys_dnode_init` before use.

Primitive operations may retrieve the head/tail of a list and the
next/prev pointers of a node with `sys_dlist_peek_head`,
`sys_dlist_peek_tail`, `sys_dlist_peek_next` and
`sys_dlist_peek_prev`.  These can all return NULL where
appropriate (i.e. for empty lists, or nodes at the endpoints of the
list).

A dlist can be modified in constant time by removing a node with
`sys_dlist_remove`, by adding a node to the head or tail of a list
with `sys_dlist_prepend` and `sys_dlist_append`, or by
inserting a node before an existing node with `sys_dlist_insert`.

As for slist, each node in a dlist can be processed in a natural code
block style using `SYS_DLIST_FOR_EACH_NODE`.  This macro also
exists in a "FROM_NODE" form which allows for iterating from a known
starting point, a "SAFE" variant that allows for removing the node
being inspected within the code block, a "CONTAINER" style that
provides the pointer to a containing struct instead of the raw node,
and a "CONTAINER_SAFE" variant that provides both properties.

Convenience utilities provided by dlist include
`sys_dlist_insert_at`, which inserts a node that linearly searches
through a list to find the right insertion point, which is provided by
the user as a C callback function pointer, and
`sys_dnode_is_linked`, which will affirmatively return whether or
not a node is currently linked into a dlist or not (via an
implementation that has zero overhead vs. the normal list processing).
