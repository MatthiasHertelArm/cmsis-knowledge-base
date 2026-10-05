---
id: "pyocd-installing-pe-micro-probe-support"
type: "concept"
domain: "debug"
title: "Installing: PE Micro probe support"
summary: "Support for Cyclone and/or Multilink debug probes by PE Micro is available in a probe driver plug-in that is a separate package from pyOCD. There are two ways to install the PE Micro probe plug-in."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/installing.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/installing.md#pe-micro-probe-support"
license: "Apache-2.0"
mode: "V"
---

Support for Cyclone and/or Multilink debug probes by [PE Micro](https://pemicro.com/) is available in a probe
driver plug-in that is a separate package from pyOCD. There are two ways to install the PE Micro probe plug-in.
Either substitute `pyocd[pemicro]` for `pyocd` in the commands above, or separately install `pyocd-pemicro`
using pip.
