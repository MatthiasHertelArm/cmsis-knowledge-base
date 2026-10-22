---
id: "core-trustzone-setup-partition-device-h-sau-ctrl-register-settings"
type: "concept"
domain: "core"
title: "TrustZone setup: partition_<Device>.h: SAU CTRL register settings"
summary: "TrustZone setup: partition_<Device>.h: SAU CTRL register settings"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/core_partition_device_h.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/core_partition_device_h.md#sau-ctrl-register-settings"
license: "Apache-2.0"
mode: "V"
---

| \#define | Value Range | Default | Description |
|---|---|---|---|
| SAU_INIT_CTRL | 0 .. 1 | 0 | Initialize SAU CTRL register or not - 0: do not initialize SAU CTRL register - 1: initialize SAU CTRL register |
| SAU_INIT_CTRL_ENABLE | 0 .. 1 | 0 | enable/disable the SAU - 0: disable SAU - 1: enable SAU |
| SAU_INIT_CTRL_ALLNS | 0 .. 1 | 0 | value for SAU_CTRL register bit ALLNS - 0: all Memory is Secure - 1: all Memory is Non-Secure |
