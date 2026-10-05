---
id: "zep-kconfig-tips-and-best-practices-what-to-turn-into-kconfig-options"
type: "concept"
domain: "project"
title: "Kconfig - Tips and Best Practices: What to turn into Kconfig options"
summary: "When deciding whether something belongs in Kconfig, it helps to distinguish between symbols that have prompts and symbols that don't."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/kconfig/tips.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/kconfig/tips.rst"
license: "Apache-2.0"
mode: "V"
---

When deciding whether something belongs in Kconfig, it helps to distinguish
between symbols that have prompts and symbols that don't.

If a symbol has a prompt (e.g. `bool "Enable foo"`), then the user can change
the symbol's value in the `menuconfig` or `guiconfig` interface (see
menuconfig), or by manually editing configuration files. Conversely, a
symbol without a prompt can never be changed directly by the user, not even by
manually editing configuration files.

Only put a prompt on a symbol if it makes sense for the user to change its
value.

Symbols without prompts are called *hidden* or *invisible* symbols, because
they don't show up in `menuconfig` and `guiconfig`. Symbols that have
prompts can also be invisible, when their dependencies are not satisfied.

Symbols without prompts can't be configured directly by the user (they derive
their value from other symbols), so less restrictions apply to them. If some
derived setting is easier to calculate in Kconfig than e.g. during the build,
then do it in Kconfig, but keep the distinction between symbols with and
without prompts in mind.

See the optional prompts section for a way to deal with settings that are
fixed on some machines and configurable on other machines.
