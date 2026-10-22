---
id: "pyocd-command-reference-core"
type: "concept"
domain: "debug"
title: "Command reference: Core"
summary: "Command reference: Core"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/command_reference.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/command_reference.md#core"
license: "Apache-2.0"
mode: "V"
---

##### `continue`

**Aliases**: `c`, `go`, `g` \
**Usage**: continue  \
Resume execution of the target. The target's state is read back after resuming. If the target is not running, then it's state is reported. For instance, if the target is halted immediately after resuming, a debug event such as a breakpoint most likely occurred.


##### `core`

**Usage**: core [NUMBER | NAME] \
Select CPU core by number or name, or print selected core.


##### `halt`

**Aliases**: `h` \
**Usage**: halt  \
Halt the target.


##### `step`

**Aliases**: `s` \
**Usage**: step [COUNT] \
Step one or more instructions.
