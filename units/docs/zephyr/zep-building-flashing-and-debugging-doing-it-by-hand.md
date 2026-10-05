---
id: "zep-building-flashing-and-debugging-doing-it-by-hand"
type: "concept"
domain: "project"
title: "Building, Flashing and Debugging: Doing it By Hand"
summary: "If you prefer not to use West to flash or debug your board, simply inspect the build directory for the binaries output by the build system."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/build-flash-debug.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/build-flash-debug.rst"
license: "Apache-2.0"
mode: "V"
---

If you prefer not to use West to flash or debug your board, simply
inspect the build directory for the binaries output by the build
system. These will be named something like `zephyr/zephyr.elf`,
`zephyr/zephyr.hex`, etc., depending on your board's build system
integration. These binaries may be flashed to a board using
alternative tools of your choice, or used for debugging as needed,
e.g. as a source of symbol tables.

By default, these West commands rebuild binaries before flashing and
debugging. This can of course also be accomplished using the usual
targets provided by Zephyr's build system (in fact, that's how these
commands do it).

.. _cmake(1):
   https://cmake.org/cmake/help/latest/manual/cmake.1.html
