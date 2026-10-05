---
id: "pyocd-semihosting-supported-requests"
type: "concept"
domain: "debug"
title: "Semihosting: Supported requests"
summary: "The majority of standard Arm-defined semihosting requests are supported by pyOCD."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/semihosting.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/semihosting.md#supported-requests"
license: "Apache-2.0"
mode: "V"
---

The majority of standard Arm-defined semihosting requests are supported by pyOCD.

- `SYS_OPEN` (0x01): syscall
    - The special file name `:tt` is used to open standard I/O files, per the Arm semihosting specification. The open
    mode selects which standard I/O file is opened. "r" (0) is stdin, "w" (4) is stdout, "a" (8) is stderr. With pyOCD's
    implementation, explicitly opening the standard I/O files is not required.
    - The special file name `:semihosting-features` will open the semihosting feature bits file. Supported
        feature bits are:
        - `SH_EXT_EXIT_EXTENDED` (byte 0 bit 0): =0, meaning `SYS_EXIT_EXTENDED` is not supported
        - `SH_EXT_STDOUT_STDERR` (byte 0 bit 1): =1, meaning both stdout and stderr are supported
    - Standard I/O files opened via this request are only accessible when not routing console to the telnet server.
- `SYS_CLOSE` (0x02): syscall
- `SYS_WRITEC` (0x03): console
- `SYS_WRITE0` (0x04): console
- `SYS_WRITE` (0x05): console for stdout and stderr, otherwise syscall
- `SYS_READ` (0x06): console for stdin, otherwise syscall
- `SYS_READC` (0x07): console
- `SYS_ISTTY` (0x09): syscall
- `SYS_SEEK` (0x0a): syscall
- `SYS_FLEN` (0x0c): syscall
- `SYS_REMOVE` (0x0e): syscall
- `SYS_RENAME` (0x0f): syscall
- `SYS_CLOCK` (0x10): returns the number of centiseconds since pyOCD started (technically, since the semihosting agent
    object was created, so this will not line up with timestamps in pyOCD's log output)
- `SYS_TIME` (0x11): returns the number of seconds since midnight, January 1, 1970
- `SYS_ERRNO` (0x13): syscall
- `SYS_GET_CMDLINE` (0x15): returns the value of the `semihost.commandline` session option. If that option
    is not set, the request fails (returns -1).
- `SYS_HEAPINFO` (0x16): stubbed to return all 0 values


The following semihosting requests are not supported. If invoked, the return code is -1 and pyOCD logs a
warning message, such as "Semihost: unimplemented request pc=\`<x>` r0=\`<y>` r1=\`<z>`".

- `SYS_ISERROR` (0x08)
- `SYS_TMPNAM` (0x0d)
- `SYS_SYSTEM` (0x12)
- `angel_SWIreason_EnterSVC` (0x17)
- `SYS_EXIT` (0x18), also called `angel_SWIreason_ReportException`
- `SYS_EXIT_EXTENDED` (0x20)
- `SYS_ELAPSED` (0x30)
- `SYS_TICKFREQ` (0x31)

The [Arm semihosting operations](https://developer.arm.com/documentation/dui0471/i/semihosting/semihosting-operations?lang=en)
documentation has the full specification of each request.
