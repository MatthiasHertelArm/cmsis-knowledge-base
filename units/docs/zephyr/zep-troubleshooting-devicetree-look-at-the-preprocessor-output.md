---
id: "zep-troubleshooting-devicetree-look-at-the-preprocessor-output"
type: "concept"
domain: "project"
title: "Troubleshooting devicetree: Look at the preprocessor output"
summary: "To save preprocessor output files, enable the CONFIG_COMPILER_SAVE_TEMPS option. For example, to build hello_world with west with this option set, use:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/troubleshooting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/troubleshooting.rst"
license: "Apache-2.0"
mode: "V"
---

To save preprocessor output files, enable the
`CONFIG_COMPILER_SAVE_TEMPS` option. For example, to build
hello_world with west with this option set, use:

```sh

west build -b BOARD samples/hello_world -- -DCONFIG_COMPILER_SAVE_TEMPS=y
```
This will create a preprocessor output file named `foo.c.i` in the build
directory for each source file `foo.c`.

You can then search for the file in the build directory to see what your
devicetree macros expanded to. For example, on macOS and Linux, using `find`
to find `main.c.i`:

```sh

$ find build -name main.c.i
build/CMakeFiles/app.dir/src/main.c.i
```
It's usually easiest to run a style formatter on the results before opening
them. For example, to use `clang-format` to reformat the file in place:

```sh

clang-format -i build/CMakeFiles/app.dir/src/main.c.i
```
You can then open the file in your favorite editor to view the final C results
after preprocessing.
