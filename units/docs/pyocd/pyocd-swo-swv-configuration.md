---
id: "pyocd-swo-swv-configuration"
type: "concept"
domain: "debug"
title: "SWO/SWV: Configuration"
summary: "If enableswv is true, pyOCD will set up ITM and TPIU to output ITM stimulus ports over SWO at the specified baud rate. Currently, semihosting must also be enabled for SWV to work, so the enablesemihosting option must be on."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/swo_swv.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/swo_swv.md#configuration"
license: "Apache-2.0"
mode: "V"
---

If `enable_swv` is true, pyOCD will set up ITM and TPIU to output ITM stimulus ports over SWO at the specified baud
rate.  Currently, [semihosting]({% link _docs/semihosting.md %}) must also be enabled for SWV to work, so the
`enable_semihosting` option must be on. A thread reads the data from the probe in the background and parses it.

The SWV stream from ITM port 0 will be output to the semihosting console (see the [Routing]({% link _docs/semihosting.md
%}#routing) section of the [semihosting documentation]({% link _docs/semihosting.md %})), which is either the telnet
server or stdout depending on the `semihost_console_type` option.




An example of running the gdbserver with SWV output is:

```
pyocd gdb -S -Oenable_swv=1 -Oswv_system_clock=80000000 -Osemihost_console_type=console
```

This will turn on semihosting and SWV with the default 1 MHz baud rate, an 80 MHz system clock, and output to stdout.
