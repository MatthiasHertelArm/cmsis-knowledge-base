---
id: "tfm-stm32l5-directory-content"
type: "concept"
domain: "security"
title: "STM32L5: Directory content"
summary: "STM32L5: Directory content"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/stm/nucleo_l552ze_q/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/stm/nucleo_l552ze_q/.html#directory-content"
license: "BSD-3-Clause"
mode: "V"
---

- stm/common/stm32l5xx/stm32l5xx_hal:
   Content from https://github.com/STMicroelectronics/stm32l5xx_hal_driver.git

- stm/common/stm32l5xx/Device:
   Content from https://github.com/STMicroelectronics/cmsis_device_l5.git

- stm/common/stm32l5xx/bl2:
   stm32l5xx bl2 code specific from https://github.com/STMicroelectronics/STM32CubeL5.git (Projects/STM32L562E-DK/Applications/TFM)

- stm/common/stm32l5xx/secure:
   stm32l5xx Secure porting adaptation from https://github.com/STMicroelectronics/STM32CubeL5.git (Projects/STM32L562E-DK/Applications/TFM)

- stm/common/stm32l5xx/boards:
   Adaptation and tools specific to stm32 board using stm32l5xx soc from https://github.com/STMicroelectronics/STM32CubeL5.git (Projects/STM32L562E-DK/Applications/TFM)

- stm/common/stm32l5xx/CMSIS_Driver:
   Flash and uart driver for stm32l5xx platform

- stm/common/stm32l5xx/Native_Driver:
   Random generator and tickless implementation
