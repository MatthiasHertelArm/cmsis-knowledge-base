---
id: "zep-shields-shield-porting-and-configuration"
type: "concept"
domain: "bring-up"
title: "Shields: Shield porting and configuration"
summary: "Shield configuration files are available in the board directory under boards/shields:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/porting/shields.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/porting/shields.rst"
license: "Apache-2.0"
mode: "V"
---

Shield configuration files are available in the board directory
under `boards/shields`:

```none

boards/shields/<shield>
├── shield.yml
├── <shield>.overlay
├── Kconfig.shield
├── Kconfig.defconfig
└── pre_dt_shield.cmake
```
These files provides shield configuration as follows:

* **shield.yml**: This file provides metadata about the shield in YAML format.
  It must contain the following fields:

  * `name`: Name of the shield used in Kconfig and build system (required)
  * `full_name`: Full commercial name of the shield (required)
  * `vendor`: Manufacturer/vendor of the shield (required)
  * `supported_features`: List of hardware features the shield supports (optional). In order to
    help users identify the features a shield supports without having to dig into its overlay file,
    the `supported_features` field can be used to list the types of features the shield supports.
    The values should be the same as the ones defined in the
    `dts/bindings/binding-types.txt` file.

  Example:

```yaml

name: foo_shield
full_name: Foo Shield for Arduino
vendor: acme
supported_features:
  - display
  - input
```
* **<shield>.overlay**: This file provides a shield description in devicetree
  format that is merged with the board's devicetree
  before compilation.

* **Kconfig.shield**: This file defines shield Kconfig symbols that will be
  used for default shield configuration. To ease use with applications,
  the default shield configuration here should be consistent with those in
  the default_board_configuration.

* **Kconfig.defconfig**: This file defines the default shield configuration. It
  is made to be consistent with the default_board_configuration. Hence,
  shield configuration should be done by keeping in mind that features
  activation is application responsibility.

* **pre_dt_shield.cmake**: This optional file can be used to pass additional
  arguments to the devicetree compiler `dtc`.

Besides, in order to avoid name conflicts with devices that may be defined at
board level, it is advised, specifically for shields devicetree descriptions,
to provide a device nodelabel is the form <device>_<shield>, for instance:

```devicetree

sdhc_myshield: sdhc@1 {
        reg = <1>;
        ...
};
```
