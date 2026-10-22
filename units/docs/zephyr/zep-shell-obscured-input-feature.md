---
id: "zep-shell-obscured-input-feature"
type: "concept"
domain: "debug"
title: "Shell: Obscured Input Feature"
summary: "With the obscured input feature, the shell can be used for implementing a login prompt or other user interaction whereby the characters the user types should not be revealed on screen, such as when entering a password."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

With the obscured input feature, the shell can be used for implementing a login
prompt or other user interaction whereby the characters the user types should
not be revealed on screen, such as when entering a password.

Once the obscured input has been accepted, it is normally desired to return the
shell to normal operation.  Such runtime control is possible with the
`shell_obscure_set` function.

An example of login and logout commands using this feature is located in
`samples/subsys/shell/shell_module/src/main.c` and the config file
`samples/subsys/shell/shell_module/prj_login.conf`.

This feature is activated upon startup by `CONFIG_SHELL_START_OBSCURED`
set to `y`. With this set either way, the option can still be controlled later
at runtime. `CONFIG_SHELL_CMDS_SELECT` is useful to prevent entry
of any other command besides a login command, by means of the
`shell_set_root_cmd` function. Likewise, `CONFIG_SHELL_PROMPT_UART`
allows you to set the prompt upon startup, but it can be changed later with the
`shell_prompt_change` function.
