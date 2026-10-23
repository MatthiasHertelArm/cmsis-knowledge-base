---
id: "zep-kconfig-tips-and-best-practices-depends-on-and-string-int-hex-symbols"
type: "concept"
domain: "project"
title: "Kconfig - Tips and Best Practices: `depends on` and `string`/`int`/`hex` symbols"
summary: "depends on works not just for bool symbols, but also for string, int, and hex symbols (and for choices)."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/kconfig/tips.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/kconfig/tips.rst"
license: "Apache-2.0"
mode: "V"
---

`depends on` works not just for `bool` symbols, but also for `string`,
`int`, and `hex` symbols (and for choices).

The Kconfig definitions below will hide the `FOO_DEVICE_FREQUENCY` symbol and
disable any configuration output for it when `FOO_DEVICE` is disabled.

```kconfig

config FOO_DEVICE
    bool "Foo device"

config FOO_DEVICE_FREQUENCY
    int "Foo device frequency"
    depends on FOO_DEVICE
```
In general, it's a good idea to check that only relevant symbols are ever shown
in the `menuconfig`/`guiconfig` interface. Having `FOO_DEVICE_FREQUENCY`
show up when `FOO_DEVICE` is disabled (and possibly hidden) makes the
relationship between the symbols harder to understand, even if code never looks
at `FOO_DEVICE_FREQUENCY` when `FOO_DEVICE` is disabled.
