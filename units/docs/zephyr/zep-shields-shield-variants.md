---
id: "zep-shields-shield-variants"
type: "concept"
domain: "bring-up"
title: "Shields: Shield variants"
summary: "Some shields may support several variants or revisions. In that case, it is possible to provide multiple version of the shields description:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/shields.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/shields.rst"
license: "Apache-2.0"
mode: "V"
---

Some shields may support several variants or revisions. In that case, it is
possible to provide multiple version of the shields description:

```none

boards/shields/<shield>
├── <shield_v1>.overlay
├── <shield_v1>.defconfig
├── <shield_v2>.overlay
└── <shield_v2>.defconfig
```
In this case, a shield-particular revision name can be used:

You can also provide a board-specific configuration to a specific shield
revision:

```none

boards/shields/<shield>
├── <shield_v1>.overlay
├── <shield_v1>.defconfig
├── <shield_v2>.overlay
├── <shield_v2>.defconfig
└── boards
    └── <shield_v2>
        ├── <board>.overlay
        └── <board>.defconfig
```
