---
id: "pyocd-board-ids-moving-forward"
type: "concept"
domain: "debug"
title: "Board IDs: Moving forward"
summary: "Version 2.1 of the CMSIS-DAP specification adds support for new DAP_Info selectors that identify the board and target. The values returned by these selectors are required to match board and target identifiers in CMSIS-Packs."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/developer/board_ids.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/developer/board_ids.md#moving-forward"
license: "Apache-2.0"
mode: "V"
---

Version 2.1 of the [CMSIS-DAP](https://arm-software.github.io/CMSIS_5/DAP/html/index.html) specification adds support for new [DAP_Info](https://arm-software.github.io/CMSIS_5/DAP/html/group__DAP__Info.html) selectors that identify the board and target. The values returned by these selectors are required to match board and target identifiers in CMSIS-Packs.

PyOCD supports the new CMSIS-DAP v2.1 info selectors and will use them in preference to a board ID if available. This works with any debug probe firmware compatible with CMSIS-DAP. Thus, any new CMSIS-DAP firmware projects should support v2.1 and the new DAP_Info selectors rather than implementing board IDs.

The DAPLink open source CMSIS-DAP firmware has support for the v2.1 identifiers. We recommend using these identifiers rather than a board ID for any new DAPLink based firmware.
