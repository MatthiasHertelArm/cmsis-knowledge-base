---
id: "zep-using-zephyr-without-west-flashing-and-debugging"
type: "concept"
domain: "project"
title: "Using Zephyr without west: Flashing and Debugging"
summary: "Flashing and debugging are done with the west flash, west debug, west debugserver, west attach and west rtt commands, which are documented in west-build-flash-debug. These commands require west, so they are not available if you are using Zephyr without it."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/without-west.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/without-west.rst"
license: "Apache-2.0"
mode: "V"
---

Flashing and debugging are done with the `west flash`, `west debug`,
`west debugserver`, `west attach` and `west rtt` commands, which are
documented in west-build-flash-debug. These commands require west, so
they are not available if you are using Zephyr without it.

Without west, you can still flash and debug using any of the
flash-debug-host-tools which work for your board (and which those west
commands wrap), but you will have to invoke them yourself, with the right
options for your board and application.
