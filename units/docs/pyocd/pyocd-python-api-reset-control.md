---
id: "pyocd-python-api-reset-control"
type: "concept"
domain: "debug"
title: "python api: Reset control"
summary: "To control reset, there are several options."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/python_api.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/python_api.md#reset-control"
license: "Apache-2.0"
mode: "V"
---

To control reset, there are several options.

`DebugPort` has methods for driving the hardware reset signal:
- `DebugPort.reset()`, asks the debug probe to perform a hardware reset of the target.
- `DebugPort.assert_reset(asserted)` to directly control the nRESET signal. Pass True to drive
  nRESET low, False to drive high.

A wider range of reset options is provided by these `Target` methods:
- `Target.reset(reset_type=None)`. Normally performs a software reset unless the optional parameter
  is set to False.
- `Target.reset_and_halt(reset_type=None)` to perform a halting reset. Again, the reset defaults
  to software but may be set to hardware.

The `reset_type` parameter on the `Target` reset methods can be set to one of the `Target.ResetType`
enums:
- `ResetType.DEFAULT`: Uses the core's default reset method. For pack targets `defaultResetSequence` is used.
For internal targets, the default is mapped to `ResetType.SYSTEM`, unless `default_reset_type`
property is explicitly set.
- `ResetType.HARDWARE`: Execute `ResetHardware` debug sequence for pack targets, if the sequence doesn't exist,
hardware reset using the nSRST signal is used. The same mapping applies for internal targets.
- `ResetType.SYSTEM`: Execute `ResetSystem` debug sequence for pack targets, if the sequence doesn't exist,
software reset using SYSRESETREQ is used. The same mapping applies for internal targets.
- `ResetType.CORE`: Execute `ResetProcessor` debug sequence for pack targets, if the sequence doesn't exist,
software reset using VECTRESET is used. The same mapping applies for internal targets.
- `ResetType.NSRST`: Hardware reset using the nSRST signal.
- `ResetType.SYSRESETREQ`: Software reset using SYSRESETREQ, which usually resets the entire system
on most MCUs.
- `ResetType.VECTRESET`: Software reset using VECTRESET, only available on v7-M targets. This
resets only the core itself. If requested on non-v7-M targets, it will fall back to `ResetType.EMULATED`.
- `ResetType.EMULATED`: Restores the core to reset conditions by writing registers. However, this
will not trigger a reset vector catch.

The `CortexM` objects have a `default_reset_type` property that lets you control the overall default reset type.
Property value can be any one of the `ResetType` enums.

Another option for performing a halting reset is by setting vector catch with the target's `set_vector_catch()`
method, then using a normal reset. This has the benefit of always halting at reset, if you leave the
vector catch enabled.

Example timed reset using the DP:
```
import time

dp = session.board.target.dp

# Timed reset.
dp.assert_reset(True)
time.sleep(1.0)
dp.assert_reset(False)
```
