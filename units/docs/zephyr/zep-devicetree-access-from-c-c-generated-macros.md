---
id: "zep-devicetree-access-from-c-c-generated-macros"
type: "concept"
domain: "project"
title: "Devicetree access from C/C++: Generated macros"
summary: "While the zephyr/devicetree.h API is not generated, it does rely on a generated C header which is put into every application build directory: devicetree_generated.h. This file contains macros with devicetree data."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/api-usage.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/api-usage.rst"
license: "Apache-2.0"
mode: "V"
---

While the `zephyr/devicetree.h` API is not generated, it does rely on a
generated C header which is put into every application build directory:
devicetree_generated.h. This file contains macros with
devicetree data.

These macros have tricky naming conventions which the devicetree_api API
abstracts away. They should be considered an implementation detail, but it's
useful to understand them since they will frequently be seen in compiler error
messages.

This section contains an Augmented Backus-Naur Form grammar for these
generated macros, with examples and more details in comments. See `7405`
(which extends `5234`) for a syntax specification.
