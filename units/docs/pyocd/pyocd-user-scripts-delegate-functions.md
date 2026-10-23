---
id: "pyocd-user-scripts-delegate-functions"
type: "concept"
domain: "debug"
title: "User scripts: Delegate functions"
summary: "This section documents all functions that user scripts can provide to modify pyOCD's behaviour. Some are simply notifications, while others allow for overriding of default behaviour. Collectively, these are called delegate functions."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/user_scripts.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/user_scripts.md#delegate-functions"
license: "Apache-2.0"
mode: "V"
---

This section documents all functions that user scripts can provide to modify pyOCD's behaviour. Some are simply
notifications, while others allow for overriding of default behaviour. Collectively, these are called delegate functions.

All parameters of user script delegate functions are optional. Parameters can be declared in any order, and
those that are not needed can be excluded. In fact, most parameters are not necessary because the same objects
are available as [script globals](#script_globals), for instance `session` and `target`.

Those parameters that are present must have names matching the specification below, and there must not be
additional unspecified, required parameters (those without a default value). Extra optional parameters are
allowed but will never be passed any value other than the default, unless you call the function yourself from
within the script.

_Note:_ Delegate functions override CMSIS-Pack debug sequences. See the [debug sequence documentation]({% link _docs/open_cmsis_pack_support.md %}#debug-access-sequences) for more details.


### will_connect

Pre-init notification for the board.
```
will_connect(board: Board) -> None
```

**Parameters** \
*board* - A `Board` instance that is about to be initialized. \
**Result** \
Ignored.

### did_connect

Post-initialization notification for the board.
```
did_connect(board: Board) -> None
```

**Parameters** \
*board* - A `Board` instance. \
**Result** \
Ignored.

### will_init_target

Hook to review and modify init call sequence prior to execution.
```
will_init_target(target: SoCTarget, init_sequence: CallSequence) -> None
```

**Parameters** \
*target* - An `SoCTarget` object about to be initialized. \
*init_sequence* - The `CallSequence` that will be invoked. Because call sequences are
  mutable, this parameter can be modified before return to change the init calls. \
**Result** \
Ignored.

### did_init_target

Post-initialization notification.
```
did_init_target(target: SoCTarget) -> None
```

**Parameters** \
*target* - An `SoCTarget` object. \
**Result** \
Ignored.

### unlock_device

Hook to perform any required unlock sequence.
```
unlock_device(target: SoCTarget) -> None
```

**Parameters** \
*target* - An `SoCTarget` object. \
**Result** \
Ignored.

Called after the DP is initialised but prior to discovery. This hook delegate can be used to unlock debug
access to the target. It can also be used to perform other pre-discovery actions.

Note that because this hoook is called prior to discovery, APs and cores are not yet created. This means
that any register accesses must be performed through the DP's methods. (However, it's possible to create
a temporary instance of 'AccessPort' or one of its subclasses, such as `MEM_AP`.)

### will_start_debug_core

Notification hook for before core debug is enabled.

```
will_start_debug_core(core: CoreTarget) -> None
```

**Parameters** \
*core* - A `CoreTarget` object about to be initialized. \
**Result** \
Ignored.

This hook is called during connection, prior to any register accesses being performed on the
indicated core (aside from the CoreSight peripheral ID registers that were read to identify
the core's presence during discovery).

### start_debug_core

Hook to enable debug for the given core.
```
start_debug_core(core: CoreTarget) -> Optional[bool]
```

**Parameters** \
*core* - A `CoreTarget` object about to be initialized. \
**Result** \
*True* Do not perform the normal procedure to start core debug. \
*False/None* Continue with normal behaviour.

### did_start_debug_core

Notification hook that core debug has been enabled.
```
did_start_debug_core(core: CoreTarget) -> None
```

**Parameters** \
*core* - A `CoreTarget` object. \
**Result** \
Ignored.

This hook method is called once a debug has been enabled for a core, and it has been fully
identified.

### will_stop_debug_core

Pre core disconnect notification hook for the core.
```
will_stop_debug_core(core: CoreTarget) -> None
```

**Parameters** \
*core* - A `CoreTarget` object. \
**Result** \
Ignored.

### stop_debug_core

Core debug disable hook.
```
stop_debug_core(core: CoreTarget) -> Optional[bool]
```

**Parameters** \
*core* - A `CoreTarget` object. \
**Result** \
*True* Do not perform the normal procedure to disable core debug. \
*False/None* Continue with normal behaviour.

This delegate is only called if resuming the core on disconnect, e.g. the `resume_on_disconnect` session
option is True. Therefore, the delegate should ensure that the core has properly resumed execution if it
returns True.

### did_stop_debug_core

Post core disconnect notification hook for the core.
```
did_stop_debug_core(core: CoreTarget) -> None
```

**Parameters** \
*core* - A `CoreTarget` object. \
**Result** \
Ignored.

### will_disconnect

Pre-disconnect notification.
```
will_disconnect(target: SoCTarget, resume: bool) -> None
```

**Parameters** \
*target* - An `SoCTarget` object. \
*resume* - The value of the `disconnect_on_resume` option. \
**Result** \
Ignored.

### did_disconnect

Post-disconnect notification.
```
did_disconnect(target: SoCTarget, resume: bool) -> None
```

**Parameters** \
*target* - An `SoCTarget` object. \
*resume* - The value of the `disconnect_on_resume` option. \
**Result** \
Ignored.

### will_reset

```
will_reset(core: CoreTarget, reset_type: Target.ResetType) -> Optional[bool]
```
Pre-reset hook.

**Parameters** \
*core* - A `CoreTarget` instance. \
*reset_type* - One of the `Target.ResetType` enumerations. \
**Result** \
*True* The hook performed the reset.  \
*False/None* Caller should perform the normal reset procedure.

### did_reset

Post-reset notification.
```
did_reset(core: CoreTarget, reset_type: Target.ResetType) -> None
```

**Parameters** \
*core* - A `CoreTarget` instance. \
*reset_type* - One of the `Target.ResetType` enumerations. \
**Result** \
Ignored.

### set_reset_catch

Hook to prepare target for halting on reset.
```
set_reset_catch(core: CoreTarget, reset_type: Target.ResetType) -> Optional[bool]
```

**Parameters** \
*core* - A `CoreTarget` instance. \
*reset_type* - One of the `Target.ResetType` enumerations. \
**Result** \
*True* This hook handled setting up reset catch, caller should do nothing. \
*False/None* Perform the default reset catch set using vector catch.

### clear_reset_catch

Hook to clean up target after a reset and halt.
```
clear_reset_catch(core: CoreTarget, reset_type: Target.ResetType) -> None
```

**Parameters** \
*core* - A `CoreTarget` instance. \
*reset_type* - One of the `Target.ResetType` enumerations. \
**Result** \
Ignored.

### mass_erase

Hook to override mass erase.
```
mass_erase(target: SoCTarget) -> Optional[bool]
```

**Parameters** \
*target* - An `SoCTarget` object. \
**Result** \
*True* Indicate that mass erase was performed by the hook. \
*False/None* Mass erase was not overridden and the caller should proceed with the standard mass erase procedure.

### trace_start

Notification to prepare for tracing the target.
```
trace_start(target: SoCTarget, mode: int) -> None
```

**Parameters** \
*target* - A `CoreSightTarget` object. \
*mode* - The trace mode. Currently always 0 to indicate SWO. \
*Result* - Ignored.

### trace_stop

Notification to clean up after tracing the target.
```
trace_stop(target: SoCTarget, mode: int) -> None
```

**Parameters** \
*target* - A `CoreSightTarget` object. \
*mode* - The trace mode. Currently always 0 to indicate SWO. \
**Result** \
Ignored.

### trace_capture

Notification to capture trace data.
```
trace_capture(target: SoCTarget, mode: int) -> None
```

**Parameters** \
*target* - A `CoreSightTarget` object. \
*mode* - The trace mode. Currently always 0 to indicate SWO. \
**Result** \
Ignored.

### trace_flush

Notification to flush trace data.
```
trace_flush(target: SoCTarget, mode: int) -> None
```

**Parameters** \
*target* - A `CoreSightTarget` object. \
*mode* - The trace mode. Currently always 0 to indicate SWO. \
**Result** \
Ignored.
