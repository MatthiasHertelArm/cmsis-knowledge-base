---
id: "zep-shell-tab-feature"
type: "concept"
domain: "debug"
title: "Shell: Tab Feature"
summary: "The Tab button can be used to suggest commands or subcommands. This feature is enabled by CONFIG_SHELL_TAB set to y. It can also be used for partial or complete auto-completion of commands."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

The Tab button can be used to suggest commands or subcommands. This feature
is enabled by `CONFIG_SHELL_TAB` set to `y`.
It can also be used for partial or complete auto-completion of commands.
This feature is activated by
`CONFIG_SHELL_TAB_AUTOCOMPLETION` set to `y`.
When user starts writing a command and presses the `Tab` button then
the shell will do one of 3 possible things:

* Autocomplete the command.
* Prompts available commands and if possible partly completes the command.
* Will not do anything if there are no available or matching commands.
