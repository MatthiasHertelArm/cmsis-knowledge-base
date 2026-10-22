---
id: "core-device-header-file-device-h-configuration-of-the-processor-and-core"
type: "concept"
domain: "core"
title: "Device Header File `<Device.h>`: Configuration of the Processor and Core Peripherals"
summary: "The device_h_pg configures the Cortex-M or SecurCore processors and the core peripherals with #define directives that are set prior to including the file core<cpu>.h."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/core_device_h.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/core_device_h.md#configuration-of-the-processor-and-core-peripherals"
license: "Apache-2.0"
mode: "V"
---

The device_h_pg  configures the Cortex-M or SecurCore processors and the core peripherals with `#define` directives
that are set prior to including the file `core_<cpu>.h`.

The following tables list the _\#defines_ along with the possible values for each processor core.
If these _\#defines_ are missing default values are used.

**Cortex-M0 core** (core_cm0.h)


| \#define | Value Range | Default | Description |
|---|---|---|---|
| __CM0_REV | 0x0000 | 0x0000 | Core revision number ([15:8] revision number, [7:0] patch number) |
| __NVIC_PRIO_BITS | 2 | 2 | Number of priority bits implemented in the NVIC (device specific) |
| __Vendor_SysTickConfig | 0 .. 1 | 0 | Vendor defined **SysTick_Config** function. |



**Cortex-M0+ core** (core_cm0plus.h)


| \#define | Value Range | Default | Description |
|---|---|---|---|
| __CM0PLUS_REV | 0x0000 | 0x0000 | Core revision number ([15:8] revision number, [7:0] patch number) |
| __VTOR_PRESENT | 0 .. 1 | 0 | Defines if a VTOR register is present or not |
| __NVIC_PRIO_BITS | 2 | 2 | Number of priority bits implemented in the NVIC (device specific) |
| __Vendor_SysTickConfig | 0 .. 1 | 0 | Vendor defined **SysTick_Config** function. |



**Cortex-M3 core** (core_cm3.h)


| \#define | Value Range | Default | Description |
|---|---|---|---|
| __CM3_REV | 0x0101 \| 0x0200 | 0x0200 | Core revision number ([15:8] revision number, [7:0] patch number) |
| __VTOR_PRESENT | 0 .. 1 | 1 | Defines if a VTOR register is present or not |
| __NVIC_PRIO_BITS | 2 .. 8 | 4 | Number of priority bits implemented in the NVIC (device specific) |
| __MPU_PRESENT | 0 .. 1 | 0 | Defines if a MPU is present or not |
| __Vendor_SysTickConfig | 0 .. 1 | 0 | Vendor defined **SysTick_Config** function. |



**Cortex-M4 core** (core_cm4.h)


| \#define | Value Range | Default | Description |
|---|---|---|---|
| __CM4_REV | 0x0000 | 0x0000 | Core revision number ([15:8] revision number, [7:0] patch number) |
| __VTOR_PRESENT | 0 .. 1 | 1 | Defines if a VTOR register is present or not |
| __NVIC_PRIO_BITS | 2 .. 8 | 4 | Number of priority bits implemented in the NVIC (device specific) |
| __MPU_PRESENT | 0 .. 1 | 0 | Defines if a MPU is present or not |
| __FPU_PRESENT | 0 .. 1 | 0 | Defines if a FPU is present or not |
| __Vendor_SysTickConfig | 0 .. 1 | 0 | Vendor defined **SysTick_Config** function. |



**Cortex-M7 core** (core_cm7.h)


| \#define | Value Range | Default | Description |
|---|---|---|---|
| __CM7_REV | 0x0000 | 0x0000 | Core revision number ([15:8] revision number, [7:0] patch number) |
| __MPU_PRESENT | 0 .. 1 | 0 | Defines if a MPU is present or not |
| __VTOR_PRESENT | 0 .. 1 | 1 | Defines if a VTOR register is present or not |
| __NVIC_PRIO_BITS | 2 .. 8 | 4 | Number of priority bits implemented in the NVIC (device specific) |
| __Vendor_SysTickConfig | 0 .. 1 | 0 | If this define is set to 1, then the default **SysTick_Config** function is excluded. In this case, the file **device.h** must contain a vendor specific implementation of this function. |
| __FPU_PRESENT | 0 .. 1 | 0 | Defines if a FPU is present or not. |
| __FPU_DP | 0 .. 1 | 0 | The combination of the defines __FPU_PRESENT and __FPU_DP determine whether the FPU is with single or double precision. |
| __ICACHE_PRESENT | 0 .. 1 | 1 | Instruction Chache present or not |
| __DCACHE_PRESENT | 0 .. 1 | 1 | Data Chache present or not |
| __DTCM_PRESENT | 0 .. 1 | 1 | Data Tightly Coupled Memory is present or not |



\if ARMSC
**SecurCore SC000 core** (core_sc000.h)


| \#define | Value Range | Default | Description |
|---|---|---|---|
| __SC000_REV | 0x0000 | 0x0000 | Core revision number ([15:8] revision number, [7:0] patch number) |
| __VTOR_PRESENT | 0 .. 1 | 0 | Defines if a VTOR register is present or not |
| __NVIC_PRIO_BITS | 2 | 2 | Number of priority bits implemented in the NVIC (device specific) |
| __MPU_PRESENT | 0 .. 1 | 0 | Defines if a MPU is present or not |
| __Vendor_SysTickConfig | 0 .. 1 | 0 | Vendor defined **SysTick_Config** function. |


\endif

\if ARMSC
**SecurCore SC300 core** (core_sc300.h)


| \#define | Value Range | Default | Description |
|---|---|---|---|
| __SC300_REV | 0x0000 | 0x0000 | Core revision number ([15:8] revision number, [7:0] patch number) |
| __VTOR_PRESENT | 0 .. 1 | 1 | Defines if a VTOR register is present or not |
| __NVIC_PRIO_BITS | 2 .. 8 | 4 | Number of priority bits implemented in the NVIC (device specific) |
| __MPU_PRESENT | 0 .. 1 | 0 | Defines if a MPU is present or not |
| __Vendor_SysTickConfig | 0 .. 1 | 0 | Vendor defined **SysTick_Config** function. |


\endif

\if ARMv8M
**Cortex-M23 core, Armv8-M Baseline core** (core_cm23.h , core_armv8mbl.h)


| \#define | Value Range | Default | Description |
|---|---|---|---|
| __ARMv8MBL_REV or __CM23_REV | 0x0000 | 0x0000 | Core revision number ([15:8] revision number, [7:0] patch number) |
| __MPU_PRESENT | 0 .. 1 | 0 | Defines if a MPU is present or not |
| __SAUREGION_PRESENT | 0 .. 1 | 0 | Defines if SAU regions are present or not |
| __VTOR_PRESENT | 0 .. 1 | 0 | Defines if a VTOR register is present or not |
| __NVIC_PRIO_BITS | 2 | 2 | Number of priority bits implemented in the NVIC (device specific) |
| __Vendor_SysTickConfig | 0 .. 1 | 0 | Vendor defined **SysTick_Config** function. |


\endif

\if ARMv8M
**Cortex-M33, Cortex-M35P, Armv8-M Mainline core** (core_cm33.h, core_cm35p.h, core_armv8mml.h)


| \#define | Value Range | Default | Description |
|---|---|---|---|
| __ARMv8MML_REV or __CM33_REV or __CM35P_REV | 0x0000 | 0x0000 | Core revision number ([15:8] revision number, [7:0] patch number) |
| __MPU_PRESENT | 0 .. 1 | 0 | Defines if a MPU is present or not |
| __SAUREGION_PRESENT | 0 .. 1 | 0 | Defines if SAU regions are present or not |
| __FPU_PRESENT | 0 .. 1 | 0 | Defines if a FPU is present or not |
| __VTOR_PRESENT | 0 .. 1 | 1 | Defines if a VTOR register is present or not |
| __NVIC_PRIO_BITS | 2 .. 8 | 3 | Number of priority bits implemented in the NVIC (device specific) |
| __Vendor_SysTickConfig | 0 .. 1 | 0 | Vendor defined **SysTick_Config** function. |


\endif

\if ARMv8M
**Cortex-M55 core, Armv8.1-M Mainline core** (core_cm55.h, core_armv81mml.h)


| \#define | Value Range | Default | Description |
|---|---|---|---|
| __ARMv81MML_REV or __CM55_REV | 0x0000 | 0x0000 | Core revision number ([15:8] revision number, [7:0] patch number) |
| __MPU_PRESENT | 0 .. 1 | 0 | Defines if a MPU is present or not |
| __SAUREGION_PRESENT | 0 .. 1 | 0 | Defines if SAU regions are present or not |
| __FPU_PRESENT | 0 .. 1 | 0 | Defines if a FPU is present or not |
| __FPU_DP | 0 .. 1 | 0 | The combination of the defines __FPU_PRESENT and __FPU_DP determine whether the FPU is with single or double precision. |
| __ICACHE_PRESENT | 0 .. 1 | 1 | Instruction Chache present or not |
| __DCACHE_PRESENT | 0 .. 1 | 1 | Data Chache present or not |
| __VTOR_PRESENT | 0 .. 1 | 1 | Defines if a VTOR register is present or not |
| __NVIC_PRIO_BITS | 2 .. 8 | 3 | Number of priority bits implemented in the NVIC (device specific) |
| __Vendor_SysTickConfig | 0 .. 1 | 0 | Vendor defined **SysTick_Config** function. |


\endif

\if ARMv8M
**Cortex-M85 core** (core_cm85.h)


| \#define | Value Range | Default | Description |
|---|---|---|---|
| __CM85_REV | 0x0001 | 0x0001 | Core revision number ([15:8] revision number, [7:0] patch number) |
| __MPU_PRESENT | 0 .. 1 | 0 | Defines if a MPU is present or not |
| __SAUREGION_PRESENT | 0 .. 1 | 0 | Defines if SAU regions are present or not |
| __FPU_PRESENT | 0 .. 1 | 0 | Defines if a FPU is present or not |
| __FPU_DP | 0 .. 1 | 0 | The combination of the defines __FPU_PRESENT and __FPU_DP determine whether the FPU is with single or double precision. |
| __ICACHE_PRESENT | 0 .. 1 | 1 | Instruction Chache present or not |
| __DCACHE_PRESENT | 0 .. 1 | 1 | Data Chache present or not |
| __VTOR_PRESENT | 0 .. 1 | 1 | Defines if a VTOR register is present or not |
| __NVIC_PRIO_BITS | 2 .. 8 | 3 | Number of priority bits implemented in the NVIC (device specific) |
| __Vendor_SysTickConfig | 0 .. 1 | 0 | Vendor defined **SysTick_Config** function. |


\endif

**Example**

The following code exemplifies the configuration of the Cortex-M4 Processor and Core Peripherals.

```c
#define __CM4_REV                 0x0001U   /* Core revision r0p1                                 */
#define __MPU_PRESENT             1U        /* MPU present or not                                 */
#define __VTOR_PRESENT            1U        /* VTOR present */
#define __NVIC_PRIO_BITS          3U        /* Number of Bits used for Priority Levels            */
#define __Vendor_SysTickConfig    0U        /* Set to 1 if different SysTick Config is used       */
#define __FPU_PRESENT             1U        /* FPU present or not                                 */
.
.
#include <core_cm4.h>                       /* Cortex-M4 processor and core peripherals           */
#include "system_<Device>.h"                /* Device System Header                               */
```
