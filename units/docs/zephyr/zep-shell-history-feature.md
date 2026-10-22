---
id: "zep-shell-history-feature"
type: "concept"
domain: "debug"
title: "Shell: History Feature"
summary: "This feature enables commands history in the shell. It is activated by: CONFIG_SHELL_HISTORY set to y. History can be accessed using keys: ↑ ↓ or Ctrl+n and Ctrl+p if meta keys are active."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

This feature enables commands history in the shell. It is activated by:
`CONFIG_SHELL_HISTORY` set to `y`. History can be accessed
using keys: `↑` `↓` or `Ctrl+n` and `Ctrl+p`
if meta keys are active.
Number of commands that can be stored depends on size
of `CONFIG_SHELL_HISTORY_BUFFER` parameter.
