---
id: "cda-troubleshooting-python-debug-sessi-starting-the-session"
type: "concept"
domain: "debug"
title: "Troubleshooting Python debug sessions: Starting the session"
summary: "Troubleshooting Python debug sessions: Starting the session"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@7db44ba:docs/agent-resources/troubleshooting/python.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/7db44ba/docs/agent-resources/troubleshooting/python.md#starting-the-session"
license: "Apache-2.0"
mode: "V"
---

- Set the first breakpoints with `add_breakpoint` before `start_debugging`. The program does not stop on entry, so a short script can finish before a breakpoint added later could ever matter.
- With an entry in `.vscode/launch.json`, pass its name as `configurationName`. `workingDirectory` picks the workspace folder whose `launch.json` is read, and the entry runs exactly as written.
- `configurationName: "Default Configuration"` builds the launch from the file instead: `fileFullPath` runs as a script without arguments, in the file's own folder (not in `workingDirectory`), with its output in the integrated terminal. Leaving `configurationName` out opens a picker for the user, and the call waits for their choice.
- No tool returns what the program prints, whether it lands in the terminal or in the Debug Console. Work out what happened from the state at a stop.
- After `start_debugging` the program is running: `wait_for_stop` waits for the first breakpoint, while `continue_execution` refuses until the program has stopped.
- Settings that decide whether your breakpoints can be reached belong in a `launch.json` entry (type `debugpy`, or the older `python`):
  - `program` runs a script path; `module` runs `python -m pkg.cli`. Code with package-relative imports needs `module` and a `cwd` above the package.
  - `args`, `cwd`, `env` and `envFile`: a missing argument, file or variable often ends the run before the interesting code.
  - `python`: the interpreter, such as the project's `.venv/bin/python`; without it the interpreter selected in VS Code runs.
  - `justMyCode` (on unless configured otherwise), `subProcess` (on: Python child processes are debugged as well) and `stopOnEntry`.
