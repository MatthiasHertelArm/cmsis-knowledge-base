---
id: "zep-extensions-disabling-extension-commands"
type: "concept"
domain: "project"
title: "Extensions: Disabling Extension Commands"
summary: "To disable support for extension commands, set the commands.allow_extensions configuration option to false. To set this globally for whenever you run west, use:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/extensions.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/extensions.rst"
license: "Apache-2.0"
mode: "V"
---

To disable support for extension commands, set the `commands.allow_extensions`
configuration option to `false`. To set this
globally for whenever you run west, use:

```console

west config --global commands.allow_extensions false
```
If you want to, you can then re-enable them in a particular :term:`west
workspace` with:

```console

west config --local commands.allow_extensions true
```
Note that the files containing extension commands are not imported by west
unless the commands are explicitly run. See below for details.
