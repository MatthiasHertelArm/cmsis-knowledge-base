---
id: "cda-embedded-debugging-troubleshooting-first-line-diagnostic-sweep"
type: "concept"
domain: "debug"
title: "Embedded Debugging Troubleshooting: First-line diagnostic sweep"
summary: "Whenever a tool call hangs, errors out, or returns an unexpected state, run this three-call sequence before retrying:"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@29d444c:docs/agent-resources/troubleshooting/embedded.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/29d444c/docs/agent-resources/troubleshooting/embedded.md#first-line-diagnostic-sweep"
license: "Apache-2.0"
mode: "V"
---

Whenever a tool call hangs, errors out, or returns an unexpected state, run this three-call sequence **before** retrying:

1. `get_session_status` — what state is the session in? (`no-session` / `initializing` / `running` / `stopped` / `unresponsive`)
2. `check_target_connection` — is the probe / GDB server actually responsive?
3. `get_fault_info` — did the target crash?

The session-status output includes a hint for each state. If state is `running` and you needed `stopped`, call `pause_execution`. If state is `unresponsive`, reads answer `PROBE_WEDGED`: see [Reads Fail With PROBE_WEDGED](#reads-fail-with-probe_wedged) before you restart anything.
