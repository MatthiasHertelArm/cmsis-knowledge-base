---
id: "zep-kconfig-tips-and-best-practices-menuconfig-symbols"
type: "concept"
domain: "project"
title: "Kconfig - Tips and Best Practices: `menuconfig` symbols"
summary: "If the definition of a symbol FOO is immediately followed by other symbols that depend on FOO, then those symbols become children of FOO. If FOO is defined with config FOO, then the children are shown indented relative to FOO."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/kconfig/tips.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/kconfig/tips.rst"
license: "Apache-2.0"
mode: "V"
---

If the definition of a symbol `FOO` is immediately followed by other symbols
that depend on `FOO`, then those symbols become children of `FOO`. If
`FOO` is defined with `config FOO`, then the children are shown indented
relative to `FOO`. Defining `FOO` with `menuconfig FOO` instead puts the
children in a separate menu rooted at `FOO`.

`menuconfig` has no effect on evaluation. It's just a display option.

`menuconfig` can cut down on the number of menus and make the menu structure
easier to navigate. For example, say you have the following definitions:

```kconfig

menu "Foo subsystem"

config FOO_SUBSYSTEM
    bool "Foo subsystem"

if FOO_SUBSYSTEM

config FOO_FEATURE_1
    bool "Foo feature 1"

config FOO_FEATURE_2
    bool "Foo feature 2"

config FOO_FREQUENCY
    int "Foo frequency"

... lots of other FOO-related symbols

endif # FOO_SUBSYSTEM

endmenu
```
In this case, it's probably better to get rid of the `menu` and turn
`FOO_SUBSYSTEM` into a `menuconfig` symbol:

```kconfig

menuconfig FOO_SUBSYSTEM
    bool "Foo subsystem"

if FOO_SUBSYSTEM

config FOO_FEATURE_1
    bool "Foo feature 1"

config FOO_FEATURE_2
    bool "Foo feature 2"

config FOO_FREQUENCY
    int "Foo frequency"

... lots of other FOO-related symbols

endif # FOO_SUBSYSTEM
```
In the `menuconfig` interface, this will be displayed as follows:

```none

[*] Foo subsystem  --->
```
Note that making a symbol without children a `menuconfig` is meaningless. It
should be avoided, because it looks identical to a symbol with all children
invisible:

```none

[*] I have no children  ----
[*] All my children are invisible  ----
```
