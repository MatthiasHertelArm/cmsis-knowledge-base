---
id: "zep-building-flashing-and-debugging-basics"
type: "concept"
domain: "project"
title: "Building, Flashing and Debugging: Building: `west build` / Basics"
summary: "The easiest way to use west build is to go to an application's root directory (i.e. the folder containing the application's CMakeLists.txt) and then run::"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/build-flash-debug.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/build-flash-debug.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Building: `west build`_

The easiest way to use `west build` is to go to an application's root
directory (i.e. the folder containing the application's `CMakeLists.txt`)
and then run::
```
west build -b <BOARD>
```
Where `<BOARD>` is the name of the board you want to build for. This is
exactly the same name you would supply to CMake if you were to invoke it with:
`cmake -DBOARD=<BOARD>`.


**Tip:** You can use the west boards command to list all supported boards.

A build directory named `build` will be created, and the application will
be compiled there after `west build` runs CMake to create a build system in
that directory. If `west build` finds an existing build directory, the
application is incrementally re-compiled there without re-running CMake. You
can force CMake to run again with `--cmake`.

You don't need to use the `--board` option if you've already got an existing
build directory; `west build` can figure out the board from the CMake cache.
For new builds, the `--board` option, `BOARD` environment variable,
or `build.board` configuration option are checked (in that order).
