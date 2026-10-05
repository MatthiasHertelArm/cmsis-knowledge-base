---
id: "zep-devicetree-access-from-c-c-a-note-for-linux-developers"
type: "concept"
domain: "project"
title: "Devicetree access from C/C++: A note for Linux developers"
summary: "Linux developers familiar with devicetree should be warned that the API described here differs significantly from how devicetree is used on Linux."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/api-usage.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/api-usage.rst"
license: "Apache-2.0"
mode: "V"
---

Linux developers familiar with devicetree should be warned that the API
described here differs significantly from how devicetree is used on Linux.

Instead of generating a C header with all the devicetree data which is then
abstracted behind a macro API, the Linux kernel would instead read the
devicetree data structure in its binary form. The binary representation is
parsed at runtime, for example to load and initialize device drivers.

Zephyr does not work this way because the size of the devicetree binary and
associated handling code would be too large to fit comfortably on the
relatively constrained devices Zephyr supports.
