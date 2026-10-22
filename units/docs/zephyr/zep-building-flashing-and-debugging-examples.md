---
id: "zep-building-flashing-and-debugging-examples"
type: "concept"
domain: "project"
title: "Building, Flashing and Debugging: Building: `west build` / Examples"
summary: "Here are some west build usage examples, grouped by area."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/build-flash-debug.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/build-flash-debug.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Building: `west build`_

Here are some `west build` usage examples, grouped by area.


#### Forcing CMake to Run Again


To force a CMake re-run, use the `--cmake` (or `-c`) option::
```
west build -c
```

#### Setting a Default Board


To configure `west build` to build for the `reel_board` by default::
```
west config build.board reel_board
```
(You can use any other board supported by Zephyr here; it doesn't have to be
`reel_board`.)


#### Setting Source and Build Directories


To set the application source directory explicitly, give its path as a
positional argument::
```
west build -b <BOARD> path/to/source/directory
```
To set the build directory explicitly, use `--build-dir` (or `-d`)::
```
west build -b <BOARD> --build-dir path/to/build/directory
```
To change the default build directory from `build`, use the
`build.dir-fmt` configuration option. This lets you name build
directories using format strings, like this::
```
west config build.dir-fmt "build/{board}/{app}"
```
With the above, running `west build -b reel_board samples/hello_world` will
use build directory `build/reel_board/hello_world`.  See
west-building-config for more details on this option.


#### Setting the Build System Target


To specify the build system target to run, use `--target` (or `-t`).

For example, on host platforms with QEMU, you can use the `run` target to
build and run the hello_world sample for the emulated
qemu_x86 board in one command::
```
west build -b qemu_x86 -t run samples/hello_world
```
As another example, to use `-t` to list all build system targets::
```
west build -t help
```
As a final example, to use `-t` to run the `pristine` target, which deletes
all the files in the build directory::
```
west build -t pristine
```

#### Pristine Builds


A *pristine* build directory is essentially a new build directory. All
byproducts from previous builds have been removed.

To force `west build` make the build directory pristine before re-running
CMake to generate a build system, use the `--pristine=always` (or
`-p=always`) option.

Giving `--pristine` or `-p` without a value has the same effect as giving
it the value `always`. For example, these commands are equivalent::
```
west build -p -b reel_board samples/hello_world
west build -p=always -b reel_board samples/hello_world
```
By default, `west build` makes no attempt to detect if the build directory
needs to be made pristine. This can lead to errors if you do something like
try to reuse a build directory for a different `--board`.

Using `--pristine=auto` makes `west build` detect some of these situations
and make the build directory pristine before trying the build.


**Tip:** You can run `west config build.pristine always` to always do a pristine build, or `west config build.pristine never` to disable the heuristic. See the `west build` west-building-config for details.


#### Verbose Builds


To print the CMake and compiler commands run by `west build`, use the global
west verbosity option, `-v`::
```
west -v build -b reel_board samples/hello_world
```

#### One-Time CMake Arguments


To pass additional arguments to the CMake invocation performed by ``west
build`, pass them after a `--`` at the end of the command line.


**Important:** Passing additional CMake arguments like this forces `west build` to re-run the CMake build configuration step, even if a build system has already been generated.  This will make incremental builds slower (but still much faster than building from scratch). After using `--` once to generate the build directory, use `west build -d <build-dir>` on subsequent runs to do incremental builds. Alternatively, make your CMake arguments permanent as described in the next section; it will not slow down incremental builds.

For example, to use the Unix Makefiles CMake generator instead of Ninja (which
`west build` uses by default), run::
```
west build -b reel_board -- -G'Unix Makefiles'
```
To use Unix Makefiles and set CMAKE_VERBOSE_MAKEFILE to `ON`::
```
west build -b reel_board -- -G'Unix Makefiles' -DCMAKE_VERBOSE_MAKEFILE=ON
```
Notice how the `--` only appears once, even though multiple CMake arguments
are given. All command-line arguments to `west build` after a `--` are
passed to CMake.

To set DTC_OVERLAY_FILE to
`enable-modem.overlay`, using that file as a
devicetree overlay::
```
west build -b reel_board -- -DDTC_OVERLAY_FILE=enable-modem.overlay
```
To merge the `file.conf` Kconfig fragment into your build's
`.config`::
```
west build -- -DEXTRA_CONF_FILE=file.conf
```

#### Permanent CMake Arguments


The previous section describes how to add CMake arguments for a single ``west
build` command. If you want to save CMake arguments for `west build`` to use
every time it generates a new build system instead, you should use the
`build.cmake-args` configuration option. Whenever `west build` runs CMake
to generate a build system, it splits this option's value according to shell
rules and includes the results in the `cmake` command line.

Remember that, by default, `west build` **tries to avoid generating a new
build system if one is present** in your build directory. Therefore, you need
to either delete any existing build directories or do a :ref:`pristine build
<west-building-pristine>` after setting `build.cmake-args` to make sure it
will take effect.

For example, to always enable `CMAKE_EXPORT_COMPILE_COMMANDS`, you can
run::
```
west config build.cmake-args -- -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
```
(The extra `--` is used to force the rest of the command to be treated as a
positional argument. Without it, west config would
treat the `-DVAR=VAL` syntax as a use of its `-D` option.)

To enable `CMAKE_VERBOSE_MAKEFILE`, so CMake always produces a verbose
build system::
```
west config build.cmake-args -- -DCMAKE_VERBOSE_MAKEFILE=ON
```
To save more than one argument in `build.cmake-args`, use a single string
whose value can be split into distinct arguments (`west build` uses the
Python function shlex.split() internally to split the value).

.. _shlex.split(): https://docs.python.org/3/library/shlex.html#shlex.split

For example, to enable both `CMAKE_EXPORT_COMPILE_COMMANDS` and
`CMAKE_VERBOSE_MAKEFILE`::
```
west config build.cmake-args -- "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_VERBOSE_MAKEFILE=ON"
```
If you want to save your CMake arguments in a separate file instead, you can
combine CMake's `-C <initial-cache>` option with `build.cmake-args`. For
instance, another way to set the options used in the previous example is to
create a file named `~/my-cache.cmake` with the following contents:

```cmake

set(CMAKE_EXPORT_COMPILE_COMMANDS ON CACHE BOOL "")
set(CMAKE_VERBOSE_MAKEFILE ON CACHE BOOL "")
```
Then run::
```
west config build.cmake-args "-C ~/my-cache.cmake"
```
See the cmake(1) manual page and the set() command documentation for
more details.

.. _cmake(1) manual page:
   https://cmake.org/cmake/help/latest/manual/cmake.1.html

.. _set() command:
   https://cmake.org/cmake/help/latest/command/set.html


#### Build tool arguments


Use `-o` to pass options to the underlying build tool.

This works with both `ninja` (the default)
and `make` based build systems.

For example, to pass `-dexplain` to `ninja`::
```
west build -o=-dexplain
```
As another example, to pass `--keep-going` to `make`::
```
west build -o=--keep-going
```
Note that using `-o=--foo` instead of `-o --foo` is required to prevent
`--foo` from being treated as a `west build` option.


#### Build parallelism


By default, `ninja` uses all of your cores to build, while `make` uses only
one. You can control this explicitly with the `-j` option supported by both
tools.

For example, to build with 4 cores::
```
west build -o=-j4
```
The `-o` option is described further in the previous section.


#### Build a single domain


In a multi-domain build with hello_world and MCUboot, you can use
`--domain hello_world` to only build this domain::
```
west build --sysbuild --domain hello_world
```
The `--domain` argument can be combined with the `--target` argument to
build the specific target for the target, for example::
```
west build --sysbuild --domain hello_world --target help
```

#### Use a snippet


See using-snippets.
