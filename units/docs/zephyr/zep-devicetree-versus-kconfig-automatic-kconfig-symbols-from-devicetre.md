---
id: "zep-devicetree-versus-kconfig-automatic-kconfig-symbols-from-devicetre"
type: "concept"
domain: "project"
title: "Devicetree versus Kconfig: Automatic Kconfig symbols from devicetree"
summary: "During the devicetree processing step, CMake runs scripts/dts/gen_driver_kconfig_dts.py, which scans all DTS root directories, including dts/bindings and writes Kconfig.dts into the build's KCONFIG_BINARY_DIR (for example <build>/zephyr or <build>/<image>/zephyr in case of sysbuild)."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/dt-vs-kconfig.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/dt-vs-kconfig.rst"
license: "Apache-2.0"
mode: "V"
---

During the devicetree processing step, CMake runs
`scripts/dts/gen_driver_kconfig_dts.py`, which scans all
DTS root directories, including `dts/bindings` and
writes `Kconfig.dts` into the build's `KCONFIG_BINARY_DIR` (for example
`<build>/zephyr` or `<build>/<image>/zephyr` in case of sysbuild).
For each `compatible = "vendor,chip"` that appears in a binding, the generated
file contains:

```kconfig

DT_COMPAT_VENDOR_CHIP := vendor,chip

config DT_HAS_VENDOR_CHIP_ENABLED
        def_bool $(dt_compat_enabled,$(DT_COMPAT_VENDOR_CHIP))
```
The assignment keeps the literal `compatible` string available to the
preprocessor functions described in kconfig-functions, so that Kconfig
files can call helpers such as `$(dt_compat_on_bus,$(DT_COMPAT_<compatible>),i2c)`.
Characters like `-`, `,` and `@` are converted to underscores when the
symbol names are created.

The hidden boolean symbol becomes `CONFIG_DT_HAS_<compatible>_ENABLED` after
Kconfig runs. Its value tracks whether the current devicetree contains at least
one node with that `compatible` whose status is
`okay`. Symbols for enabling drivers should almost certainly be `default y`
and have `depends on CONFIG_DT_HAS_<compatible>_ENABLED`, for example:

```kconfig

config SENSOR_VENDOR_CHIP
        bool "Vendor Chip sensor"
        default y
        depends on DT_HAS_VENDOR_CHIP_ENABLED
```
Because these symbols are generated automatically, adding a new binding with
a `compatible` property is all that is required to make the corresponding
`DT_HAS_<compatible>_ENABLED` and `DT_COMPAT_<compatible>` constructs
available to Kconfig.
