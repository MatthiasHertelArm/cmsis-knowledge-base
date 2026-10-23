---
id: "zep-shell-overview"
type: "concept"
domain: "debug"
title: "Shell: Overview"
summary: "This module allows you to create and handle a shell with a user-defined command set. You can use it in examples where more than simple button or LED user interaction is required."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

This module allows you to create and handle a shell with a user-defined command
set. You can use it in examples where more than simple button or LED user
interaction is required. This module is a Unix-like shell with these features:

* Support for multiple instances.
* Advanced cooperation with the logging_api.
* Support for static and dynamic commands.
* Support for dictionary commands.
* Smart command completion with the `Tab` key.
* Built-in commands: `aliases`, `clear`, `shell`,
  `colors`, `echo`, `history` and
  `resize`.
* Viewing recently executed commands using keys: `↑` `↓` or meta keys.
* Text edition using keys: `←`, `→`, `Backspace`,
  `Delete`, `End`, `Home`, `Insert`.
* Support for ANSI escape codes: `VT100` and `ESC[n~` for cursor control
  and color printing.
* Support for editing multiline commands.
* Built-in handler to display help for the commands.
* Support for wildcards: `*` and `?`.
* Support for meta keys.
* Support for getopt and getopt_long.
* Kconfig configuration to optimize memory usage.


**Note:** Some of these features have a significant impact on RAM and flash usage, but many can be disabled when not needed.  To default to options which favor reduced RAM and flash requirements instead of features, you should enable `CONFIG_SHELL_MINIMAL` and selectively enable just the features you want.
