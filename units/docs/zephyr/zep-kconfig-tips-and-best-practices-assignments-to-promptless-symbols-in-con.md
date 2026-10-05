---
id: "zep-kconfig-tips-and-best-practices-assignments-to-promptless-symbols-in-con"
type: "concept"
domain: "project"
title: "Kconfig - Tips and Best Practices: Assignments to promptless symbols in configuration files"
summary: "Assignments to hidden (promptless, also called invisible) symbols in configuration files are always ignored. Hidden symbols get their value indirectly from other symbols, via e.g. default and select."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/kconfig/tips.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/kconfig/tips.rst"
license: "Apache-2.0"
mode: "V"
---

Assignments to hidden (promptless, also called *invisible*) symbols in
configuration files are always ignored. Hidden symbols get their value
indirectly from other symbols, via e.g. `default` and `select`.

A common source of confusion is opening the output configuration file
(`zephyr/.config`), seeing a bunch of assignments to hidden symbols,
and assuming that those assignments must be respected when the configuration is
read back in by Kconfig. In reality, all assignments to hidden symbols in
`zephyr/.config` are ignored by Kconfig, like for other configuration
files.

To understand why `zephyr/.config` still includes assignments to hidden
symbols, it helps to realize that `zephyr/.config` serves two separate
purposes:

1. It holds the saved configuration, and

2. it holds configuration output. `zephyr/.config` is parsed by the CMake
   files to let them query configuration settings, for example.

The assignments to hidden symbols in `zephyr/.config` are just
configuration output. Kconfig itself ignores assignments to hidden symbols when
calculating symbol values.


**Note:** A *minimal configuration*, which can be generated from within the closer to just a saved configuration, without the full configuration output.
