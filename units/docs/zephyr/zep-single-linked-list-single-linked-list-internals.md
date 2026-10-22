---
id: "zep-single-linked-list-single-linked-list-internals"
type: "concept"
domain: "rtos"
title: "Single-linked List: Single-linked List Internals"
summary: "The slist code is designed to be minimal and conventional. Internally, a sys_slist_t struct is nothing more than a pair of \"head\" and \"tail\" pointer fields. And a sys_snode_t stores only a single \"next\" pointer."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/data_structures/slist.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/data_structures/slist.rst"
license: "Apache-2.0"
mode: "V"
---

The slist code is designed to be minimal and conventional.
Internally, a `sys_slist_t` struct is nothing more than a pair of
"head" and "tail" pointer fields.  And a `sys_snode_t` stores only a
single "next" pointer.

The specific implementation of the list code, however, is done with an
internal "Z_GENLIST" template API which allows for extracting those
fields from arbitrary structures and emits an arbitrarily named set of
functions.  This allows for implementing more complicated
single-linked list variants using the same basic primitives.  The
genlist implementer is responsible for a custom implementation of the
primitive operations only: an "init" step for each struct, and a "get"
and "set" primitives for each of head, tail and next pointers on their
relevant structs.  These inline functions are passed as parameters to
the genlist macro expansion.

Only one such variant, sflist, exists in Zephyr at the moment.
