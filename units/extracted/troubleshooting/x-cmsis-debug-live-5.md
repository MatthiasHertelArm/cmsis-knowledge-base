---
id: "x-cmsis-debug-live-5"
type: "troubleshooting"
domain: "debug"
title: "Target window does not finish or does not answer"
status: "draft"
symptoms: ["WORKER_TIMEOUT", "WINDOW_UNREACHABLE"]
extracted_from: "proc-cmsis-debug-live"
source: "cmsis-debug-live/SKILL.md"
license: "Apache-2.0"
---

`WORKER_TIMEOUT` means the target window is alive but the call did not finish in time and still runs there, often because a picker or dialog waits for the user: call `get_session_status` and ask the user to look at that window before you repeat the call. `WINDOW_UNREACHABLE` means the window did not answer at all, because its extension host is blocked or it closed: call `list_debug_windows`, and if the window is still listed, ask the user to reload it.
