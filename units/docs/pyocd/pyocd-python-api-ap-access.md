---
id: "pyocd-python-api-ap-access"
type: "concept"
domain: "debug"
title: "python api: AP access"
summary: "CoreSight APs are represented with AccessPort classes defined in pyocd.coresight.ap. These include the MEMAP subclass and AHBAP subclass of that."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/python_api.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/python_api.md#ap-access"
license: "Apache-2.0"
mode: "V"
---

CoreSight APs are represented with `AccessPort` classes defined in `pyocd.coresight.ap`. These include
the `MEM_AP` subclass and `AHB_AP` subclass of that.

To get the AP objects you can use the 'aps' attribute of the `DebugPort`. This attribute is a dict
with the keys being the APSEL number and values being AccessPort instances. For instance, use
`session.board.target.aps[1]` to get the AP with APSEL=1, assuming it exists (if not, you'll get an
`IndexError` exception).

`AccessPort` also has `read_reg(addr)` and `write_reg(addr, data)` methods. For these methods, `addr` is
an integer of the register offset. Note that you do not need to include the APSEL in the address, and
you do not need to modify the DP's SELECT register prior to accessing AP registers. The AP will
automatically be selected in the DP as required.

The `MEM_AP`/`AHB_AP` class has the memory access methods that are available on
the target, but the access is, of course, performed through that specific AP. This is particularly
useful for multicore devices or Cortex-A class devices.

Example showing access of the proprietary MDM-AP of NXP Kinetis MCUs:
```py
mdm_ap = session.board.target.dp.aps[1]
idr = mdm_ap.read_reg(0xfc) # Read IDR.
mdm_ap.write_reg(0x4, 0x1)
```
