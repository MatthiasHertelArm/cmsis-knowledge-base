---
id: "pyocd-gdb-remote-server-gdbserver-exit"
type: "concept"
domain: "debug"
title: "gdb remote server: Gdbserver exit"
summary: "The pyOCD gdbserver process will normally exit automatically when gdb detaches using any of the detach, kill, or disconnect commands."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/gdbserver.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/gdbserver.md#gdbserver-exit"
license: "Apache-2.0"
mode: "V"
---

The pyOCD gdbserver process will normally exit automatically when gdb detaches using any of the `detach`, `kill`, or `disconnect` commands. This can be changed with the `--persist` argument or `persist` session option, so that the gdbserver always remains running until terminated directly (by Control-C or equivalent signal).

When gdb connects in extended remote mode, the gdb `disconnect` command will detach gdb but keep the gdbserver running even if persist isn't enabled.
