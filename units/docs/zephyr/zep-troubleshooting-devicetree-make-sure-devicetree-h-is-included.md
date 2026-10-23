---
id: "zep-troubleshooting-devicetree-make-sure-devicetree-h-is-included"
type: "concept"
domain: "project"
title: "Troubleshooting devicetree: Make sure <devicetree.h> is included"
summary: "Unlike Kconfig symbols, the devicetree.h header must be included explicitly."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/troubleshooting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/troubleshooting.rst"
license: "Apache-2.0"
mode: "V"
---

Unlike Kconfig symbols, the `devicetree.h` header must be included
explicitly.

Many Zephyr header files rely on information from devicetree, so including some
other API may transitively include `devicetree.h`, but that's not
guaranteed.
