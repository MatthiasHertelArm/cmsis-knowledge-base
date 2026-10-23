---
id: "zep-building-flashing-and-debugging-building-west-build"
type: "concept"
domain: "project"
title: "Building, Flashing and Debugging: Building: `west build`"
summary: "The build command helps you build Zephyr applications from source. You can use west config to configure its behavior."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/build-flash-debug.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/build-flash-debug.rst"
license: "Apache-2.0"
mode: "V"
---

**Tip:** Run `west build -h` for a quick overview.

The `build` command helps you build Zephyr applications from source. You can
use west config to configure its behavior.

Its default behavior tries to "do what you mean":

- If there is a Zephyr build directory named `build` in your current
  working directory, it is incrementally re-compiled. The same is true if you
  run `west build` from a Zephyr build directory.

- Otherwise, if you run `west build` from a Zephyr application's source
  directory and no build directory is found, a new one is created and the
  application is compiled in it.
