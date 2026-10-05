---
id: "zep-scope-and-purpose"
type: "concept"
domain: "project"
title: "Scope and purpose"
summary: "A devicetree is primarily a hierarchical data structure that describes hardware. The Devicetree specification defines its source and binary representations."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/intro-scope-purpose.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/intro-scope-purpose.rst"
license: "Apache-2.0"
mode: "V"
---

A *devicetree* is primarily a hierarchical data structure that describes
hardware. The Devicetree specification defines its source and binary
representations.

Zephyr uses devicetree to describe:

- the hardware available on its boards
- that hardware's initial configuration

As such, devicetree is both a hardware description language and a configuration
language for Zephyr. See dt_vs_kconfig for some comparisons between
devicetree and Zephyr's other main configuration language, Kconfig.

There are two types of devicetree input files: *devicetree sources* and
*devicetree bindings*. The sources contain the devicetree itself. The bindings
describe its contents, including data types. The :ref:`build system
<build_overview>` uses devicetree sources and bindings to produce a generated C
header. The generated header's contents are abstracted by the `devicetree.h`
API, which you can use to get information from your devicetree.

Here is a simplified view of the process:

All Zephyr and application source code files can include and use
`devicetree.h`. This includes device drivers,
applications, tests, the kernel, etc.

The API itself is based on C macros. The macro names all start with `DT_`. In
general, if you see a macro that starts with `DT_` in a Zephyr source file,
it's probably a `devicetree.h` macro. The generated C header contains macros
that start with `DT_` as well; you might see those in compiler error
messages. You always can tell a generated- from a non-generated macro:
generated macros have some lowercased letters, while the `devicetree.h` macro
names have all capital letters.
