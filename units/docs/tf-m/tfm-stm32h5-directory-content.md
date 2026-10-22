---
id: "tfm-stm32h5-directory-content"
type: "concept"
domain: "security"
title: "STM32H5: Directory content"
summary: "STM32H5: Directory content"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/stm/stm32h573i_dk/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/stm/stm32h573i_dk/.html#directory-content"
license: "BSD-3-Clause"
mode: "V"
---

- stm/common/stm32h5xx/stm32h5xx_hal:
   Content from https://github.com/STMicroelectronics/stm32h5xx_hal_driver

- stm/common/stm32h5xx/Device:
   Content from https://github.com/STMicroelectronics/cmsis_device_h5

- stm/common/stm32h5xx/bl2:
   stm32h5xx bl2 code specific from https://github.com/STMicroelectronics/STM32CubeH5.git (Projects/STM32H573I_DK/Applications/TFM)

- stm/common/stm32h5xx/secure:
   stm32h5xx Secure porting adaptation from https://github.com/STMicroelectronics/STM32CubeH5.git (Projects/STM32H573I_DK/Applications/TFM)

- stm/common/stm32h5xx/boards:
   Adaptation and tools specific to stm32 board using stm32h5xx soc from https://github.com/STMicroelectronics/STM32CubeH5.git (Projects/STM32H573I_DK/Applications/TFM)

- stm/common/stm32h5xx/CMSIS_Driver:
   Flash and uart driver for stm32h5xx platform

- stm/common/stm32h5xx/Native_Driver:
   Random generator and tickless implementation
