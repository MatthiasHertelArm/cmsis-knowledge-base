---
id: "pyocd-command-reference-gdbserver"
type: "concept"
domain: "debug"
title: "Command reference: Gdbserver"
summary: "Command reference: Gdbserver"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/command_reference.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/command_reference.md#gdbserver"
license: "Apache-2.0"
mode: "V"
---

##### `exit`

**Usage**: exit  \
Terminate running gdbservers in this session. For the pyocd gdbserver subcommand, terminating gdbservers will cause the process to exit. The effect when the gdbserver(s) are running in a different environment depends on that program. Note that gdb will still believe the connection to be valid after this command completes, so executing the 'disconnect' command is a necessity.
