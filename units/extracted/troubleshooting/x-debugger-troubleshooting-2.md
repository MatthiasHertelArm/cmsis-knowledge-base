---
id: "x-debugger-troubleshooting-2"
type: "troubleshooting"
domain: "debug"
title: "Something already holds the probe or the GDB port"
status: "draft"
symptoms: ["Waiting for a debug probe matching unique ID", "Failed to open listener port 3333", "gdbserver exited with code 254"]
extracted_from: "proc-debugger-troubleshooting"
source: "debugger-troubleshooting/SKILL.md"
license: "Apache-2.0"
---

`cmsis_action { action: 'status' }` lists this window's CMSIS tasks. A `CMSIS Run` task that is alive holds the probe and the GDB port: `cmsis_action { action: 'stop_run' }` ends it, then repeat the call.
`list_debug_windows` shows whether another VS Code window has a debug session on the same probe.
A process outside VS Code can hold the port too, and it is often a different kind of backend than the one you are starting: an FVP bridge or a model left over on 3333 blocks a J-Link or pyOCD GDB server with exactly the message above. These commands only look at the host and are allowed:

lsof -nP -iTCP:3333 -sTCP:LISTEN
ps -ww -o pid,etime,command -p <PID>

Identify the process before anything is stopped: it may be a session the user wants. Tell the user what holds the port and let them decide.
