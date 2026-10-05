---
id: "pyocd-gdb-remote-server-useful-commands"
type: "concept"
domain: "debug"
title: "gdb remote server: Useful commands"
summary: "Gdb by default restricts memory accesses to regions defined in the target memory map provided by pyOCD."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/gdbserver.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/gdbserver.md#useful-commands"
license: "Apache-2.0"
mode: "V"
---

Gdb by default restricts memory accesses to regions defined in the target memory map provided by pyOCD. This has the unhappy side effect of preventing access to peripheral registers or other Device memory, since the memory maps do not include those regions.

To work around this, disable gbd's `mem inaccessible-by-default` setting.

This line can be added into your `.gdbinit` file:

    (gdb) set mem inaccessible-by-default off

It can also be useful to add an alias to make monitor commands (below) easier to access:

    (gdb) alias m = monitor

To catch crashes and unexpected exceptions, use [`set vector-catch`]({% link _docs/command_reference.md %}#vector-catch) to enable the M-profile vector catch feature:

    (gdb) monitor set vector-catch all

If the core halts in an exception handler, use [`show fault`]({% link _docs/command_reference.md %}#fault) to print out the M-profile fault syndrome registers.

    (gdb) monitor show fault

For most targets, peripheral registers can be accessed using pyOCD's [`reg`]({% link _docs/command_reference.md %}#reg) and [`wreg`]({% link _docs/command_reference.md %}#wreg) commands.

    (gdb) monitor reg TIM21.PSC

Enabling access to all memory as described above is required for this to work.
