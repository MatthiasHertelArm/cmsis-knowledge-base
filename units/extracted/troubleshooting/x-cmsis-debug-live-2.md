---
id: "x-cmsis-debug-live-2"
type: "troubleshooting"
domain: "debug"
title: "Probe wedged during fault read"
status: "draft"
symptoms: ["PROBE_WEDGED"]
extracted_from: "proc-cmsis-debug-live"
source: "cmsis-debug-live/SKILL.md"
license: "Apache-2.0"
---

If a fault read answers PROBE_WEDGED, the debug port no longer answers (DHCSR could not be read either): stop reading and follow the hint. An attach session reconnects with cmsis_action detach, then attach, without a reset. A load_and_debug session owns its GDB server: the user restarts that server without a reset, and you cmsis_action attach. Only then restart_debugging, reset or load_and_debug again.
