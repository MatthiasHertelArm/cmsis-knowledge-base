---
id: "pyocd-swo-swv"
type: "concept"
domain: "debug"
title: "SWO/SWV"
summary: "The Arm Cortex-M and CoreSight architectures support a single-wire trace output called Serial Wire Output (SWO). This SWO trace feature can be used for everything from printf debugging to PC-sampling based profiling and various performance measurements."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/swo_swv.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/swo_swv.md"
license: "Apache-2.0"
mode: "V"
---

The Arm Cortex-M and CoreSight architectures support a single-wire trace output called Serial Wire Output (SWO).
This SWO trace feature can be used for everything from printf debugging to PC-sampling based profiling and various
performance measurements.

SWO supports two wire protocols, asynchronous UART and Manchester encoding, although in practise UART is used almost
exclusively. (SWO is also available as a standalone CoreSight component, but this is relatively rare.)

The Arm Cortex-M DWT and ITM core peripherals generate packets that can be output over SWO when a configurable set of
events occur. The combination of DWT/ITM packets transmitted via SWO is called the Serial Wire Viewer (SWV). A common
use case for SWV is printf-style log output, so much so that "SWV" has more or less come to mean exactly that.

The major features are:

- The gdbserver supports SWV printf-style log output to console or telnet, muxed with semihosting stdout.
- Raw SWO data can be served through a TCP port while the gdbserver is running, allowing other tools such as
    [Orbuculum](https://github.com/orbcode/orbuculum) to process it.
- The Python API has a set of classes for building a trace event data flow graph.
