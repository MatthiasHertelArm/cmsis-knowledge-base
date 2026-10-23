---
id: "zep-kconfig-tips-and-best-practices-stuck-symbols-in-menuconfig-and-guiconfi"
type: "concept"
domain: "project"
title: "Kconfig - Tips and Best Practices: \"Stuck\" symbols in menuconfig and guiconfig"
summary: "There is a common subtle gotcha related to interdependent configuration symbols with prompts. Consider these symbols:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/kconfig/tips.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/kconfig/tips.rst"
license: "Apache-2.0"
mode: "V"
---

There is a common subtle gotcha related to interdependent configuration symbols
with prompts. Consider these symbols:

```kconfig

config FOO
    bool "Foo"

config STACK_SIZE
    hex "Stack size"
    default 0x200 if FOO
    default 0x100
```
Assume that the intention here is to use a larger stack whenever `FOO` is
enabled, and that the configuration initially has `FOO` disabled. Also,
remember that Zephyr creates an initial configuration in `zephyr/.config`
in the build directory by merging configuration files (including e.g.
`prj.conf`). This configuration file exists before
`menuconfig` or `guiconfig` is run.

When first entering the configuration interface, the value of `STACK_SIZE` is
0x100, as expected. After enabling `FOO`, you might reasonably expect the
value of `STACK_SIZE` to change to 0x200, but it stays as 0x100.

To understand what's going on, remember that `STACK_SIZE` has a prompt,
meaning it is user-configurable, and consider that all Kconfig has to go on
from the initial configuration is this:

```cfg

CONFIG_STACK_SIZE=0x100
```
Since Kconfig can't know if the 0x100 value came from a `default` or was
typed in by the user, it has to assume that it came from the user. Since
`STACK_SIZE` is user-configurable, the value from the configuration file is
respected, and any symbol defaults are ignored. This is why the value of
`STACK_SIZE` appears to be "frozen" at 0x100 when toggling `FOO`.

The right fix depends on what the intention is. Here's some different scenarios
with suggestions:

- If `STACK_SIZE` can always be derived automatically and does not need to be
  user-configurable, then just remove the prompt:

```kconfig

config STACK_SIZE
    hex
    default 0x200 if FOO
    default 0x100
```
  Symbols without prompts ignore any value from the saved configuration.

- If `STACK_SIZE` should usually be user-configurable, but needs to be set to
  0x200 when `FOO` is enabled, then disable its prompt when `FOO` is
  enabled, as described in optional prompts:

```kconfig

config STACK_SIZE
    hex "Stack size" if !FOO
    default 0x200 if FOO
    default 0x100
```
- If `STACK_SIZE` should usually be derived automatically, but needs to be
  set to a custom value in rare circumstances, then add another option for
  making `STACK_SIZE` user-configurable:

```kconfig

config CUSTOM_STACK_SIZE
    bool "Use a custom stack size"
    help
      Enable this if you need to use a custom stack size. When disabled, a
      suitable stack size is calculated automatically.

config STACK_SIZE
    hex "Stack size" if CUSTOM_STACK_SIZE
    default 0x200 if FOO
    default 0x100
```
  As long as `CUSTOM_STACK_SIZE` is disabled, `STACK_SIZE` will ignore the
  value from the saved configuration.

It is a good idea to try out changes in the `menuconfig` or `guiconfig`
interface, to make sure that things behave the way you expect. This is
especially true when making moderately complex changes like these.
