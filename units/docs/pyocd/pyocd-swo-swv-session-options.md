---
id: "pyocd-swo-swv-session-options"
type: "concept"
domain: "debug"
title: "SWO/SWV: Session options"
summary: "Several session options are used to control and configure SWV:"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/swo_swv.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/swo_swv.md#session-options"
license: "Apache-2.0"
mode: "V"
---

Several session options are used to control and configure SWV:

- `enable_swv` - Flag to enable SWV output.
- `swv_clock` - Optional baud rate for SWO, which defaults to 1 MHz if not set.
- `swv_system_clock` - Required system clock frequency. Used to compute TPIU baud rate divider.
- `swv_raw_enable` - Enable flag for the raw SWV stream server.
- `swv_raw_port` - TCP port number for the raw SWV stream server. The default port is 3443, which is the default port for the Orbuculum client.
- `swv_raw_file` - File path for the raw SWV stream output.
