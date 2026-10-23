---
id: "zep-kconfig-tips-and-best-practices-select-statements"
type: "concept"
domain: "project"
title: "Kconfig - Tips and Best Practices: `select` statements"
summary: "The select statement is used to force one symbol to y whenever another symbol is y. For example, the following code forces CONSOLE to y whenever USB_CONSOLE is y:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/kconfig/tips.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/kconfig/tips.rst"
license: "Apache-2.0"
mode: "V"
---

The `select` statement is used to force one symbol to `y` whenever another
symbol is `y`. For example, the following code forces `CONSOLE` to `y`
whenever `USB_CONSOLE` is `y`:

```kconfig

config CONSOLE
    bool "Console support"

...

config USB_CONSOLE
    bool "USB console support"
    select CONSOLE
```
This section covers some pitfalls and good uses for `select`.



### `select` pitfalls


`select` might seem like a generally useful feature at first, but can cause
configuration issues if overused.

For example, say that a new dependency is added to the `CONSOLE` symbol
above, by a developer who is unaware of the `USB_CONSOLE` symbol (or simply
forgot about it):

```kconfig

config CONSOLE
    bool "Console support"
    depends on STRING_ROUTINES
```
Enabling `USB_CONSOLE` now forces `CONSOLE` to `y`, even if
`STRING_ROUTINES` is `n`.

To fix the problem, the `STRING_ROUTINES` dependency needs to be added to
`USB_CONSOLE` as well:

```kconfig

config USB_CONSOLE
    bool "USB console support"
    select CONSOLE
    depends on STRING_ROUTINES

...

config STRING_ROUTINES
    bool "Include string routines"
```
More insidious cases with dependencies inherited from `if` and `menu`
statements are common.

An alternative attempt to solve the issue might be to turn the `depends on`
into another `select`:

```kconfig

config CONSOLE
    bool "Console support"
    select STRING_ROUTINES

...

config USB_CONSOLE
    bool "USB console support"
    select CONSOLE
```
In practice, this often amplifies the problem, because any dependencies added
to `STRING_ROUTINES` now need to be copied to both `CONSOLE` and
`USB_CONSOLE`.

In general, whenever the dependencies of a symbol are updated, the dependencies
of all symbols that (directly or indirectly) select it have to be updated as
well. This is very often overlooked in practice, even for the simplest case
above.

Chains of symbols selecting each other should be avoided in particular, except
for simple helper symbols, as covered below in good_select_use.

Liberal use of `select` also tends to make Kconfig files harder to read, both
due to the extra dependencies and due to the non-local nature of `select`,
which hides ways in which a symbol might get enabled.



### Alternatives to `select`


For the example in the previous section, a better solution is usually to turn
the `select` into a `depends on`:

```kconfig

config CONSOLE
    bool "Console support"

...

config USB_CONSOLE
    bool "USB console support"
    depends on CONSOLE
```
This makes it impossible to generate an invalid configuration, and means that
dependencies only ever have to be updated in a single spot.

An objection to using `depends on` here might be that configuration files
that enable `USB_CONSOLE` now also need to enable `CONSOLE`:

```cfg

CONFIG_CONSOLE=y
CONFIG_USB_CONSOLE=y
```
This comes down to a trade-off, but if enabling `CONSOLE` is the norm, then a
mitigation is to make `CONSOLE` default to `y`:

```kconfig

config CONSOLE
    bool "Console support"
    default y
```
This gives just a single assignment in configuration files:

```cfg

CONFIG_USB_CONSOLE=y
```
Note that configuration files that do not want `CONSOLE` enabled now have to
explicitly disable it:

```cfg

CONFIG_CONSOLE=n
```

### Using `select` for helper symbols


A good and safe use of `select` is for setting "helper" symbols that capture
some condition. Such helper symbols should preferably have no prompt or
dependencies.

For example, a helper symbol for indicating that a particular CPU/SoC has an
FPU could be defined as follows:

```kconfig

config CPU_HAS_FPU
    bool
    help
      If y, the CPU has an FPU

...

config SOC_FOO
    bool
    select CPU_HAS_FPU

...

config SOC_BAR
    bool
    select CPU_HAS_FPU
```
This makes it possible for other symbols to check for FPU support in a generic
way, without having to look for particular architectures:

```kconfig

config FPU
    bool "Support floating point operations"
    depends on CPU_HAS_FPU
```
The alternative would be to have dependencies like the following, possibly
duplicated in several spots:

```kconfig

config FPU
    bool "Support floating point operations"
    depends on SOC_FOO || SOC_BAR || ...
```
Invisible helper symbols can also be useful without `select`. For example,
the following code defines a helper symbol that has the value `y` if the
machine has some arbitrarily-defined "large" amount of memory:

```kconfig

config LARGE_MEM
    def_bool MEM_SIZE >= 64
```

**Note:** This is short for the following: .. code-block:: kconfig config LARGE_MEM bool default MEM_SIZE >= 64


### `select` recommendations


In summary, here are some recommended practices for `select`:

- Avoid selecting symbols with prompts or dependencies. Prefer `depends on`.
  If `depends on` causes annoying bloat in configuration files, consider
  adding a Kconfig default for the most common value.

  Rare exceptions might include cases where you're sure that the dependencies
  of the selecting and selected symbol will never drift out of sync, e.g. when
  dealing with two simple symbols defined close to one another within the same
  `if`.

  Common sense applies, but be aware that `select` often causes issues in
  practice. `depends on` is usually a cleaner and safer solution.

- Select simple helper symbols without prompts and dependencies however much
  you like. They're a great tool for simplifying Kconfig files.

- An exemption are buses like I2C and SPI, and following the same thought
  process things like MFD as well. Drivers on these buses should use
  `select` to allow the automatic activation of the necessary bus drivers
  when devices on the bus are enabled in the devicetree.

```kconfig

config ADC_FOO
   bool "external SPI ADC foo driver"
   select SPI
```
