---
id: "x-cmsis-bootstrap-3"
type: "concept"
domain: "project"
title: "Which window cmsis_action open_solution uses"
status: "draft"
extracted_from: "proc-cmsis-bootstrap"
source: "cmsis-bootstrap/SKILL.md"
license: "Apache-2.0"
---

A folder that a window already has open is used there, and the solution is made the active one. Any other folder opens in a new window. The window you started in stays as it is; this session's later calls go to the new window. `list_debug_windows` shows both.
