---
id: "zep-kconfig-tips-and-best-practices-lesser-known-used-kconfig-features"
type: "concept"
domain: "project"
title: "Kconfig - Tips and Best Practices: Lesser-known/used Kconfig features"
summary: "This section lists some more obscure Kconfig behaviors and features that might still come in handy."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/kconfig/tips.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/kconfig/tips.rst"
license: "Apache-2.0"
mode: "V"
---

This section lists some more obscure Kconfig behaviors and features that might
still come in handy.



### The `imply` statement


The `imply` statement is similar to `select`, but respects dependencies and
doesn't force a value. For example, the following code could be used to enable
USB keyboard support by default on the FOO SoC, while still allowing the user
to turn it off:

```kconfig

config SOC_FOO
    bool
    imply USB_KEYBOARD

...

config USB_KEYBOARD
    bool "USB keyboard support"
```
`imply` acts like a suggestion, whereas `select` forces a value.



### Optional prompts


A condition can be put on a symbol's prompt to make it optionally configurable
by the user. For example, a value `MASK` that's hardcoded to 0xFF on some
boards and configurable on others could be expressed as follows:

```kconfig

config MASK
    hex "Bitmask" if HAS_CONFIGURABLE_MASK
    default 0xFF
```

**Note:** This is short for the following: .. code-block:: kconfig config MASK hex prompt "Bitmask" if HAS_CONFIGURABLE_MASK default 0xFF

The `HAS_CONFIGURABLE_MASK` helper symbol would get selected by boards to
indicate that `MASK` is configurable. When `MASK` is configurable, it will
also default to 0xFF.



### Optional choices


Defining a choice with the `optional` keyword allows the whole choice to be
toggled off to select none of the symbols:

```kconfig

choice
    prompt "Use legacy protocol"
    optional

config LEGACY_PROTOCOL_1
    bool "Legacy protocol 1"

config LEGACY_PROTOCOL_2
    bool "Legacy protocol 2"

endchoice
```
In the `menuconfig` interface, this will be displayed e.g. as
`[*] Use legacy protocol (Legacy protocol 1) --->`, where the choice can be
toggled off to enable neither of the symbols.



### `visible if` conditions


Putting a `visible if` condition on a menu hides the menu and all the symbols
within it, while still allowing symbol default values to kick in.

As a motivating example, consider the following code:

```kconfig

menu "Foo subsystem"
    depends on HAS_CONFIGURABLE_FOO

config FOO_SETTING_1
    int "Foo setting 1"
    default 1

config FOO_SETTING_2
    int "Foo setting 2"
    default 2

endmenu
```
When `HAS_CONFIGURABLE_FOO` is `n`, no configuration output is generated
for `FOO_SETTING_1` and `FOO_SETTING_2`, as the code above is logically
equivalent to the following code:

```kconfig

config FOO_SETTING_1
    int "Foo setting 1"
    default 1
    depends on HAS_CONFIGURABLE_FOO

config FOO_SETTING_2
    int "Foo setting 2"
    default 2
    depends on HAS_CONFIGURABLE_FOO
```
If we want the symbols to still get their default values even when
`HAS_CONFIGURABLE_FOO` is `n`, but not be configurable by the user, then we
can use `visible if` instead:

```kconfig

menu "Foo subsystem"
    visible if HAS_CONFIGURABLE_FOO

config FOO_SETTING_1
    int "Foo setting 1"
    default 1

config FOO_SETTING_2
    int "Foo setting 2"
    default 2

endmenu
```
This is logically equivalent to the following:

```kconfig

config FOO_SETTING_1
    int "Foo setting 1" if HAS_CONFIGURABLE_FOO
    default 1

config FOO_SETTING_2
    int "Foo setting 2" if HAS_CONFIGURABLE_FOO
    default 2
```

**Note:** See the optional prompts section for the meaning of the conditions on the prompts.

When `HAS_CONFIGURABLE_FOO` is `n`, we now get the following configuration
output for the symbols, instead of no output:

```cfg

...
CONFIG_FOO_SETTING_1=1
CONFIG_FOO_SETTING_2=2
...
```
