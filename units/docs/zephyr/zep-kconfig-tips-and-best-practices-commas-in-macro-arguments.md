---
id: "zep-kconfig-tips-and-best-practices-commas-in-macro-arguments"
type: "concept"
domain: "project"
title: "Kconfig - Tips and Best Practices: Commas in macro arguments"
summary: "Kconfig uses commas to separate macro arguments. This means a construct like this will fail:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/kconfig/tips.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/kconfig/tips.rst"
license: "Apache-2.0"
mode: "V"
---

Kconfig uses commas to separate macro arguments.
This means a construct like this will fail:

```kconfig

config FOO
    bool
    default y if $(dt_chosen_enabled,"zephyr,bar")
```
To solve this problem, create a variable with the text and use this variable as
argument, as follows:

```kconfig

DT_CHOSEN_ZEPHYR_BAR := zephyr,bar

config FOO
    bool
    default y if $(dt_chosen_enabled,$(DT_CHOSEN_ZEPHYR_BAR))
```

**Note:** A variable `DT_COMPAT_{VND_MY_DEVICE} := {vnd,my-device}` is automatically created by Zephyr for every `compatible` found in Devicetree bindings; there is no need to define such variables. See auto-dts-kconfig for details.
