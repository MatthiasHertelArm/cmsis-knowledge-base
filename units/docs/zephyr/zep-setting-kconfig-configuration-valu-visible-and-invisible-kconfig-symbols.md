---
id: "zep-setting-kconfig-configuration-valu-visible-and-invisible-kconfig-symbols"
type: "concept"
domain: "project"
title: "Setting Kconfig configuration values: Visible and invisible Kconfig symbols"
summary: "When making Kconfig changes, it's important to understand the difference between visible and invisible symbols."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/kconfig/setting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/kconfig/setting.rst"
license: "Apache-2.0"
mode: "V"
---

When making Kconfig changes, it's important to understand the difference
between *visible* and *invisible* symbols.

- A visible symbol is a symbol defined with a prompt. Visible symbols show
  up in the interactive configuration interfaces (hence *visible*), and can be
  set in configuration files.

  Here's an example of a visible symbol:

```kconfig

config FPU
    bool "Support floating point operations"
    depends on HAS_FPU
```
  The symbol is shown like this in `menuconfig`, where it can be toggled:

```none

[ ] Support floating point operations
```
- An *invisible* symbol is a symbol without a prompt. Invisible symbols are
  not shown in the interactive configuration interfaces, and users have no
  direct control over their value. They instead get their value from defaults
  or from other symbols.

  Here's an example of an invisible symbol:

```kconfig

config CPU_HAS_FPU
    bool
    help
      This symbol is y if the CPU has a hardware floating point unit.
```
  In this case, `CPU_HAS_FPU` is enabled through other symbols having
  `select CPU_HAS_FPU`.
