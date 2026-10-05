---
id: "zep-setting-kconfig-configuration-valu-configuring-invisible-kconfig-symbols"
type: "concept"
domain: "project"
title: "Setting Kconfig configuration values: Configuring invisible Kconfig symbols"
summary: "When making changes to the default configuration for a board, you might have to configure invisible symbols. This is done in boards/<VENDOR>/<BOARD>/Kconfig.defconfig, which is a regular Kconfig file."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/kconfig/setting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/kconfig/setting.rst"
license: "Apache-2.0"
mode: "V"
---

When making changes to the default configuration for a board, you might have to
configure invisible symbols. This is done in
`boards/<VENDOR>/<BOARD>/Kconfig.defconfig`, which is a regular
`Kconfig` file.


**Note:** Assignments in `.config` files have no effect on invisible symbols, so this scheme is not just an organizational issue.

Assigning values in `Kconfig.defconfig` relies on defining a Kconfig
symbol in multiple locations. As an example, say we want to set `FOO_WIDTH`
below to 32:

```kconfig

config FOO_WIDTH
    int
```
To do this, we extend the definition of `FOO_WIDTH` as follows, in
`Kconfig.defconfig`:

```kconfig

if BOARD_MY_BOARD

config FOO_WIDTH
    default 32

endif
```

**Note:** Since the type of the symbol (`int`) has already been given at the first definition location, it does not need to be repeated here. Only giving the type once at the "base" definition of the symbol is a good idea for reasons explained in kconfig_shorthands.

`default` values in `Kconfig.defconfig` files have priority over
`default` values given on the "base" definition of a symbol. Internally, this
is implemented by including the `Kconfig.defconfig` files first. Kconfig
uses the first `default` with a satisfied condition, where an empty condition
corresponds to `if y` (is always satisfied).

Note that conditions from surrounding top-level `if`\ s are propagated to
symbol properties, so the above `default` is equivalent to
`default 32 if BOARD_MY_BOARD`.


### Multiple symbol definitions


When a symbol is defined in multiple locations, each definition acts as an
independent symbol that happens to share the same name. This means that
properties are not appended to previous definitions. If the conditions
for **ANY** definition result in the symbol resolving to `y`, the symbol
will be `y`. It is therefore not possible to make the dependencies of a
symbol more restrictive by defining it in multiple locations.

For example, the dependencies of the symbol `FOO` below are satisfied if
either `DEP1` **OR** `DEP2` are true, it does not require both:

```none

config FOO
   ...
   depends on DEP1

config FOO
   ...
   depends on DEP2
```

**Warning:** Symbols without explicit dependencies still follow the above rule. A symbol without any dependencies will result in the symbol always being assignable. The definition below will result in `FOO` always being enabled by default, regardless of the value of `DEP1`. .. code-block:: kconfig config FOO bool "FOO" depends on DEP1 config FOO default y This dependency weakening can be avoided with the configdefault extension if the desire is only to add a new default without modifying any other behaviour of the symbol.


**Note:** When making changes to `Kconfig.defconfig` files, always check the symbol's direct dependencies in one of the interactive configuration interfaces afterwards. It is often necessary to repeat dependencies from the base definition of the symbol to avoid weakening a symbol's dependencies.


### Motivation for Kconfig.defconfig files


One motivation for this configuration scheme is to avoid making fixed
`BOARD`-specific settings configurable in the interactive configuration
interfaces. If all board configuration were done via `<BOARD>_defconfig`,
all symbols would have to be visible, as values given in
`<BOARD>_defconfig` have no effect on invisible symbols.

Having fixed settings be user-configurable would clutter up the configuration
interfaces and make them harder to understand, and would make it easier to
accidentally create broken configurations.

When dealing with fixed board-specific settings, also consider whether they
should be handled via devicetree instead.



### Configuring choices


There are two ways to configure a Kconfig `choice`:

1. By setting one of the choice symbols to `y` in a configuration file.

   Setting one choice symbol to `y` automatically gives all other choice
   symbols the value `n`.

   If multiple choice symbols are set to `y`, only the last one set to `y`
   will be honored (the rest will get the value `n`). This allows a choice
   selection from a board `defconfig` file to be overridden from an
   application `prj.conf` file.

2. By changing the `default` of the choice in `Kconfig.defconfig`.

   As with symbols, changing the default for a choice is done by defining the
   choice in multiple locations. For this to work, the choice must have a name.

   As an example, assume that a choice has the following base definition (here,
   the name of the choice is `FOO`):

```kconfig

choice FOO
    bool "Foo choice"
    default B

config A
    bool "A"

config B
    bool "B"

endchoice
```
   To change the default symbol of `FOO` to `A`, you would add the
   following definition to `Kconfig.defconfig`:

```kconfig

choice FOO
    default A
endchoice
```
The `Kconfig.defconfig` method should be used when the dependencies of
the choice might not be satisfied. In that case, you're setting the default
selection whenever the user makes the choice visible.



#### More Kconfig resources


The kconfig_tips_and_tricks page has some tips for writing Kconfig
files.

The `kconfiglib.py <scripts/kconfig/kconfiglib.py>` docstring
(at the top of the file) goes over how symbol values are calculated in detail.
