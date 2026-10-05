---
id: "zep-single-linked-list"
type: "concept"
domain: "rtos"
title: "Single-linked List"
summary: "Zephyr provides a sys_slist_t type for storing simple singly-linked list data (i.e. data where each list element stores a pointer to the next element, but not the previous one)."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/data_structures/slist.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/data_structures/slist.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr provides a `sys_slist_t` type for storing simple
singly-linked list data (i.e. data where each list element stores a
pointer to the next element, but not the previous one).  This supports
constant-time access to the first (head) and last (tail) elements of
the list, insertion before the head and after the tail of the list and
constant time removal of the head.  Removal of subsequent nodes
requires access to the "previous" pointer and thus can only be
performed in linear time by searching the list.

The `sys_slist_t` struct may be instantiated by the user in any
accessible memory.  It should be initialized with either
`sys_slist_init` or by static assignment from SYS_SLIST_STATIC_INIT
before use.  Its interior fields are opaque and should not be accessed
by user code.

The end nodes of a list may be retrieved with
`sys_slist_peek_head` and `sys_slist_peek_tail`, which will
return NULL if the list is empty, otherwise a pointer to a
`sys_snode_t` struct.

The `sys_snode_t` struct represents the data to be inserted.  In
general, it is expected to be allocated/controlled by the user,
usually embedded within a struct which is to be added to the list.
The container struct pointer may be retrieved from a list node using
`SYS_SLIST_CONTAINER`, passing it the struct name of the
containing struct and the field name of the node.  Internally, the
`sys_snode_t` struct contains only a next pointer, which may be
accessed with `sys_slist_peek_next`.

Lists may be modified by adding a single node at the head or tail with
`sys_slist_prepend` and `sys_slist_append`.  They may also
have a node added to an interior point with `sys_slist_insert`,
which inserts a new node after an existing one.  Similarly
`sys_slist_remove` will remove a node given a pointer to its
predecessor.  These operations are all constant time.

Convenience routines exist for more complicated modifications to a
list.  `sys_slist_merge_slist` will append an entire list to an
existing one.  `sys_slist_append_list` will append a bounded
subset of an existing list in constant time.  And
`sys_slist_find_and_remove` will search a list (in linear time)
for a given node and remove it if present.

Finally the slist implementation provides a set of "for each" macros
that allows for iterating over a list in a natural way without needing
to manually traverse the next pointers.  `SYS_SLIST_FOR_EACH_NODE`
will enumerate every node in a list given a local variable to store
the node pointer.  `SYS_SLIST_FOR_EACH_NODE_SAFE` behaves
similarly, but has a more complicated implementation that requires an
extra scratch variable for storage and allows the user to delete the
iterated node during the iteration.  Each of those macros also exists
in a "container" variant (`SYS_SLIST_FOR_EACH_CONTAINER` and
`SYS_SLIST_FOR_EACH_CONTAINER_SAFE`) which assigns a local
variable of a type that matches the user's container struct and not
the node struct, performing the required offsets internally.  And
`SYS_SLIST_ITERATE_FROM_NODE` exists to allow for enumerating a
node and all its successors only, without inspecting the earlier part
of the list.
