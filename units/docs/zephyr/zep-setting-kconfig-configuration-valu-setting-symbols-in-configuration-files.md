---
id: "zep-setting-kconfig-configuration-valu-setting-symbols-in-configuration-files"
type: "concept"
domain: "project"
title: "Setting Kconfig configuration values: Setting symbols in configuration files"
summary: "Visible symbols can be configured by setting them in configuration files. The initial configuration is produced by merging a defconfig file for the board with application settings, usually from prj.conf. See initial-conf below for more details."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/kconfig/setting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/kconfig/setting.rst"
license: "Apache-2.0"
mode: "V"
---

Visible symbols can be configured by setting them in configuration files. The
initial configuration is produced by merging a `*_defconfig` file for the
board with application settings, usually from `prj.conf`. See
initial-conf below for more details.

Assignments in configuration files use this syntax:

```cfg

CONFIG_<symbol name>=<value>
```
There should be no spaces around the equals sign.

`bool` symbols can be enabled or disabled by setting them to `y` or `n`,
respectively. The `FPU` symbol from the example above could be enabled like
this:

```cfg

CONFIG_FPU=y
```

**Note:** A boolean symbol can also be set to `n` with a comment formatted like this: .. code-block:: cfg # CONFIG_SOME_OTHER_BOOL is not set This is the format you will see in the merged configuration saved to `zephyr/.config` in the build directory. This style is accepted for historical reasons: Kconfig configuration files can be parsed as makefiles (though Zephyr doesn't use this). Having `n`-valued symbols correspond to unset variables simplifies tests in Make.

Other symbol types are assigned like this:

```cfg

CONFIG_SOME_STRING="cool value"
CONFIG_SOME_INT=123
```
Comments use a #:

```cfg

# This is a comment
```
Assignments in configuration files are only respected if the dependencies for
the symbol are satisfied. A warning is printed otherwise. To figure out what
the dependencies of a symbol are, use one of the :ref:`interactive
configuration interfaces <menuconfig>` (you can jump directly to a symbol with
`/`), or look up the symbol in the :ref:`Kconfig search page
<kconfig-search>`.
