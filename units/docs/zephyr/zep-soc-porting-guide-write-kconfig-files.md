---
id: "zep-soc-porting-guide-write-kconfig-files"
type: "concept"
domain: "bring-up"
title: "SoC Porting Guide: Write Kconfig files"
summary: "Zephyr uses the Kconfig language to configure software features. Your SoC needs to provide some Kconfig settings before you can compile a Zephyr application for it."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/soc_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/soc_porting.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr uses the Kconfig language to configure software features. Your SoC
needs to provide some Kconfig settings before you can compile a Zephyr
application for it.

Setting Kconfig configuration values is documented in detail in
setting_configuration_values.

There is one mandatory Kconfig file in the SoC directory, and two optional
files for a SoC:

```none

soc/<vendor>/<your soc>
├── Kconfig.soc
├── Kconfig
└── Kconfig.defconfig
```
`Kconfig.soc`
  A shared Kconfig file which can be sourced both in Zephyr Kconfig and sysbuild
  Kconfig trees.

  This file selects the SoC family and series in the Kconfig tree and potential
  other SoC related Kconfig settings. In some cases a SOC_PART_NUMBER.
  This file must not select anything outside the reusable Kconfig SoC tree.

  A `Kconfig.soc` may look like this:

```kconfig

config SOC_FAMILY_<SOC_FAMILY_NAME>
        bool

config SOC_SERIES_<SOC_SERIES_NAME>
        bool
        select SOC_FAMILY_<SOC_FAMILY_NAME>

config SOC_<SOC_NAME>
        bool
        select SOC_SERIES_<SOC_SERIES_NAME>

config SOC_FAMILY
        default "<soc_family_name>" if SOC_FAMILY_<SOC_FAMILY_NAME>

config SOC_SERIES
        default "<soc_series_name>" if SOC_SERIES_<SOC_SERIES_NAME>

config SOC
        default "<soc_name>" if SOC_<SOC_NAME>
```
  Notice that `SOC_NAME` is a pure uppercase version of the SoC name, `SOC_SERIES_NAME` is
  a pure uppercase version of SoC series name and `SOC_FAMILY_NAME` is a pure uppercase version
  of the SoC family name. If these fields do not appear in the `soc.yml` file then they
  should not be present in the `Kconfig.soc` file.

  The Kconfigs `SOC`, `SOC_SERIES` and `SOC_FAMILY` settings are globally defined as
  strings and therefore the `Kconfig.soc` file shall only define the default string values
  and not the types. Notice that the string values must match the values used in the
  `soc.yml` file.


**Note:** The build system supports any variation of case for `soc_name`, `soc_series_name` and `soc_family_mame`, but when submitting boards for inclusion in Zephyr itself, these must be purely lowercase versions of the Kconfig names

`Kconfig`
  Included by `soc/Kconfig`.

  This file can add Kconfig settings which are specific to the current SoC.

  The `Kconfig` will often indicate given hardware support using a setting
  of the form `HAS_<support>`.

```kconfig

config SOC_<SOC_NAME>
        select ARM
        select CPU_HAS_FPU
```
  If the setting name is identical to an existing Kconfig setting in Zephyr and
  only modifies the default value of said setting, then
  `Kconfig.defconfig` should be used  instead.

`Kconfig.defconfig`
  SoC specific default values for Kconfig options.

  Not all SoCs have a `Kconfig.defconfig` file.

  The entire file should be inside a pair of `if SOC_<SOC_NAME>` / `endif`
  or `if SOC_SERIES_<SERIES_NAME>` / `endif`, like this:

```kconfig

if SOC_<SOC_NAME>

config NUM_IRQS
        default 32

endif # SOC_<SOC_NAME>
```

### Multiple CPU clusters


CPU clusters must provide additional Kconfig settings in the `Kconfig.soc`
file. This will usually be in the form of `SOC_<SOC_NAME>_<CLUSTER>` so for
a given `soc1` with two clusters `clusterA` and `clusterB`, then this
will look like:

SoC's When a SoC defines CPU cluster

```kconfig

config SOC_SOC1_CLUSTERA
        bool
        select SOC_SOC1

config SOC_SOC1_CLUSTERB
        bool
        select SOC_SOC1
```
