---
id: "zep-gdb-stub-overview"
type: "concept"
domain: "debug"
title: "GDB stub: Overview"
summary: "The gdbstub feature provides an implementation of the GDB Remote Serial Protocol (RSP) that allows you to remotely debug Zephyr using GDB."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/debugging/gdbstub.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/debugging/gdbstub.rst"
license: "Apache-2.0"
mode: "V"
---

The gdbstub feature provides an implementation of the GDB Remote
Serial Protocol (RSP) that allows you to remotely debug Zephyr
using GDB.

The protocol supports different connection types: serial, UDP/IP and
TCP/IP. Zephyr currently supports only serial device communication.

The GDB program acts as a client while the Zephyr gdbstub acts as a
server. When this feature is enabled, Zephyr stops its execution after
`gdb_init` starts gdbstub service and waits for a GDB
connection. Once a connection is established it is possible to
synchronously interact with Zephyr. Note that currently it is not
possible to asynchronously send commands to the target.
