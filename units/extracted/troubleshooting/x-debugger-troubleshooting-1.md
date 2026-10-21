---
id: "x-debugger-troubleshooting-1"
type: "troubleshooting"
domain: "debug"
title: "GDB client errors that name a consequence, not a cause"
status: "draft"
symptoms: ["EPIPE", "Error getting GDB host-charset"]
extracted_from: "proc-debugger-troubleshooting"
source: "debugger-troubleshooting/SKILL.md"
license: "Apache-2.0"
---

Several of these errors name a consequence, not a cause. A GDB client that dies with `EPIPE` or `Error getting GDB host-charset` is almost never a GDB problem: the server exited first and the client wrote into a dead pipe. Read the server's own last lines in the `gdb-server` records.
