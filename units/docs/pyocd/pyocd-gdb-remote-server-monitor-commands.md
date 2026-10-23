---
id: "pyocd-gdb-remote-server-monitor-commands"
type: "concept"
domain: "debug"
title: "gdb remote server: Monitor commands"
summary: "Commands can be sent directly to pyOCD using the gdb monitor command. Any output from pyOCD is returned through gdb and printed on the console. This is effectively the same as running the pyocd commander subcommand."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/gdbserver.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/gdbserver.md#monitor-commands"
license: "Apache-2.0"
mode: "V"
---

Commands can be sent directly to pyOCD using the gdb `monitor` command. Any output from pyOCD is returned through gdb and printed on the console. This is effectively the same as running the `pyocd commander` subcommand. All [pyOCD commands]({% link _docs/command_reference.md %}) are available.

pyOCD initial selects the core controlled by the gdbserver as the target for monitor commands. Similarly, the selected AP is initially set to the gdbserver's core's MEM-AP. PyOCD's [`core` command]({% link _docs/command_reference.md %}#core-1) can be used to select a different core. This might be useful in order to release a secondary core from reset before starting to debug it, although a [user script]({% link _docs/user_scripts.md %}) could be a better choice.
