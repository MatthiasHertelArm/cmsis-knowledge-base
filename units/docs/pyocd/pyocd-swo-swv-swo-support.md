---
id: "pyocd-swo-swv-swo-support"
type: "concept"
domain: "debug"
title: "SWO/SWV: SWO support"
summary: "PyOCD supports SWO and SWV for those debug probes that support it. This includes CMSIS-DAP, J-Link, and STLink."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/swo_swv.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/swo_swv.md#swo-support"
license: "Apache-2.0"
mode: "V"
---

PyOCD supports SWO and SWV for those debug probes that support it. This includes CMSIS-DAP, J-Link, and STLink.

Be aware that even if a probe type supports SWO, the MCU (and its CPU) must also support SWO, and the board must route
the SWO signal from the MCU to the debug header. In a surprising number of cases, even for silicon vendor evaluation
kits, the probe and MCU support it but the signal simply wasn't routed.

Not all versions of the Arm M-profile architecture support SWO. The Arm v7-M and Arm v8-M Mainline architectures do
support SWO, while the Arm v6-M and Arm v8-M Baseline, architectures do not.


 Core           | Architecture      | Supports SWO
----------------|-------------------|--------------
 Cortex-M0      | v6-M              | -
 Cortex-M0+     | v6-M              | -
 Cortex-M1      | v6-M              | -
 Cortex-M3      | v7-M              | ✓
 Cortex-M4      | v7-M              | ✓
 Cortex-M7      | v7-M              | ✓
 Cortex-M23     | v8.0-M Baseline   | -
 Cortex-M33     | v8.0-M Mainline   | ✓
 Cortex-M55     | v8.1-M Mainline   | ✓
 Cortex-M85     | v8.1-M Mainline   | ✓
