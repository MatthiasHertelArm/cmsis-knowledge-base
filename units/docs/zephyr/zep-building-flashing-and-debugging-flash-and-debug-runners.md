---
id: "zep-building-flashing-and-debugging-flash-and-debug-runners"
type: "concept"
domain: "project"
title: "Building, Flashing and Debugging: Flash and debug runners"
summary: "The flash and debug commands use Python wrappers around various flash-debug-host-tools. These wrappers are all defined in a Python library at scripts/west_commands/runners. Each wrapper is called a runner. Runners can flash and/or debug Zephyr programs."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/build-flash-debug.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/build-flash-debug.rst"
license: "Apache-2.0"
mode: "V"
---

The flash and debug commands use Python wrappers around various
flash-debug-host-tools. These wrappers are all defined in a Python
library at `scripts/west_commands/runners`. Each wrapper is
called a *runner*. Runners can flash and/or debug Zephyr programs.

The central abstraction within this library is `ZephyrBinaryRunner`, an
abstract class which represents runners. The set of available runners is
determined by the imported subclasses of `ZephyrBinaryRunner`.
`ZephyrBinaryRunner` is available in the `runners.core` module; individual
runner implementations are in other submodules, such as `runners.nrfjprog`,
`runners.openocd`, etc.
