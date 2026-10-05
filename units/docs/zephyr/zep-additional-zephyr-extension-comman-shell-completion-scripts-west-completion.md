---
id: "zep-additional-zephyr-extension-comman-shell-completion-scripts-west-completion"
type: "concept"
domain: "project"
title: "Additional Zephyr extension commands: Shell completion scripts: `west completion`"
summary: "The completion extension command outputs shell completion scripts that can then be used directly to enable shell completion for the supported shells."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/zephyr-cmds.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/zephyr-cmds.rst"
license: "Apache-2.0"
mode: "V"
---

The `completion` extension command outputs shell completion scripts that can
then be used directly to enable shell completion for the supported shells.

It currently supports the following shells:

- bash
- zsh
- fish
- powershell (board qualifiers only)

Additional instructions are available in the command's help::
```
west help completion
```
