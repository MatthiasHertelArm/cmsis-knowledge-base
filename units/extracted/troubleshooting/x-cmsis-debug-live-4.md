---
id: "x-cmsis-debug-live-4"
type: "troubleshooting"
domain: "debug"
title: "PROBE_WEDGED during a fault read"
status: "draft"
symptoms: ["PROBE_WEDGED", "INVALID_ARGUMENT"]
extracted_from: "proc-cmsis-debug-live"
source: "cmsis-debug-live/SKILL.md"
---

If a fault read answers `PROBE_WEDGED`, the debug port no longer answers (DHCSR could not be read either): stop reading and follow the hint. An attach session reconnects with `cmsis_action detach`, then `attach`, without a reset. A `load_and_debug` session owns its GDB server; `restart_debugging` and `load_and_debug` re-flash and reset, so to keep the fault state the user restarts the server without a reset and you `cmsis_action attach`. Never start a GDB server yourself. `INVALID_ARGUMENT` "the debug port answers" means only that address is unreadable. A lockup note means the core faulted inside a fault handler.
