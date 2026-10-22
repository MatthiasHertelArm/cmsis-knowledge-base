---
id: "cda-cmsis-developer-assistant-tool-con-cmsis-developer-assistant-tool-rules"
type: "concept"
domain: "debug"
title: "CMSIS Developer Assistant tool contract: CMSIS Developer Assistant tool rules"
summary: "Only the user can lift a rule, by asking for the specific command."
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@29d444c:docs/agent-resources/tool-contract.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/29d444c/docs/agent-resources/tool-contract.md#cmsis-developer-assistant-tool-rules"
license: "Apache-2.0"
mode: "V"
---

Only the user can lift a rule, by asking for the specific command.

- Talk to the board only through the cmsis-developer-assistant MCP tools. Never run `pyocd`, `gdb`, `JLinkExe`, `JLinkGDBServer` or `openocd` from a shell, and never install pyOCD.
- Build, load, erase, run and debug with `cmsis_action`; program with `flash`. Run `cbuild`, `csolution` or `cpackget` in a shell only when the user asks or a CMSIS skill step names the command.
- Serial I/O only through the `serial_*` tools, not `screen`, PuTTY, a read of the port or a serial script.
- Manuals, datasheets and register meanings through the documentation tools; use the web only to find a PDF URL for `fetch_doc`, and never read a PDF into your context.
- Symbol, section, memory-usage and build-log questions through the build-artefact tools, not `nm`, `size` or a grep of the map file.
- If a tool you need is not in your tool list, name the setting that enables it (`cmsis-developer-assistant.packDocs.enabled` or `cmsis-developer-assistant.buildInfo.enabled`), not a shell command.
- The control server and the registry files are internal: never call or read them. With several windows, use `list_debug_windows` and `select_debug_window`.
- A running target rejects reads and steps: call `pause_execution` first.
- When one call fails twice the same way, follow the hints of `get_session_status` and `get_recent_problems`, never a shell command. A value GDB cannot read is an answer, not a failure. Before you finish, leave the target running; ask the user only for what no tool can do.
<!-- cmsis-developer-assistant:rules:end -->

<!-- cmsis-developer-assistant:shell-to-tool:begin -->
