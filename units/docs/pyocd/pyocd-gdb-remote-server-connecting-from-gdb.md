---
id: "pyocd-gdb-remote-server-connecting-from-gdb"
type: "concept"
domain: "debug"
title: "gdb remote server: Connecting from gdb"
summary: "To connect gdb to pyOCD's gdbserver, use the target remote <host>:<port> command. These take the server's host name and port number separated by a colon as an argument."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/gdbserver.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/gdbserver.md#connecting-from-gdb"
license: "Apache-2.0"
mode: "V"
---

To connect gdb to pyOCD's gdbserver, use the `target remote <host>:<port>` command. These take the server's host name and port number separated by a colon as an argument. For a server running on the same host as gdb, using the default pyOCD port (see above for how to change it), this will be `target remote localhost:3333`.

PyOCD also support extended remote mode. In this case, the connect command is `target extended-remote <host>:<port>`. Extended remote mode allows using the gdb `disconnect` command to disconnect from pyOCD while keeping the gdbserver running.

After connecting gdb, perform the following steps to program updated firmware and run the new code.

1. Program firmware using the `load` command.

2. Reset the target and halt with `monitor reset halt`. This halts the core at the first instruction.

3. Set breakpoints and resume, or use a command line `until main` to run to the first line of `main()`.
