---
id: "zep-shell-wildcards-feature"
type: "concept"
domain: "debug"
title: "Shell: Wildcards Feature"
summary: "The shell module can handle wildcards. Wildcards are interpreted correctly when expanded command and its subcommands do not have a handler."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

The shell module can handle wildcards. Wildcards are interpreted correctly
when expanded command and its subcommands do not have a handler. For example,
if you want to set logging level to `err` for the `app` and `app_test`
modules you can execute the following command:

```none

log enable err a*
```
This feature is activated by `CONFIG_SHELL_WILDCARD` set to `y`.


**Note:** When the wildcard feature is enabled, the characters `*` and `?` cannot be used as normal characters in commands or arguments.
