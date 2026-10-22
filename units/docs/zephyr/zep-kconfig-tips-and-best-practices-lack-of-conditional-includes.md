---
id: "zep-kconfig-tips-and-best-practices-lack-of-conditional-includes"
type: "concept"
domain: "project"
title: "Kconfig - Tips and Best Practices: (Lack of) conditional includes"
summary: "if blocks add dependencies to each item within the if, as if depends on was used."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/kconfig/tips.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/kconfig/tips.rst"
license: "Apache-2.0"
mode: "V"
---

`if` blocks add dependencies to each item within the `if`, as if ``depends
on`` was used.

A common misunderstanding related to `if` is to think that the following code
conditionally includes the file `Kconfig.other`:

```kconfig

if DEP

source "Kconfig.other"

endif
```
In reality, there are no conditional includes in Kconfig. `if` has no special
meaning around a `source`.


**Note:** Conditional includes would be impossible to implement, because `if` conditions may contain (either directly or indirectly) forward references to symbols that haven't been defined yet.

Say that `Kconfig.other` above contains this definition:

```kconfig

config FOO
    bool "Support foo"
```
In this case, `FOO` will end up with this definition:

```kconfig

config FOO
    bool "Support foo"
    depends on DEP
```
Note that it is redundant to add `depends on DEP` to the definition of
`FOO` in `Kconfig.other`, because the `DEP` dependency has already
been added by `if DEP`.

In general, try to avoid adding redundant dependencies. They can make the
structure of the Kconfig files harder to understand, and also make changes more
error-prone, since it can be hard to spot that the same dependency is added
twice.
