---
id: "x-pyocd-detect-debug-topology-1"
type: "pattern"
domain: "bring-up"
title: "Stop a pyOCD gdbserver that a workflow started"
status: "draft"
extracted_from: "proc-pyocd-detect-debug-topology"
source: "bring-up/pyocd-detect-debug-topology/SKILL.md"
---

Unless the user needs it to remain running, request the host's most graceful supported interrupt and wait up to 10 seconds for exit: Ctrl+C / `CTRL_C_EVENT` on Windows or `SIGINT` on POSIX. If the server is still running after 10 seconds, force-terminate only that server process using the host mechanism: `Stop-Process -Force` on Windows or `SIGKILL` on POSIX.
