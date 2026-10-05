---
id: "cda-troubleshooting-python-debug-sessi-reading-state"
type: "concept"
domain: "debug"
title: "Troubleshooting Python debug sessions: Reading state"
summary: "Troubleshooting Python debug sessions: Reading state"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@7db44ba:docs/agent-resources/troubleshooting/python.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/7db44ba/docs/agent-resources/troubleshooting/python.md#reading-state"
license: "Apache-2.0"
mode: "V"
---

- Call `list_variable_names` with `scope: "local"` first, then `get_variables_values` with the `variableNames` you need. A listing without names stops at 40 variables per scope and 200 characters per value, and module globals pass that quickly.
- `special variables`, `function variables` and `class variables` are debugpy's groups of dunder names, functions and classes, not variables of the program. After stepping over or out of a call, `(return) <function>` holds the value it returned.
- Values arrive as `repr()` text. For attributes, items or large objects use `evaluate_expression`: `order.items[0].price`, `len(rows)`, `rows[:3]`, `type(obj).__name__`.
- For another frame, take its `frameId` from `get_call_stack` and call `get_frame_variables`; `evaluate_expression` runs in the frame VS Code has in focus, normally the top frame of the stop.
- `evaluate_expression` takes Python, and Python sessions have no `-exec` passthrough. It also executes statements (`x = 0`, `import json`), and each call or property access runs program code: `next(gen)` advances the generator, `queue.get()` removes an item. The other threads stay suspended, so a call that waits for one of them (a lock, a queue, a future) hangs until the tool times out.
- A value of `None` comes back as an empty result, and `print()` inside an expression writes to the Debug Console rather than into the reply. Ask for `repr(x)` or `x is None` instead.
- Values of variables named like credentials (`password`, `token`, `api_key`) arrive as `<redacted: possible secret>`; ask for `len(token)` or `token is None`.
