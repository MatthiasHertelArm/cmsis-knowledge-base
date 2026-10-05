---
id: "zep-additional-zephyr-extension-comman-indexing-the-sources-with-gnu-global-wes"
type: "concept"
domain: "project"
title: "Additional Zephyr extension commands: Indexing the sources with GNU Global: `west gtags`"
summary: "The west gtags command lets you create a GNU Global tags file for the entire west workspace::"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/zephyr-cmds.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/zephyr-cmds.rst"
license: "Apache-2.0"
mode: "V"
---

**Important:** You must install the `gtags` and `global` programs provided by GNU Global to use this command.

The `west gtags` command lets you create a GNU Global tags file for the entire
west workspace::
```
west gtags
```
This will create a tags file named `GTAGS` in the workspace :ref:`topdir
<west-workspace>` (it will also create other Global-related metadata files
named `GPATH` and `GRTAGS` in the same place).

You can then run the `global` command anywhere inside the
workspace to search for symbol locations using this tags file.

For example, to search for definitions of the `arch_system_halt()` function,
starting from the `zephyr/drivers` directory::
```
$ cd zephyr/drivers
$ global -x arch_system_halt
arch_system_halt   65 ../arch/arc/core/fatal.c FUNC_NORETURN void arch_system_halt(unsigned int reason)
arch_system_halt  455 ../arch/arm64/core/fatal.c FUNC_NORETURN void arch_system_halt(unsigned int reason)
arch_system_halt  137 ../arch/nios2/core/fatal.c FUNC_NORETURN void arch_system_halt(unsigned int reason)
arch_system_halt   18 ../arch/posix/core/fatal.c FUNC_NORETURN void arch_system_halt(unsigned int reason)
arch_system_halt   17 ../arch/x86/core/fatal.c FUNC_NORETURN void arch_system_halt(unsigned int reason)
arch_system_halt  126 ../arch/xtensa/core/fatal.c FUNC_NORETURN void arch_system_halt(unsigned int reason)
arch_system_halt   21 ../kernel/fatal.c FUNC_NORETURN __weak void arch_system_halt(unsigned int reason)
```
This prints the search symbol, the line it is defined on, a relative path to
the file it is defined in, and the line itself, for all places where the symbol
is defined.

Additional tips:

- This can also be useful to search for vendor HAL function definitions.

- See the `global` command's manual page for more information on how to use
  this tool.

- You should run `global`, **not** `west global`. There is no need for a
  separate `west global` command since `global` already searches for the
  `GTAGS` file starting from your current working directory. This is why you
  need to run `global` from inside the workspace.
