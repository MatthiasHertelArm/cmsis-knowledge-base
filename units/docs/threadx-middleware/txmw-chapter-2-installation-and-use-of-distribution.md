---
id: "txmw-chapter-2-installation-and-use-of-distribution"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and use of LevelX: Distribution"
summary: "LevelX is distributed in ANSI C where each function is contained in its own separate C file. The files in the LevelX distribution are as follows."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter2.md#distribution"
license: "MIT"
mode: "V"
---

LevelX is distributed in ANSI C where each function is contained in its own separate C file. The files in the LevelX distribution are as follows.
- lx_api.h
- lx_nand_flash_256byte_ecc_check.c
- lx_nand_flash_256byte_ecc_compute.c
- lx_nand_flash_block_allocate.c
- lx_nand_flash_block_data_move.c
- lx_nand_flash_block_find.c
- lx_nand_flash_block_mapping_set.c
- lx_nand_flash_block_status_set.c
- lx_nand_flash_close.c
- lx_nand_flash_data_page_copy.c
- lx_nand_flash_defragment.c
- lx_nand_flash_erase_count_set.c
- lx_nand_flash_extended_cache_enable.c
- lx_nand_flash_format.c
- lx_nand_flash_free_block_list_add.c
- lx_nand_flash_initialize.c
- lx_nand_flash_mapped_block_list_add.c
- lx_nand_flash_mapped_block_list_get.c
- lx_nand_flash_mapped_block_list_remove.c
- lx_nand_flash_memory_initialize.c
- lx_nand_flash_metadata_allocate.c
- lx_nand_flash_metadata_build.c
- lx_nand_flash_metadata_write.c
- lx_nand_flash_open.c
- lx_nand_flash_page_ecc_check.c
- lx_nand_flash_page_ecc_compute.c
- lx_nand_flash_partial_defragment.c
- lx_nand_flash_sectors_read.c
- lx_nand_flash_sectors_release.c
- lx_nand_flash_sectors_write.c
- lx_nand_flash_sector_read.c
- lx_nand_flash_sector_release.c
- lx_nand_flash_sector_write.c
- lx_nand_flash_system_error.c
- lx_nor_flash_block_reclaim.c
- lx_nor_flash_close.c
- lx_nor_flash_defragment.c  
- lx_nor_flash_extended_cache_enable.c
- lx_nor_flash_initialize.c
- lx_nor_flash_logical_sector_find.c
- lx_nor_flash_next_block_to_erase_find.c
- lx_nor_flash_open.c
- lx_nor_flash_partial_defragment.c
- lx_nor_flash_physical_sector_allocate.c
- lx_nor_flash_sector_mapping_cache_invalidate.c
- lx_nor_flash_sector_read.c
- lx_nor_flash_sector_release.c
- lx_nor_flash_sector_write.c
- lx_nor_flash_system_error.c

There are also simulator and FileX driver samples for both LevelX NAND and NOR instances, as follows.

- demo_filex_nand_flash.c  
- fx_nand_flash_simulated_driver.c
- lx_nand_flash_simulator.c
- demo_filex_nor_flash.c  
- fx_nor_flash_simulated_driver.c
- lx_nor_flash_simulator.c

Of course, if only NAND flash is required, only the LevelX NAND flash files (***lx_nand_\*.c***) are needed. Similarly, if only NOR flash is required, only the NOR flash files (***lx_nor_\*.c***) are needed.
