---
id: "tfm-stm32mp2-directory-content"
type: "concept"
domain: "security"
title: "STM32MP2: Directory content"
summary: "STM32MP2: Directory content"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/stm/stm32mp2/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/stm/stm32mp2/.html#directory-content"
license: "BSD-3-Clause"
mode: "V"
---

- stm/common/stm32mp2xx/bl2:
   Specific code for bl2 platform initialisation.

- stm/common/stm32mp2xx/cmsis_driver:
   CMSIS interface to drivers.

- stm/common/stm32mp2xx/lib
   Specific libraries like qsort...

- stm/common/stm32mp2xx/linker_scripts:
   Specific linker script for bl2, TF-M secure and non secure.

- stm/common/stm32mp2xx/native_driver:
   Framework and drivers for system (with device tree support).

- stm/common/stm32mp2xx/stm32mp[21|23|25]
   Soc variant directory to define specific needs like config, cmakelist, startup...

- stm/common/stm32mp2xx/secure:
   Secure adaptation for STM32MP2 SOC device.

- stm/common/stm32mp2xx/secure_fw
   Secure firmware and the exported interfaces for application.

-------------

*Copyright (c) 2026 STMicroelectronics. All rights reserved.*
*SPDX-License-Identifier: BSD-3-Clause*
