---
id: "pyocd-gdb-remote-server"
type: "concept"
domain: "debug"
title: "gdb remote server"
summary: "The pyocd gdbserver subcommand runs a gdb remote serial protocol (RSP) server that allows gdb to debug embedded targets."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/gdbserver.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/gdbserver.md"
license: "Apache-2.0"
mode: "V"
---

The `pyocd gdbserver` subcommand runs a gdb remote serial protocol (RSP) server that allows gdb to debug embedded targets.

To run a debug session, the pyOCD gdbserver needs to first be started. Then gdb connects to pyOCD and debugging can begin.
