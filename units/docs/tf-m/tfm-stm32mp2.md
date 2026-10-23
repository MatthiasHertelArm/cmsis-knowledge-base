---
id: "tfm-stm32mp2"
type: "concept"
domain: "security"
title: "STM32MP2"
summary: "The STM32MP2 series embed an Arm Cortex-A35 (single or dual) and Cortex-M33 cores."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/stm/stm32mp2/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/stm/stm32mp2/.html"
license: "BSD-3-Clause"
mode: "V"
---

The STM32MP2 series embed an Arm Cortex-A35 (single or dual) and Cortex-M33 cores.

Depending on which core owns the Trusted Domain of the platform, the Arm Cortex-M33 can be:

- Owner of Trusted Domain (TDCID) and launched by ROM code: M33-TD flavor (default)
- A simple co-processor launched by the Cortex-A35 (`STM32_M33TDCID=OFF`): A35-TD
  flavor (not yet available on TF-M)


**Note:** Currently, this platform can only be built using GCC (GNU ARM Embedded toolchain). * Profile supported: - TF-M Profile medium design: `-DTFM_PROFILE=profile_medium` - TF-M Profile small design: `-DTFM_PROFILE=profile_small` * Hardware configuration: This platform uses the device tree (DT) to describe the hardware available on boards. Based on Zephyr devicetree concept * The board defines a default device tree (dts), but if needed, an external device tree can be used for your components (BL2 | S | NS): - `-DDTS_EXT_DIR=<external_dt_path>` - `-DDTS_BOARD_S=<dts_file_secure>` - `-DDTS_BOARD_NS=<dts_file_non_secure>` - `-DDTS_BOARD_BL2=<dts_file_bl2>`
