---
id: "zepb-mimxrt1060-evk-external-memory"
type: "concept"
domain: "bring-up"
title: "mimxrt1060_evk: Hardware / External Memory"
summary: "This platform has the following external memories:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/nxp/mimxrt1060_evk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1060_evk/doc/index.html#external-memory"
license: "Apache-2.0"
mode: "V"
---

_Part of: Hardware_

This platform has the following external memories:

+--------------------+------------+-------------------------------------+
| Device             | Controller | Status                              |
+====================+============+=====================================+
| IS25WP064AJBLE     | SEMC       | Enabled via device configuration    |
|                    |            | data block, which sets up SEMC at   |
|                    |            | boot time                           |
+--------------------+------------+-------------------------------------+
| IS42S16160J        | FLEXSPI    | Enabled via flash configuration     |
|                    |            | block, which sets up FLEXSPI at     |
|                    |            | boot time.                          |
+--------------------+------------+-------------------------------------+
