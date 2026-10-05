---
id: "zep-input-and-output-files-scripts-and-tools"
type: "concept"
domain: "project"
title: "Input and output files: Scripts and tools"
summary: "The following libraries and scripts, located in scripts/dts/, create output files from input files. Their sources have extensive documentation."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/intro-input-output.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/intro-input-output.rst"
license: "Apache-2.0"
mode: "V"
---

The following libraries and scripts, located in `scripts/dts/`,
create output files from input files. Their sources have extensive
documentation.

`dtlib.py <scripts/dts/python-devicetree/src/devicetree/dtlib.py>`
    A low-level DTS parsing library.

`edtlib.py <scripts/dts/python-devicetree/src/devicetree/edtlib.py>`
    A library layered on top of dtlib that uses bindings to interpret
    properties and give a higher-level view of the devicetree. Uses dtlib to do
    the DTS parsing.

`gen_defines.py <scripts/dts/python-devicetree/src/devicetree/edtlib.py>`
    A script that uses edtlib to generate C preprocessor macros from the
    devicetree and bindings.

In addition to these, the standard `dtc` (devicetree compiler) tool is run on
the final devicetree if it is installed on your system. This is just to catch
errors or warnings. The output is unused. Boards may need to pass `dtc`
additional flags, e.g. for warning suppression. Board directories can contain a
file named `pre_dt_board.cmake` which configures these extra flags, like
this:

```cmake

list(APPEND EXTRA_DTC_FLAGS "-Wno-simple_bus_reg")
```
Shield directories can contain a file named `pre_dt_shield.cmake` which
has the same functionality as the aforementioned `pre_dt_board.cmake`.
