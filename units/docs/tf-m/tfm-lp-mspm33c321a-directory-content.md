---
id: "tfm-lp-mspm33c321a-directory-content"
type: "concept"
domain: "security"
title: "LP_MSPM33C321A: Directory Content"
summary: "To use driverlib sources from an existing SDK installation instead, pass -DTFM_PLATFORM_TI_HAL_FILE_PATH=/path/to/mspm33_sdk to CMake."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/ti/LP_MSPM33C321A/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/ti/LP_MSPM33C321A/.html#directory-content"
license: "BSD-3-Clause"
mode: "V"
---

- `platform/ext/target/ti/LP_MSPM33C321A/Native_Driver/`:
   Bundled TI driverlib sources required by the platform (flash controller,
   UART, GPIO, GSC, sysctl). Taken from the
   [MSP SDK](https://www.ti.com/tool/MSPM0-SDK) (BSD-3-Clause).
   No external SDK installation is required to build.

   To use driverlib sources from an existing SDK installation instead, pass
   `-DTFM_PLATFORM_TI_HAL_FILE_PATH=/path/to/mspm33_sdk` to CMake.

- `platform/ext/target/ti/LP_MSPM33C321A/cmsis_drivers/`:
   CMSIS-compliant Flash and USART driver wrappers.
