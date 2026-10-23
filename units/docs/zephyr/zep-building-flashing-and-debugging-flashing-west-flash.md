---
id: "zep-building-flashing-and-debugging-flashing-west-flash"
type: "concept"
domain: "project"
title: "Building, Flashing and Debugging: Flashing: `west flash`"
summary: "From a Zephyr build directory, re-build the binary and flash it to your board::"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/build-flash-debug.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/build-flash-debug.rst"
license: "Apache-2.0"
mode: "V"
---

**Tip:** Run `west flash -h` for additional help.


### Basics


From a Zephyr build directory, re-build the binary and flash it to
your board::
```
west flash
```
To specify the build directory, use `--build-dir` (or `-d`)::
```
west flash --build-dir path/to/build/directory
```
If you don't specify the build directory, `west flash` searches for one in
`build`, then the current working directory. If you set the
`build.dir-fmt` configuration option (see west-building-dirs), ``west
flash`` searches there instead of `build`.


### Choosing a Runner


If your board's Zephyr integration supports flashing with multiple
programs, you can specify which one to use using the `--runner` (or
`-r`) option. For example, if West flashes your board with
`nrfjprog` by default, but it also supports JLink, you can override
the default with::
```
west flash --runner jlink
```
You can override the default flash runner at build time by using the
`BOARD_FLASH_RUNNER` CMake variable, and the debug runner with
`BOARD_DEBUG_RUNNER`.

For example::
```
# Set the default runner to "jlink", overriding the board's
# usual default.
west build [...] -- -DBOARD_FLASH_RUNNER=jlink
```
See west-building-cmake-args and west-building-cmake-config for
more information on setting CMake arguments.

See west-runner below for more information on the `runner`
library used by West. The list of runners which support flashing can
be obtained with `west flash -H`; if run from a build directory or
with `--build-dir`, this will print additional information on
available runners for your board.


### Configuration Overrides


The CMake cache contains default values West uses while flashing, such
as where the board directory is on the file system, the path to the
zephyr binaries to flash in several formats, and more. You can
override any of this configuration at runtime with additional options.

For example, to override the HEX file containing the Zephyr image to
flash (assuming your runner expects a HEX file), but keep other
flash configuration at default values::
```
west flash --hex-file path/to/some/other.hex
```
The `west flash -h` output includes a complete list of overrides
supported by all runners.


### Runner-Specific Overrides


Each runner may support additional options related to flashing. For
example, some runners support an `--erase` flag, which mass-erases
the flash storage on your board before flashing the Zephyr image.

To view all of the available options for the runners your board
supports, as well as their usage information, use `--context` (or
`-H`)::
```
west flash --context
```

**Important:** Note the capital H in the short option name. This re-runs the build in order to ensure the information displayed is up to date!

When running West outside of a build directory, `west flash -H` just
prints a list of runners. You can use ``west flash -H -r
<runner-name>`` to print usage information for options supported by
that runner.

For example, to print usage information about the `jlink` runner::
```
west flash -H -r jlink
```

### Multi-domain flashing


When a west-multi-domain-builds folder is detected, then `west flash`
will flash all domains in the order defined by sysbuild.

It is possible to flash the image from a single domain in a multi-domain project
by using `--domain`.

For example, in a multi-domain build with hello_world and
MCUboot, you can use the `--domain hello_world` domain to only flash
only the image from this domain::
```
west flash --domain hello_world
```

### Configuration Options


You can configure `west flash` using these options.

.. NOTE: docs authors: keep this table sorted alphabetically


* - Option
  - Description
* - `flash.rebuild`
  - Boolean, default `true`. If `false`, do not rebuild on west flash.
