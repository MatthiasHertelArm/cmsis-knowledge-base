---
id: "zep-kconfig-tips-and-best-practices-checking-changes-in-menuconfig-guiconfig"
type: "concept"
domain: "project"
title: "Kconfig - Tips and Best Practices: Checking changes in menuconfig/guiconfig"
summary: "When adding new symbols or making other changes to Kconfig files, it is a good idea to look up the symbols in menuconfig or guiconfig afterwards. To get to a symbol quickly, use the jump-to feature (press /)."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/kconfig/tips.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/kconfig/tips.rst"
license: "Apache-2.0"
mode: "V"
---

When adding new symbols or making other changes to Kconfig files, it is a good
idea to look up the symbols in menuconfig or guiconfig
afterwards. To get to a symbol quickly, use the jump-to feature (press
`/`).

Here are some things to check:

* Are the symbols placed in a good spot? Check that they appear in a menu where
  they make sense, close to related symbols.

  If one symbol depends on another, then it's often a good idea to place it
  right after the symbol it depends on. It will then be shown indented relative
  to the symbol it depends on in the `menuconfig` interface, and in a
  separate menu rooted at the symbol in `guiconfig`. This also works if
  several symbols are placed after the symbol they depend on.

* Is it easy to guess what the symbols do from their prompts?

* If many symbols are added, do all combinations of values they can be set to
  make sense?

  For example, if two symbols `FOO_SUPPORT` and `NO_FOO_SUPPORT` are added,
  and both can be enabled at the same time, then that makes a nonsensical
  configuration. In this case, it's probably better to have a single
  `FOO_SUPPORT` symbol.

* Are there any duplicated dependencies?

  This can be checked by selecting a symbol and pressing `?` to view the
  symbol information. If there are duplicated dependencies, then use the
  `Included via ...` path shown in the symbol information to figure out where
  they come from.
