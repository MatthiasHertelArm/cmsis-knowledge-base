---
id: "pyocd-semihosting-routing"
type: "concept"
domain: "debug"
title: "Semihosting: Routing"
summary: "There several ways to route semihosting I/O requests in pyOCD, depending on the file on which the request is operating."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/semihosting.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/semihosting.md#routing"
license: "Apache-2.0"
mode: "V"
---

There several ways to route semihosting I/O requests in pyOCD, depending on the file on which the request is operating.

First, an I/O request is classified as either "console" or "syscall". Console requests are those that operate on the
first three file descriptions: stdin (0), stdout (1), and stderr (2). Certain semihosting requests are always console.
All other requests, which are always for explicitly opened files, are classified as syscalls.

Console requests have two options for routing, controlled with the `semihost_console_type` session option's value.

- "telnet": I/O is connected to the "telnet" server. (In fact, it's not a true telnet server because it doesn't implement
    the telnet control requests.) This server runs on the port indicated by the `telnet_port` session option or the
    `-T`/`--telnet-port` command line argument of the gdbserver subcommand.
- "console": pyOCD's standard I/O is used.

Syscall requests also have two routing options. The `semihost_use_syscalls` option controls this depending on whether it
is true or false.

- _false_: File I/O requests are handled by pyOCD itself, and therefore are performed on the system on which the pyOCD
    process is running.
- _true_: File I/O is passed to gdb for handling.

Relative paths passed to the `SYS_OPEN` request are interpreted relative to the syscall handler's working directory.
In addition, if pyOCD and gdb are running on different systems, absolute paths will be interpreter according to the
appropriate system's root filesystem.

Defaults are for console to be routed to telnet and syscalls handled by gdb.
