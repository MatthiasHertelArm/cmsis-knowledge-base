---
id: "pyocd-debug-probes"
type: "concept"
domain: "debug"
title: "Debug probes"
summary: "The debug probe is the interface between pyOCD and the target, and it drives the SWD or JTAG signals that control the target."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/debug_probes.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/debug_probes.md"
license: "Apache-2.0"
mode: "V"
---

The debug probe is the interface between pyOCD and the target, and it drives the SWD or JTAG signals that control
the target. By way of the connection between the debug probe and target, selecting the debug probe implicitly controls
which target pyOCD debugs.

There are two major flavours of debug probe:

- **On-board probes**. Many evaluation boards include an on-board debug probe, so you can plug it in and start using
    it without needing any other devices.
- **Standalone probes**. For debugging custom hardware you typically need a standalone probe that connects via an
    SWD/JTAG cable. Most commercially available debug probes, such as the SEGGER J-Link or Arm ULINKplus, are standalone.


PyOCD uses debug probe driver plug-ins to enable support for different kinds of debug probes. It comes with plug-ins for
these types of debug probes:

 Plug-in Name        | Debug Probe Type
---------------------|--------------------
`cmsisdap`           | [CMSIS-DAP](http://www.keil.com/pack/doc/CMSIS/DAP/html/index.html)
`picoprobe`          | Raspberry Pi [Picoprobe](https://github.com/raspberrypi/picoprobe)
`jlink`              | [SEGGER](https://segger.com/) [J-Link](https://www.segger.com/products/debug-trace-probes/)
`stlink`             | [STMicro](https://st.com/) [STLinkV2](https://www.st.com/en/development-tools/st-link-v2.html) and [STLinkV3](https://www.st.com/en/development-tools/stlink-v3set.html)
`remote`             | pyOCD [remote debug probe client]({% link _docs/remote_probe_access.md %})

Additional debug probe plugins are available as Python packages through [PyPI](https://pypi.python.org), and
can be installed with pip:

 Plug-in Name   | Package           | Debug Probe Type
----------------|-------------------|--------------------
`pemicro`       | pyocd-pemicro     | [PE Micro](https://pemicro.com/) Cyclone and Multilink.
