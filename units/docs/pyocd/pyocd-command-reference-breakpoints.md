---
id: "pyocd-command-reference-breakpoints"
type: "concept"
domain: "debug"
title: "Command reference: Breakpoints"
summary: "Command reference: Breakpoints"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/command_reference.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/command_reference.md#breakpoints"
license: "Apache-2.0"
mode: "V"
---

##### `break`

**Usage**: break ADDR \
Set a breakpoint address.


##### `lsbreak`

**Usage**: lsbreak  \
List breakpoints.


##### `lswatch`

**Usage**: lswatch  \
List watchpoints.


##### `rmbreak`

**Usage**: rmbreak ADDR \
Remove a breakpoint.


##### `rmwatch`

**Usage**: rmwatch ADDR [r|w|rw] [1|2|4] \
Remove watchpoint(s). Access type and size are optional. All watchpoints matching the specified parameters will be removed.


##### `watch`

**Usage**: watch ADDR [r|w|rw] [1|2|4] \
Set a watchpoint address, and optional access type (default rw) and size (4).
