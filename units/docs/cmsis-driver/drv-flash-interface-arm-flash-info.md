---
id: "drv-flash-interface-arm-flash-info"
type: "concept"
domain: "drivers"
title: "Flash Interface: ARM_FLASH_INFO"
summary: "Stores the characteristics of a Flash device. This includes sector layout, programming size and a default value for erased memory."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_FLASH_INFO
```

 
Stores the characteristics of a Flash device. This includes sector layout, programming size and a default value for erased memory.
This information can be obtained from the Flash device datasheet and is used by the middleware in order to properly interact with the Flash device.

Sector layout is described by specifying the **sector_info** which points to an array of sector information (start and end address) and by specifying the **sector_count** which defines the number of sectors.
The element **sector_size** is not used in this case and needs to be **0.**
Flash sectors need not to be aligned continuously. Gaps are allowed in the device memory space in order to reserve sectors for other usage (for example application code).

When the device has uniform sector size than the sector layout can be described by specifying the **sector_size** which defines the size of a single sector and by specifying the **sector_count** which defines the number of sectors.
The element **sector_info** is not used in this case and needs to be **NULL.**

The smallest programmable unit within a sector is specified by the **program_unit.** It defines the granularity for programming data.

Optimal programming page size is specified by the **page_size** and defines the amount of data that should be programmed in one step to achieve maximum programming speed.

Contents of erased memory is specified by the **erased_value** and is typically **0xFF.** This value can be used before erasing a sector to check if the sector is blank and erase can be skipped.

******************************************************************************************************************
