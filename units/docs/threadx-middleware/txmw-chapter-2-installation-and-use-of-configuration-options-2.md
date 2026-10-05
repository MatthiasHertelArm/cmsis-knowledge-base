---
id: "txmw-chapter-2-installation-and-use-of-configuration-options-2"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and use of LevelX: Configuration Options"
summary: "LevelX can be configured at compile time via the conditional defines described below. Simply add the desired define to the compilation of each LevelX source to use the option."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter2.md#configuration-options"
license: "MIT"
mode: "V"
---

LevelX can be configured at compile time via the conditional defines described below. Simply add the desired define to the compilation of each LevelX source to use the option.

- **LX_DIRECT_READ**:  Defined, this option bypasses the NOR flash driver read routine in favor or reading the NOR memory directly, resulting in a significant performance increase.
- **LX_FREE_SECTOR_DATA_VERIFY**: Defined, this causes the LevelX NOR instance open logic to verify free NOR sectors are all ones.
- **LX_NAND_SECTOR_MAPPING_CACHE_SIZE**:  By default this value is 16 and defines the logical sector mapping cache size. Large values improve performance, but cost memory. The minimum size is 8 and all values must be a power of 2.
- **LX_NAND_FLASH_DIRECT_MAPPING_CACHE**: Defined, this creates a direct mapping cache, such that there are no cache misses. It also requires that LX_NAND_SECTOR_MAPPING_CACHE_SIZE represents the exact number of total pages in your flash device.
- **LX_NOR_DISABLE_EXTENDED_CACHE**: Defined, this disabled the extended NOR cache.
- **LX_NOR_EXTENDED_CACHE_SIZE**: By default this value is 8, which represents a maximum of 8 sectors that can be cached in a NOR instance.
- **LX_NOR_SECTOR_MAPPING_CACHE_SIZE**: By default this value is 16 and defines the logical sector mapping cache size. Large values improve performance, but cost memory. The minimum size is 8 and all values must be a power of 2.
- **LX_THREAD_SAFE_ENABLE**: Defined, this makes LevelX thread-safe by using a ThreadX mutex object throughout the API.
- **LX_STANDALONE_ENABLE**: Defined, enables LevelX to be used in standalone mode (without Eclipse ThreadX). By default this symbol is not defined.

  > **Important:** When using LevelX in Standalone mode (**LX_STANDALONE_ENABLE** must be defined), ThreadX files/libraries are not required. LevelX thread-safe feature is disabled in this mode.

- **LX_NOR_FLASH_USER_EXTENSION**: Define user extension for NOR flash control block. User extension is placed at the end of flash control block and it is not cleared on opening flash.
- **LX_NAND_FLASH_USER_EXTENSION**: Define user extension for NAND flash control block. User extension is placed at the end of flash control block and it is not cleared on opening flash.
- **LX_NOR_ENABLE_MAPPING_BITMAP**: Determine if logical sector mapping bitmap should be enabled in extended cache. Cache memory will be allocated to sector mapping bitmap first. One bit can be allocated for each physical sector.
- **LX_NOR_ENABLE_OBSOLETE_COUNT_CACHE**: Determine if obsolete count cache should be enabled in extended cache. Cache memory will be allocated to obsolete count cache after the mapping bitmap if enabled, and the rest of the cache memory is allocated to sector cache.
- **LX_NOR_OBSOLETE_COUNT_CACHE_TYPE**: Defines obsolete count cache element size. If number of sectors per block is greater than 256, use USHORT instead of UCHAR.
- **LX_NOR_SECTOR_SIZE**: Define the logical sector size for NOR flash. The sector size is in units of 32-bit words. This sector size should match the sector size used in file system.
