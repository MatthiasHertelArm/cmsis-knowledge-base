---
id: "core-trustzone-setup-partition-device-h-configuration-of-sleep-and-exception-beh"
type: "concept"
domain: "core"
title: "TrustZone setup: partition_<Device>.h: Configuration of Sleep and Exception behaviour"
summary: "TrustZone setup: partition_<Device>.h: Configuration of Sleep and Exception behaviour"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/core_partition_device_h.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/core_partition_device_h.md#configuration-of-sleep-and-exception-behaviour"
license: "Apache-2.0"
mode: "V"
---

| \#define | Value Range | Default | Description |
|---|---|---|---|
| SCB_CSR_AIRCR_INIT | 0 .. 1 | 1 | Setup behaviour of Sleep and Exception Handling - 0: not setup of CSR and AIRCR registers; the values below are not relevant - 1: setup of CSR and AIRCR registers with values below |
| CSR_INIT_DEEPSLEEPS_VAL | 0 .. 1 | 1 | value for SCB_CSR register bit DEEPSLEEPS - 0: Deep Sleep can be enabled by Secure and Non-Secure state - 1: Deep Sleep can be enabled by Secure state only |
| AIRCR_INIT_SYSRESETREQS_VAL | 0 .. 1 | 1 | value for SCB_AIRCR register bit SYSRESETREQS - 0: System reset request accessible from Secure and Non-Secure state - 1: System reset request accessible from Secure state only |
| AIRCR_INIT_PRIS_VAL | 0 .. 1 | 1 | value for SCB_AIRCR register bit PRIS - 0: Priority of Non-Secure exceptions is Not altered - 1: Priority of Non-Secure exceptions is Lowered to 0x80-0xFF |
| AIRCR_INIT_BFHFNMINS_VAL | 0 .. 1 | 0 | value for SCB_AIRCR register bit BFHFNMINS - 0: BusFault, HardFault, and NMI target are Secure state - 1: BusFault, HardFault, and NMI target are Non-Secure state |
