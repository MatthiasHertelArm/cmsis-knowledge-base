---
id: "zep-building-flashing-and-debugging-configuration-options"
type: "concept"
domain: "project"
title: "Building, Flashing and Debugging: Building: `west build` / Configuration Options"
summary: "You can configure west build using these options."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/build-flash-debug.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/build-flash-debug.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Building: `west build`_

You can configure `west build` using these options.

.. NOTE: docs authors: keep this table sorted alphabetically


* - Option
  - Description
* - `build.board`
  - String. If given, this the board used by :ref:`west build
    <west-building>` when `--board` is not given and `BOARD`
    is unset in the environment.
* - `build.board_warn`
  - Boolean, default `true`. If `false`, disables warnings when
    `west build` can't figure out the target board.
* - `build.cmake-args`
  - String. If present, the value will be split according to shell rules and
    passed to CMake whenever a new build system is generated. See
* - `build.dir-fmt`
  - String, default `build`. The build folder format string, used by
    west whenever it needs to create or locate a build folder. The currently
    available arguments are:

      - `west_topdir`: The absolute path to the west workspace, as
        returned by the `west_topdir` command
      - `board`: The board name
      - `source_dir`: Path to the CMake source directory, relative to the
        current working directory. If the current working directory is
        inside the source directory, this is an empty string, as it is on
        Windows for a source directory on another drive, which has no
        relative path to the current one. If no source directory is
        specified, it defaults to current working directory.
        E.g. if `west build ../app` is run from `<west_topdir>/app1`,
        `source_dir` resolves to `../app` (which is the relative path
        to the current working dir).
      - `source_dir_workspace`: Path to the source directory, relative to
        `west_topdir` (if it is inside the workspace). Otherwise, it is
        relative to the filesystem root (`/` on Unix, respectively
        `C:/` on Windows).
        E.g. if `west build ../app` is run from `<west_topdir>/app1`,
        `source_dir` resolves to `app` (which is the relative path to
        the west workspace dir).
      - `app`: The name of the source directory.
* - `build.generator`
  - String, default `Ninja`. The CMake Generator to use to create a
    build system. (To set a generator for a single build, see the
* - `build.guess-dir`
  - String, instructs west whether to try to guess what build folder to use
    when `build.dir-fmt` is in use and not enough information is available
    to resolve the build folder name. Can take these values:

      - `never` (default): Never try to guess, bail out instead and
        require the user to provide a build folder with `-d`.
      - `runners`: Try to guess the folder when using any of the 'runner'
        commands.  These are typically all commands that invoke an external
        tool, such as `flash` and `debug`.
* - `build.pristine`
  - String. Controls the way in which `west build` may clean the build
    folder before building. Can take the following values:

      - `never` (default): Never automatically make the build folder
        pristine.
      - `auto`:  `west build` will automatically make the build folder
        pristine before building, if a build system is present and the build
        would fail otherwise (e.g. the user has specified a different board
        or application from the one previously used to make the build
        directory).
      - `always`: Always make the build folder pristine before building, if
        a build system is present.
* - `build.sysbuild`
  - Boolean, default `false`. If `true`, build application using the
    sysbuild infrastructure.
