---
id: "pyocd-semihosting-session-options"
type: "concept"
domain: "debug"
title: "Semihosting: Session options"
summary: "These are the session options that control semihosting:"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/semihosting.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/semihosting.md#session-options"
license: "Apache-2.0"
mode: "V"
---

These are the session options that control semihosting:

- `enable_semihosting` - Set to true to handle semihosting requests.
- `semihost_console_type` - If set to 'telnet' then the semihosting telnet server will be started. If set to 'console' then semihosting will print to pyOCD's console.
- `semihost.commandline` - Command line string return to the target for the `SYS_GET_CMDLINE` request.
- `semihost_use_syscalls` - Whether to use GDB syscalls for semihosting file access operations, or to have pyOCD perform the operations.)
- `telnet_port` - Base TCP port number for the semihosting telnet server. The core number, which will be 0 for the primary core, is added to this value.
