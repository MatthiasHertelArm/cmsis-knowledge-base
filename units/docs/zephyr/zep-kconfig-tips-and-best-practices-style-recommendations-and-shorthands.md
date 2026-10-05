---
id: "zep-kconfig-tips-and-best-practices-style-recommendations-and-shorthands"
type: "concept"
domain: "project"
title: "Kconfig - Tips and Best Practices: Style recommendations and shorthands"
summary: "This section gives some style recommendations and explains some common Kconfig shorthands."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/kconfig/tips.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/kconfig/tips.rst"
license: "Apache-2.0"
mode: "V"
---

This section gives some style recommendations and explains some common Kconfig
shorthands.



### Factoring out common dependencies


If a sequence of symbols/choices share a common dependency, the dependency can
be factored out with an `if`.

As an example, consider the following code:

```kconfig

config FOO
    bool "Foo"
    depends on DEP

config BAR
    bool "Bar"
    depends on DEP

choice
    prompt "Choice"
    depends on DEP

config BAZ
    bool "Baz"

config QAZ
    bool "Qaz"

endchoice
```
Here, the `DEP` dependency can be factored out like this:

```kconfig

if DEP

config FOO
    bool "Foo"

config BAR
    bool "Bar"

choice
    prompt "Choice"

config BAZ
    bool "Baz"

config QAZ
    bool "Qaz"

endchoice

endif # DEP
```

**Note:** Internally, the second version of the code is transformed into the first.

If a sequence of symbols/choices with shared dependencies are all in the same
menu, the dependency can be put on the menu itself:

```kconfig

menu "Foo features"
    depends on FOO_SUPPORT

config FOO_FEATURE_1
    bool "Foo feature 1"

config FOO_FEATURE_2
    bool "Foo feature 2"

endmenu
```
If `FOO_SUPPORT` is `n`, the entire menu disappears.



### Redundant defaults


`bool` symbols implicitly default to `n`, and `string` symbols implicitly
default to the empty string. Therefore, `default n` and `default ""` are
(almost) always redundant.

The recommended style in Zephyr is to skip redundant defaults for `bool` and
`string` symbols. That also generates clearer documentation: (*Implicitly
defaults to n* instead of *n if <dependencies, possibly inherited>*).

Defaults *should* always be given for `int` and `hex` symbols, however, as
they implicitly default to the empty string. This is partly for compatibility
with the C Kconfig tools, though an implicit 0 default might be less likely to
be what was intended compared to other symbol types as well.

The one case where `default n`/`default ""` is not redundant is when
defining a symbol in multiple locations and wanting to override e.g. a
`default y` on a later definition. Note that a `default n` does not override
a previously defined `default y`.

That is, FOO will be set to `n` in the example below. If the `default n` was
omitted in the first definition, FOO would have been set to `y`.

```kconfig

config FOO
    bool "foo"
    default n

config FOO
    bool "foo"
    default y
```
In the following example FOO will get the value `y`.

```kconfig

config FOO
    bool "foo"
    default y

config FOO
    bool "foo"
    default n
```

### Common Kconfig shorthands


Kconfig has two shorthands that deal with prompts and defaults.

- `<type> "prompt"` is a shorthand for giving a symbol/choice a type and a
  prompt at the same time. These two definitions are equal:

```kconfig

config FOO
    bool "foo"
```
```kconfig

config FOO
    bool
    prompt "foo"
```
  The first style, with the shorthand, is preferred in Zephyr.

- `def_<type> <value>` is a shorthand for giving a type and a value at the
  same time. These two definitions are equal:

```kconfig

config FOO
    def_bool BAR && BAZ
```
```kconfig

config FOO
    bool
    default BAR && BAZ
```
Using both the `<type> "prompt"` and the `def_<type> <value>` shorthand in
the same definition is redundant, since it gives the type twice.

The `def_<type> <value>` shorthand is generally only useful for symbols
without prompts, and somewhat obscure.


**Note:** For a symbol defined in multiple locations (e.g., in a `Kconfig.defconfig` file in Zephyr), it is best to only give the symbol type for the "base" definition of the symbol, and to use `default` (instead of `def_<type> value`) for the remaining definitions. That way, if the base definition of the symbol is removed, the symbol ends up without a type, which generates a warning that points to the other definitions. That makes the extra definitions easier to discover and remove.


### Prompt strings


For a Kconfig symbol that enables a driver/subsystem FOO, consider having just
"Foo" as the prompt, instead of "Enable Foo support" or the like. It will
usually be clear in the context of an option that can be toggled on/off, and
makes things consistent.


### Style


See coding_style for style guidelines.
