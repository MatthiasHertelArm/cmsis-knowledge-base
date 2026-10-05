---
id: "zep-input-and-output-files-output-files"
type: "concept"
domain: "project"
title: "Input and output files: Output files"
summary: "These are created in your application's build directory."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/intro-input-output.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/intro-input-output.rst"
license: "Apache-2.0"
mode: "V"
---

These are created in your application's build directory.


**Warning:** Don't include the header files directly. dt-from-c explains what to do instead.

`<build>/zephyr/zephyr.dts.pre`
   The preprocessed DTS source. This is an intermediate output file, which is
   input to `gen_defines.py` and used to create `zephyr.dts` and
   `devicetree_generated.h`.

`<build>/zephyr/include/generated/zephyr/devicetree_generated.h`
   The generated macros and additional comments describing the devicetree.
   Included by `devicetree.h`.

`<build>/zephyr/zephyr.dts`
   The final merged devicetree. This file is output by `gen_defines.py`.
   It is useful for debugging any issues. If the devicetree compiler `dtc` is
   installed, it is also run on this file, to catch any additional warnings or
   errors.
