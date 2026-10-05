---
id: "zep-building-flashing-and-debugging-debugging-west-debug-west-debugserver"
type: "concept"
domain: "project"
title: "Building, Flashing and Debugging: Debugging: `west debug`, `west debugserver`"
summary: "From a Zephyr build directory, to attach a debugger to your board and open up a debug console (e.g. a GDB session)::"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/build-flash-debug.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/build-flash-debug.rst"
license: "Apache-2.0"
mode: "V"
---

**Tip:** Run `west debug -h` or `west debugserver -h` for additional help.


### Basics


From a Zephyr build directory, to attach a debugger to your board and
open up a debug console (e.g. a GDB session)::
```
west debug
```
To attach a debugger to your board and open up a local network port
you can connect a debugger to (e.g. an IDE debugger)::
```
west debugserver
```
To specify the build directory, use `--build-dir` (or `-d`)::
```
west debug --build-dir path/to/build/directory
west debugserver --build-dir path/to/build/directory
```
If you don't specify the build directory, these commands search for one in
`build`, then the current working directory. If you set the
`build.dir-fmt` configuration option (see west-building-dirs), ``west
debug`` searches there instead of `build`.


### Choosing a Runner


If your board's Zephyr integration supports debugging with multiple
programs, you can specify which one to use using the `--runner` (or
`-r`) option. For example, if West debugs your board with
`pyocd-gdbserver` by default, but it also supports JLink, you can
override the default with::
```
west debug --runner jlink
west debugserver --runner jlink
```
See west-runner below for more information on the `runner`
library used by West. The list of runners which support debugging can
be obtained with `west debug -H`; if run from a build directory or
with `--build-dir`, this will print additional information on
available runners for your board.


### Configuration Overrides


The CMake cache contains default values West uses for debugging, such
as where the board directory is on the file system, the path to the
zephyr binaries containing symbol tables, and more. You can override
any of this configuration at runtime with additional options.

For example, to override the ELF file containing the Zephyr binary and
symbol tables (assuming your runner expects an ELF file), but keep
other debug configuration at default values::
```
west debug --elf-file path/to/some/other.elf
west debugserver --elf-file path/to/some/other.elf
```
The `west debug -h` output includes a complete list of overrides
supported by all runners.


### Runner-Specific Overrides


Each runner may support additional options related to debugging. For
example, some runners support flags which allow you to set the network
ports used by debug servers.

To view all of the available options for the runners your board
supports, as well as their usage information, use `--context` (or
`-H`)::
```
west debug --context
```
(The command `west debugserver --context` will print the same output.)


**Important:** Note the capital H in the short option name. This re-runs the build in order to ensure the information displayed is up to date!

When running West outside of a build directory, `west debug -H` just
prints a list of runners. You can use ``west debug -H -r
<runner-name>`` to print usage information for options supported by
that runner.

For example, to print usage information about the `jlink` runner::
```
west debug -H -r jlink
```

### Multi-domain debugging


`west debug` can only debug a single domain at a time. When a
west-multi-domain-builds folder is detected, `west debug`
will debug the `default` domain specified by sysbuild.

The default domain will be the application given as the source directory.
See the following example::
```
west build --sysbuild path/to/source/directory
```
For example, when building `hello_world` with MCUboot using sysbuild,
`hello_world` becomes the default domain::
```
west build --sysbuild samples/hello_world
```
So to debug `hello_world` you can do::
```
west debug
```
or::
```
west debug --domain hello_world
```
If you wish to debug MCUboot, you must explicitly specify MCUboot as the domain
to debug::
```
west debug --domain mcuboot
```

### Configuration Options


You can configure `west debug` and
configure `west debugserver` using these options.

.. NOTE: docs authors: keep this table sorted alphabetically


* - Option
  - Description
* - `debug.rebuild`
  - Boolean, default `true`. If `false`, do not rebuild on west debug.
* - `debugserver.rebuild`
  - Boolean, default `true`. If `false`, do not rebuild on west debugserver.
