---
id: "zep-additional-zephyr-extension-comman-listing-boards-west-boards"
type: "concept"
domain: "project"
title: "Additional Zephyr extension commands: Listing boards: `west boards`"
summary: "The boards command can be used to list the boards that are supported by Zephyr without having to resort to additional sources of information."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/zephyr-cmds.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/zephyr-cmds.rst"
license: "Apache-2.0"
mode: "V"
---

The `boards` command can be used to list the boards that are supported by
Zephyr without having to resort to additional sources of information.

It can be run by typing::
```
west boards
```
This command lists all supported boards in a default format. If you prefer to
specify the display format yourself you can use the `--format` (or `-f`)
flag::
```
west boards -f "{arch}:{name}"
```
Additional help about the formatting options can be found by running::
```
west boards -h
```
