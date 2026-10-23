---
id: "zep-board-porting-guide-write-kconfig-files"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: Write Kconfig files"
summary: "Zephyr uses the Kconfig language to configure software features. Your board needs to provide some Kconfig settings before you can compile a Zephyr application for it."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr uses the Kconfig language to configure software features. Your board
needs to provide some Kconfig settings before you can compile a Zephyr
application for it.

Setting Kconfig configuration values is documented in detail in
setting_configuration_values.

There is one mandatory Kconfig file in the board directory, and several optional
files for a board named `plank`:

```none

boards/<vendor>/plank
├── Kconfig
├── Kconfig.plank
├── Kconfig.defconfig
└── plank_<qualifiers>_defconfig
```
`Kconfig.plank`
  A shared Kconfig file which can be sourced both in Zephyr Kconfig and sysbuild
  Kconfig trees.

  This file selects the SoC in the Kconfig tree and potential other SoC related
  Kconfig settings. This file must not select anything outside the reusable
  Kconfig board and SoC trees.

  A `Kconfig.plank` may look like this:

```kconfig

config BOARD_PLANK
        select SOC_SOC1
```
  The Kconfig symbols `BOARD_{board}` and
  `BOARD_{normalized_board_target}` are constructed by the build
  system, therefore no type shall be defined in above code snippet.

`Kconfig`
  Included by `boards/Kconfig`.

  This file can add Kconfig settings which are specific to the current board.

  Not all boards have a `Kconfig` file.

  A board specific setting should be defining a custom setting and usually with
  a prompt, like this:

```kconfig

config BOARD_FEATURE
        bool "Board specific feature"
```
  If the setting name is identical to an existing Kconfig setting in Zephyr and
  only modifies the default value of said setting, then
  `Kconfig.defconfig` should be used  instead.

`Kconfig.defconfig`
  Board-specific default values for Kconfig options.

  Not all boards have a `Kconfig.defconfig` file.

  The entire file should be inside an `if BOARD_PLANK` / `endif` pair of
  lines, like this:

```kconfig

if BOARD_PLANK

config FOO
        default y

if NETWORKING

config SOC_ETHERNET_DRIVER
        default y

endif # NETWORKING

endif # BOARD_PLANK
```
`plank_<qualifiers>_defconfig` (or `plank_defconfig` in limited circumstances)
  A Kconfig fragment that is merged as-is into the final build directory
  `.config` whenever an application is compiled for your board.

  `plank_defconfig` can only be used with boards that have no qualifiers, no variants and a
  single SoC present, though this style of naming is not recommended due to samples/tests or
  downstream usage breaking suddenly without warning if a new SoC or board variant/qualifier is
  added to an board in upstream Zephyr.


**Note:** Multiple files are not merged and there is no fallback mechanism for files, this means if there is a board with 2 different SoCs and each one has 2 board variants, a `plank_defconfig` file would be wholly unused, for the first qualifier and variant The `_defconfig` should contain mandatory settings for your UART, console, etc. The results are architecture-specific, but typically look something like this: .. code-block:: cfg CONFIG_GPIO=y CONFIG_CONSOLE=y CONFIG_UART_CONSOLE=y CONFIG_SERIAL=y

`plank_x_y_z_defconfig` / `plank_<qualifiers>_x_y_z_defconfig`
  A Kconfig fragment that is merged as-is into the final build directory
  `.config` whenever an application is compiled for your board revision
  `x.y.z`.
