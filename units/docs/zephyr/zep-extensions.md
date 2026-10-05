---
id: "zep-extensions"
type: "concept"
domain: "project"
title: "Extensions"
summary: "West is \"pluggable\": you can add your own commands to west without editing its source code. These are called west extension commands, or just \"extensions\" for short."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/extensions.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/extensions.rst"
license: "Apache-2.0"
mode: "V"
---

West is "pluggable": you can add your own commands to west without editing its
source code. These are called **west extension commands**, or just "extensions"
for short. Extensions show up in the `west --help` output in a special
section for the project which defines them. This page provides general
information on west extension commands, and has a tutorial for writing your
own.

Some commands you can run when using west with Zephyr, like the ones used to
build, flash, and debug and the
ones described here, are extensions. That's why
help for them shows up like this in `west --help`:

```none

extension commands from project manifest (path: zephyr):
  completion:           display shell completion scripts
  boards:               display information about supported boards
  shields:              display list of supported shields
  build:                compile a Zephyr application
  twister:              west twister wrapper
  sign:                 sign a Zephyr binary for bootloader chain-loading
  flash:                flash and run a binary on a board
  debug:                flash and interactively debug a Zephyr application
  debugserver:          connect to board and launch a debug server
  attach:               interactively debug a board
  ...
```
See `zephyr/scripts/west-commands.yml` and the
`zephyr/scripts/west_commands` directory for the implementation details.
