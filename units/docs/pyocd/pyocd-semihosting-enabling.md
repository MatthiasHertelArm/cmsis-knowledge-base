---
id: "pyocd-semihosting-enabling"
type: "concept"
domain: "debug"
title: "Semihosting: Enabling"
summary: "To use semihosting with pyOCD, it first must be enabled. This can be done in several ways:"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/semihosting.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/semihosting.md#enabling"
license: "Apache-2.0"
mode: "V"
---

To use semihosting with pyOCD, it first must be enabled. This can be done in several ways:

- Pass `-S`/`--semihosting` on the `pyocd gdbserver` command line.
- Set the `enable_semihosting` session option to true.
- From gdb, issue a `monitor arm semihosting enable` command. This command is supported for compatibility with OpenOCD.

Assuming the default routing options and telnet port number are acceptable, no further configuration is required. When



Currently semihosting only works when pyOCD's gdbserver is running and the target is resumed, with the gdbserver
waiting for it to halt. However, the `pyocd.debug.semihost.SemihostAgent` class is reusable if a custom
target control loop is implemented.
