---
id: "cda-troubleshooting-python-debug-sessi-exceptions"
type: "concept"
domain: "debug"
title: "Troubleshooting Python debug sessions: Exceptions"
summary: "Troubleshooting Python debug sessions: Exceptions"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@29d444c:docs/agent-resources/troubleshooting/python.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/29d444c/docs/agent-resources/troubleshooting/python.md#exceptions"
license: "Apache-2.0"
mode: "V"
---

- By default debugpy stops only on uncaught exceptions; "Raised Exceptions" and "User Uncaught Exceptions" are off. These switches live in VS Code's Breakpoints view and no tool sets them, so ask the user to tick one, or break on the `raise` or on the first line of the `except` block.
- An exception that a framework catches (a test runner, a web server, an `except Exception:` that logs and carries on) is never uncaught and never stops the run.
- `SystemExit` with a non-zero code, as from `sys.exit(1)` or an `argparse` error, stops like an uncaught exception; exit code 0 does not.
- Stopped on an exception, the frame's locals contain `__exception__`, a tuple of type, value and traceback: evaluate `repr(__exception__[1])`, then walk `get_call_stack` to the frame that raised.
