---
id: "zep-setting-kconfig-configuration-valu-tracking-kconfig-symbols"
type: "concept"
domain: "project"
title: "Setting Kconfig configuration values: Tracking Kconfig symbols"
summary: "It is possible to create Kconfig symbols which takes the default value of another Kconfig symbol."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/kconfig/setting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/kconfig/setting.rst"
license: "Apache-2.0"
mode: "V"
---

It is possible to create Kconfig symbols which takes the default value of
another Kconfig symbol.

This is valuable when you want a symbol specific to an application or subsystem
but do not want to rely directly on the common symbol. For example, you might
want to decouple the settings so they can be independently configured, or to
ensure you always have a locally named setting, even if the external setting name changes.
is later changed.

For example, consider the common `FOO_STRING` setting where a subsystem wants
to have a `SUB_FOO_STRING` but still allow for customization.

This can be done like this:

```kconfig

config FOO_STRING
        string "Foo"
        default "foo"

config SUB_FOO_STRING
        string "Sub-foo"
        default FOO_STRING
```
This ensures that the default value of `SUB_FOO_STRING` is identical to
`FOO_STRING` while still allows users to configure both settings
independently.

It is also possible to make `SUB_FOO_STRING` invisible and thereby keep the
two symbols in sync, unless the value of the tracking symbol is changed in a
`defconfig` file.

```kconfig

config FOO_STRING
        string "Foo"
        default "foo"

config SUB_FOO_STRING
        string
        default FOO_STRING
        help
          Hidden symbol which follows FOO_STRING
          Can be changed through *.defconfig files.
```
