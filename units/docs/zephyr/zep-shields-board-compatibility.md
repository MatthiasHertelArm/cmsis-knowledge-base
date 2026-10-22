---
id: "zep-shields-board-compatibility"
type: "concept"
domain: "bring-up"
title: "Shields: Board compatibility"
summary: "Hardware shield-to-board compatibility depends on the use of well-known connectors used on popular boards (such as Arduino and 96boards). For software compatibility, boards must also provide a configuration matching their supported connectors."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/shields.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/shields.rst"
license: "Apache-2.0"
mode: "V"
---

Hardware shield-to-board compatibility depends on the use of well-known
connectors used on popular boards (such as Arduino and 96boards).  For
software compatibility, boards must also provide a configuration matching
their supported connectors.

This should be done at two different level:

* Pinmux: Connector pins should be correctly configured to match shield pins

* Devicetree: A board devicetree file,
  `BOARD.dts` should define an alternate nodelabel for each connector interface.
  For example, for Arduino I2C:

```devicetree

arduino_i2c: &i2c1 {};
```

### Board specific shield configuration


If modifications are needed to fit a shield to a particular board or board
revision, you can override a shield description for a specific board by adding
board or board revision overriding files to a shield, as follows:

```none

boards/shields/<shield>
└── boards
    ├── <board>_<revision>.overlay
    ├── <board>.overlay
    ├── <board>.defconfig
    ├── <board>_<revision>.conf
    └── <board>.conf
```
