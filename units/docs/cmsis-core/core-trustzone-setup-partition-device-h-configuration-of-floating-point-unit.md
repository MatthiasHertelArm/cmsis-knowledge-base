---
id: "core-trustzone-setup-partition-device-h-configuration-of-floating-point-unit"
type: "concept"
domain: "core"
title: "TrustZone setup: partition_<Device>.h: Configuration of Floating Point Unit"
summary: "TrustZone setup: partition_<Device>.h: Configuration of Floating Point Unit"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/core_partition_device_h.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/core_partition_device_h.md#configuration-of-floating-point-unit"
license: "Apache-2.0"
mode: "V"
---

| \#define | Value Range | Default | Description |
|---|---|---|---|
| TZ_FPU_NS_USAGE | 0 .. 1 | 1 | Setup behaviour of Floating Point Unit - 0: not setup of NSACR and FPCCR registers; the values below are not relevant - 1: setup of NSACR and FPCCR registers with values below |
| SCB_NSACR_CP10_11_VAL | 0 or 3 | 3 | Floating Point Unit usage (Value for SCB->NSACR register bits CP10, CP11) - 0: Secure state only - 3: Secure and Non-Secure state |
| FPU_FPCCR_TS_VAL | 0 .. 1 | 0 | Treat floating-point registers as Secure (value for FPU->FPCCR register bit TS) - 0: Disable - 1: Enabled |
| FPU_FPCCR_CLRONRETS_VAL | 0 .. 1 | 0 | Clear on return (CLRONRET) accessibility (Value for FPU->FPCCR register bit CLRONRETS) - 0: Secure and Non-Secure state - 1: Secure state only |
| FPU_FPCCR_CLRONRET_VAL | 0 .. 1 | 1 | Clear floating-point caller saved registers on exception return (Value for FPU->FPCCR register bit CLRONRET) - 0: Disabled - 1: Enabled |
