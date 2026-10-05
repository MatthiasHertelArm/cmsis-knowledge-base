---
id: "core-trustzone-setup-partition-device-h-region-isr-setup-partition-gen-h"
type: "concept"
domain: "core"
title: "TrustZone setup: partition_<Device>.h: Region/ISR setup: partition_gen.h"
summary: "The partitiongen.h header file can be generated using CMSIS-Zone."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/core_partition_device_h.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/core_partition_device_h.md#region-isr-setup-partition-gen-h"
license: "Apache-2.0"
mode: "V"
---

The partition_gen.h header file can be generated using [CMSIS-Zone](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/../Zone/index.html).

The partition_<Device>.h file includes the partition_gen.h file with configuration settings for:

  - sau_regions_sect provides configuration of the SAU Address Regions.
  - sau_interrupttarget_sec provides device-specific interrupt target settings.

> **Note**
> - In previous versions of CMSIS-Core(M) the above settings were part of partition_<Device>.h

### Configuration of the SAU Address Regions



    | 
      \#define | 
      Value Range | 
      Default | 
      Description | 
    

    | 
      SAU_REGIONS_MAX | 
      0 .. tbd | 
      8 | 
      maximum number of SAU regions | 
    

    | 
      SAU_INIT_REGION<number> | 
      0 .. 1 | 
      0 | 
      initialize SAU region or not
           - 0: do not initialize SAU region
           - 1: initialize SAU region | 
    

    | 
      SAU_INIT_START<number> | 
      0x00000000 .. 0xFFFFFFE0\n
          [in steps of 32] | 
      0x00000000 | 
      region start address | 
    

    | 
      SAU_INIT_END<number> | 
      0x00000000 .. 0xFFFFFFE0\n
          [in steps of 32] | 
      0x00000000 | 
      region start address | 
    

    | 
      SAU_INIT_NSC<number> | 
      0 .. 1 | 
      0 | 
      SAU region attribute
           - 0: Non-Secure
           - 1: Secure, Non-Secure callable | 
    



The range of `<number>` is from 0 .. SAU_REGIONS_MAX.
A set of these macros must exist for each `<number>`.

The following example shows a set of SAU region macros.

```c
#define SAU_REGIONS_MAX   8                 /* Max. number of SAU regions */

#define SAU_INIT_REGION0    1
#define SAU_INIT_START0     0x00000000      /* start address of SAU region 0 */
#define SAU_INIT_END0       0x001FFFE0      /* end address of SAU region 0 */
#define SAU_INIT_NSC0       1

#define SAU_INIT_REGION1    1
#define SAU_INIT_START1     0x00200000      /* start address of SAU region 1 */
#define SAU_INIT_END1       0x003FFFE0      /* end address of SAU region 1 */
#define SAU_INIT_NSC1       0

#define SAU_INIT_REGION2    1
#define SAU_INIT_START2     0x20200000      /* start address of SAU region 2 */
#define SAU_INIT_END2       0x203FFFE0      /* end address of SAU region 2 */
#define SAU_INIT_NSC2       0

#define SAU_INIT_REGION3    1
#define SAU_INIT_START3     0x40000000      /* start address of SAU region 3 */
#define SAU_INIT_END3       0x40040000      /* end address of SAU region 3 */
#define SAU_INIT_NSC3       0

#define SAU_INIT_REGION4    0
#define SAU_INIT_START4     0x00000000      /* start address of SAU region 4 */
#define SAU_INIT_END4       0x00000000      /* end address of SAU region 4 */
#define SAU_INIT_NSC4       0

#define SAU_INIT_REGION5    0
#define SAU_INIT_START5     0x00000000      /* start address of SAU region 5 */
#define SAU_INIT_END5       0x00000000      /* end address of SAU region 5 */
#define SAU_INIT_NSC5       0

#define SAU_INIT_REGION6    0
#define SAU_INIT_START6     0x00000000      /* start address of SAU region 6 */
#define SAU_INIT_END6       0x00000000      /* end address of SAU region 6 */
#define SAU_INIT_NSC6       0

#define SAU_INIT_REGION7    0
#define SAU_INIT_START7     0x00000000      /* start address of SAU region 7 */
#define SAU_INIT_END7       0x00000000      /* end address of SAU region 7 */
#define SAU_INIT_NSC7       0
```


### Configuration of Interrupt Target settings

Each interrupt has a configuration bit that defines the execution in Secure or Non-secure state. The Non-Secure interrupts have a separate vector table.  Refer to Model_TrustZone for more information.



    | 
      \#define | 
      Value Range | 
      Default | 
      Description | 
    

    | 
      NVIC_INIT_ITNS<number> | 
      0x00000000 .. 0xFFFFFFFF\n
          [each bit represents an interrupt] | 
      0x00000000 | 
      Interrupt vector target
           - 0: Secure state
           - 1: Non-Secure state | 
    



The range of `<number>` is 0 .. (\`<number of external interrupts\>` + 31) / 32.

The following example shows the configuration for a maximum of 64 external interrupts.

```c
#define NVIC_INIT_ITNS0      0x0000122B
#define NVIC_INIT_ITNS1      0x0000003A
```
