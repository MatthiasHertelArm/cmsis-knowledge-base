---
id: "pyocd-session-options-list-gdb-server-options"
type: "concept"
domain: "debug"
title: "Session options list: GDB server options"
summary: "These session options are currently only applied when running the GDB server."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/options.md#gdb-server-options"
license: "Apache-2.0"
mode: "V"
---

These session options are currently only applied when running the GDB server.



| Option Name | Type | Default | Description |
|---|---|---|---|
| enable_semihosting | bool | False | Set to True to handle semihosting requests. Also see the `semihost_console_type` option. |
| enable_swv | bool | False | Whether to enable SWV printf output over the semihosting console. Requires the `swv_system_clock` option to be set. The SWO baud rate can be controlled with the `swv_clock` option. |
| debug.status_fault_retry_timeout | float | 1 | Duration in seconds that a failed target status check will be retried before an error is raised. Only applies while the target is running after a resume operation in the debugger and pyOCD is waiting for it to halt again. |
| live.status_fault_retry_timeout | float | No default | Timeout in seconds for retrying target status reads that fail with a transfer error while a server monitors a core. A successful read clears the retry period. If the timeout expires, the server instance for that core exits. If the option is omitted, retries continue indefinitely. |
| gdbserver_port | int | 3333 | Base TCP port for the gdbserver. The core number, which is 0 for the primary core, will be added to this value. |
| persist | bool | False | If True, the GDB server will not exit after GDB disconnects. |
| report_core_number | bool | False | Whether gdb server should report core number as part of the per-thread information. |
| rtos.enable | bool | True | Overall enable flag for RTOS aware debugging. By default it's enabled but can be switched off if necessary. |
| rtos.name | str | No default | Name of the RTOS plugin to use. If not set, all RTOS plugins are given a chance to load. |
| semihost_console_type | str | 'telnet' | If set to 'telnet' then the semihosting telnet server will be started. If set to 'console' then semihosting will print to the console. |
| semihost_use_syscalls | bool | False | Whether to use GDB syscalls for semihosting file access operations, or to have pyOCD perform the operations. This is most useful if GDB is running on a remote system. |
| semihost.commandline | str | Empty | Program command line string, used for the SYS_GET_CMDLINE semihosting request. |
| step_into_interrupt | bool | False | Set this option to True to enable interrupts when performing step operations. Otherwise interrupts will be disabled and step operations cannot be interrupted. |
| swv_clock | int | 1000000 (1 MHz) | Frequency in Hertz of the SWO baud rate. |
| swv_system_clock | int | No default | Frequency in Hertz of the target's system clock. Used to compute the SWO baud rate divider. |
| swv_raw_enable | bool | True | Enable flag for the raw SWV stream server. |
| swv_raw_port | int | 3443 | TCP port number for the raw SWV stream server. |
| swv_raw_file | str | No default | File path for the raw SWV stream output. |
| telnet_port | int | 4444 | Base TCP port number for the semihosting telnet server. The core number, which will be 0 for the primary core, is added to this value. |
| vector_catch | str | 'h' | Enable vector catch sources, one letter per enabled source in any order, or `all` or `none`. The source letters are: - `h`=hard fault - `b`=bus fault - `m`=mem fault - `e`=secure fault - `i`=irq err - `s`=state err - `c`=check err - `p`=nocp - `r`=reset - `a`=all - `n`=none |
| register_fields | bool | True | When set to True, registers with bitfields will have their respective bitfields defined for presentation in gdb. |
