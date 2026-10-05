---
id: "cda-troubleshooting-python-debug-sessi-when-a-breakpoint-never-hits"
type: "concept"
domain: "debug"
title: "Troubleshooting Python debug sessions: When a breakpoint never hits"
summary: "The session ends, or wait_for_stop runs into its timeout; a continue_execution whose wait runs out answers running and leaves the program running, and pause_execution shows the line it is on. Work through the likely reasons:"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@7db44ba:docs/agent-resources/troubleshooting/python.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/7db44ba/docs/agent-resources/troubleshooting/python.md#when-a-breakpoint-never-hits"
license: "Apache-2.0"
mode: "V"
---

The session ends, or `wait_for_stop` runs into its timeout; a `continue_execution` whose wait runs out answers `running` and leaves the program running, and `pause_execution` shows the line it is on. Work through the likely reasons:

- **The code ran before the breakpoint existed.** Module-level code runs once, at import. Add the breakpoint and call `restart_debugging`; breakpoints survive the restart.
- **Another copy of the file runs.** A package installed into site-packages, not in editable mode, runs instead of the workspace source. `get_call_stack` shows the real paths at any stop, and evaluating `__import__('sys').modules['pkg.mod'].__file__` names the loaded file.
- **Another interpreter runs.** Evaluate `__import__('sys').executable` at a stop and set `python` in the entry if it is not the project's environment.
- **`justMyCode` filters the file.** Breakpoints in the standard library or in site-packages are ignored while it is on, and `step_into` skips such frames. Set `"justMyCode": false`.
- **The code runs in another process.** A Python child started through `multiprocessing` or `subprocess` becomes a session of its own; the tools act on the session VS Code has in focus, which `get_session_status` names. With `subProcess` off, or in a non-Python child, it cannot stop at all.
- **The code runs in an untraced thread.** Threads from `threading` are traced; a thread created by native code is not until it calls `debugpy.debug_this_thread()`.
- **The code never runs.** A coroutine nobody awaits or schedules, or a generator nobody iterates, executes no line of its body.
- **The condition fails.** A `condition` that raises counts as false, silently in the case of a misspelt name (`NameError`).
- **The line holds no code.** A breakpoint on a comment or blank line is moved to code or left unbound; put it on a statement.
