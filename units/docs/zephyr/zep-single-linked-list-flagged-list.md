---
id: "zep-single-linked-list-flagged-list"
type: "concept"
domain: "rtos"
title: "Single-linked List: Flagged List"
summary: "The sys_sflist_t is implemented using the described genlist template API. With the exception of symbol naming (\"sflist\" instead of \"slist\") and the additional API described next, it operates in all ways identically to the slist API."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/data_structures/slist.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/data_structures/slist.rst"
license: "Apache-2.0"
mode: "V"
---

The `sys_sflist_t` is implemented using the described genlist
template API.  With the exception of symbol naming ("sflist" instead
of "slist") and the additional API described next, it operates in all
ways identically to the slist API.

It adds the ability to associate exactly two bits of user defined
"flags" with each list node.  These can be accessed and modified with
`sys_sfnode_flags_get` and `sys_sfnode_flags_set`.
Internally, the flags are stored unioned with the bottom bits of the
next pointer and incur no SRAM storage overhead when compared with the
simpler slist code.
