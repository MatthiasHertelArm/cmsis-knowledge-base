---
id: "pyocd-session-options-list-extended-options-with-multicore-support"
type: "concept"
domain: "debug"
title: "Session options list: Extended options with multicore support"
summary: "These session options offer extended configuration using either a single setting or a per-core setting, using a list with an entry for each core."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/options.md#extended-options-with-multicore-support"
license: "Apache-2.0"
mode: "V"
---

These session options offer extended configuration using either a single setting or a per-core setting,
using a list with an entry for each core. When one of the following options is set using a comma separated list
inside square brackets [], the per-core assignment is encoded by the index (position) of the value in
that list. When using a list, all cores must have a corresponding entry.



| Option Name | Type | Default | Description |
|---|---|---|---|
| gdbserver_port | int, list of int | 3333 | Base TCP port for the GDB Server. For multicore targets the zero-based core number will be added to the value unless a list is specified. Examples: `3343`, where in case of a multicore target, TCP port 3343 is assigned to `core0`, TCP port 3344 is assigned to `core1`, and so on. `[3343, 3334]`, where TCP port 3343 is assigned to `core0` and TCP port 3334 is assigned to `core1`. |
| stdio_mode | str, list of str | 'server' | Controls connection to standard I/O. Must be one of 'off', 'console', 'server', or 'file'. For multicore devices the mode applies to all cores unless it is specified as a list. This session option is preferred over the `semihost_console_type` option. Examples: `console`, where the standard I/O for all cores is routed to the console. `[console, server]`, where the standard I/O for `core0` is routed to the console and the standard I/O for `core1` is routed to the Telnet Server. |
| stdio_port | int, list of int | 4444 | The option applies only when `stdio_mode` is set to 'server'. Base TCP port for the Telnet Server. For multicore targets the zero-based core number will be added to the value unless a list is specified. Examples: `4434`, where in case of a multicore target, TCP port 4434 is assigned to `core0`, TCP port 4435 is assigned to `core1`, and so on. `[4434, 4443]`, where TCP port 4434 is assigned to `core0` and TCP port 4443 is assigned to `core1`. |
| stdio_file_in | str, list of str | `<target>`.in | The option applies only when `stdio_mode` is set to 'file'. Input filename to use as stdin . When a single string is used, the core number (_<core>) will be appended to the filename in case of multicore targets. Examples: `mytarget.in`, where in case of a multicore target, the filenames will be `mytarget_0.in` assigned to `core0`, `mytarget_1.in` assigned to `core1`, and so on. `[mytarget_cm4.in, mytarget_cm0.in]`, where `mytarget_cm4.in` is assigned to `core0` and `mytarget_cm0.in` is assigned to `core1`. |
| stdio_file_out | str, list of str | `<target>`.out | The option applies only when `stdio_mode` is set to 'file'. Output filename to use as stdout . When a single string is used, the core number (_<core>) will be appended to the filename in case of multicore targets. Examples: `mytarget.out`, where in case of a multicore target, the filenames will be `mytarget_0.out` assigned to `core0`, `mytarget_1.out` assigned to `core1`, and so on. `[mytarget_cm4.out, mytarget_cm0.out]`, where `mytarget_cm4.out` is assigned to `core0` and `mytarget_cm0.out` is assigned to `core1`. |
