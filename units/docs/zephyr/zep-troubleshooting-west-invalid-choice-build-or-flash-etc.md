---
id: "zep-troubleshooting-west-invalid-choice-build-or-flash-etc"
type: "concept"
domain: "project"
title: "Troubleshooting West: \"invalid choice: 'build'\" (or 'flash', etc.)"
summary: "If you see an unexpected error like this when trying to run a Zephyr extension command (like west flash, :ref:west build <west-building>, etc.):"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/troubleshooting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/troubleshooting.rst"
license: "Apache-2.0"
mode: "V"
---

If you see an unexpected error like this when trying to run a Zephyr extension
command (like west flash, :ref:`west build
<west-building>`, etc.):

```none

$ west build [...]
west: error: argument <command>: invalid choice: 'build' (choose from 'init', [...])

$ west flash [...]
west: error: argument <command>: invalid choice: 'flash' (choose from 'init', [...])
```
The most likely cause is that you're running the command outside of a
west workspace. West needs to know where your workspace
is to find west-extensions.

To fix this, you have two choices:

#. Run the command from inside a workspace (e.g. the `zephyrproject`
   directory you created when you got started).

   For example, create your build directory inside the workspace, or run ``west
   flash --build-dir YOUR_BUILD_DIR`` from inside the workspace.

#. Set the `ZEPHYR_BASE` environment variable and re-run
   the west extension command. If set, west will use `ZEPHYR_BASE` to
   find your workspace.

If you're unsure whether a command is built-in or an extension, run ``west
help`` from inside your workspace. The output prints extension commands
separately, and looks like this for mainline Zephyr:

```none

$ west help

built-in commands for managing git repositories:
  init:                 create a west workspace
  [...]

other built-in commands:
  help:                 get help for west or a command
  [...]

extension commands from project manifest (path: zephyr):
  build:                compile a Zephyr application
  flash:                flash and run a binary on a board
  [...]
```
