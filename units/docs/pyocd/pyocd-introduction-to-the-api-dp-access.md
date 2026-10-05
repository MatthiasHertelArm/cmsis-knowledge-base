---
id: "pyocd-introduction-to-the-api-dp-access"
type: "concept"
domain: "debug"
title: "Introduction to the API: DP access"
summary: "The DP is controlled through an instance of the DebugPort class (in pyocd.coresight.dap). You get the DebugPort object via the 'dp' attribute of the target instance, i.e., session.board.target.dp."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/python_api.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/python_api.md#dp-access"
license: "Apache-2.0"
mode: "V"
---

The DP is controlled through an instance of the `DebugPort` class (in `pyocd.coresight.dap`). You
get the `DebugPort` object via the 'dp' attribute of the target instance, i.e., `session.board.target.dp`.

The `DebugPort` class has `read_reg(addr)` and `write_reg(addr, data)` methods. 'addr' must be an
integer in the set (0x0, 0x4, 0x8, 0xC).

Example:
```py
x = session.board.target.dp.read_reg(0x4)
session.board.target.dp.write_reg(0x8, 0x1)
```

For completeness, the DebugPort class also has `readDP(addr)`, `writeDP(addr, data)`, `readAP(addr)`, and
`writeAP(addr, data)` methods. They work as described below, except that the `readAP()` and `writeAP()` methods
require the APSEL in the address (i.e., 0x010000fc to read ID of APSEL=1). The AP will automatically be
selected.
