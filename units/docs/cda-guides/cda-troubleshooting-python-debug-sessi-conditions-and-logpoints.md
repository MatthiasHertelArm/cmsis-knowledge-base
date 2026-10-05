---
id: "cda-troubleshooting-python-debug-sessi-conditions-and-logpoints"
type: "concept"
domain: "debug"
title: "Troubleshooting Python debug sessions: Conditions and logpoints"
summary: "Troubleshooting Python debug sessions: Conditions and logpoints"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@7db44ba:docs/agent-resources/troubleshooting/python.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/7db44ba/docs/agent-resources/troubleshooting/python.md#conditions-and-logpoints"
license: "Apache-2.0"
mode: "V"
---

- A `condition` is a Python expression evaluated in the frame at every hit: `i == 100`, `user is None`, `len(queue) > 10`.
- `add_logpoint` fills `{expr}` placeholders from the frame and lets the program run on, but its output goes to the Debug Console, which no tool returns. It serves a user watching that console; for values you need, stop with a conditional breakpoint and read them.
