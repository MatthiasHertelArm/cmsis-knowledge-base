---
id: "cda-troubleshooting-python-debug-sessi-checklist"
type: "concept"
domain: "debug"
title: "Troubleshooting Python debug sessions: Checklist"
summary: "Troubleshooting Python debug sessions: Checklist"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@29d444c:docs/agent-resources/troubleshooting/python.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/29d444c/docs/agent-resources/troubleshooting/python.md#checklist"
license: "Apache-2.0"
mode: "V"
---

- [ ] Breakpoints set before `start_debugging`, on statements.
- [ ] The interpreter and the file that run are the ones you expect (`sys.executable`, paths in `get_call_stack`).
- [ ] `justMyCode` off when the cause may lie in library code.
- [ ] The session in focus is the process you mean (`get_session_status`).
- [ ] Values read with `list_variable_names`, then `get_variables_values`; expressions free of side effects unless the change is the experiment.
- [ ] `clear_all_breakpoints` once the cause is confirmed.
