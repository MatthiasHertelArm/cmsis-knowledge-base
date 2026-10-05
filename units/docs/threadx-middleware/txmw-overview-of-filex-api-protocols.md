---
id: "txmw-overview-of-filex-api-protocols"
type: "concept"
domain: "rtos"
title: "Overview of FileX: API protocols"
summary: "Overview of FileX: API protocols"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/overview-filex.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/overview-filex.md#api-protocols"
license: "MIT"
mode: "V"
---

### Media Services

- FAT 12/16/32 support
- Minimal 6KB FLASH, 2.5KB RAM
- Complete media access services
- Unlimited number of media instance
- Simple read/write logical sector driver interface
- Multiple partition support
- Logical sector cache
- FAT entry cache
- Optional fault tolerance support
- Deferred Secondary FAT update
- System-level Trace via TraceX
- Intuitive media access APIs, including:
  - fx_media_open
  - fx_media_close
  - fx_media_format
  - fx_media_space_available

### Directory Services

- Up to 256 byte paths
- Long and 8.3 directory names supported
- Directory create & delete
- Directory navigation and traversal
- Directory attributes management
- System-level Trace via TraceX
- Intuitive directory access APIs, including:
  - fx_directory_create
  - fx_directory_delete
  - fx_directory_attributes_set
  - fx_directory_attributes_read
  - fx_directory_first_entry_find
  - fx_directory_next_entry_find

### File Services

- Minimal 3.3KB FLASH
- Unlimited open files
- Read-only files can be opened multiple times
- Long and 8.3 directory names supported
- Contiguous file support
- Fast seek logic
- Pre-allocation of clusters
- File create, delete, and rename
- File read, write, and see
- File attributes management
- System-level Trace via TraceX
- Intuitive file access APIs, including:
  - fx_file_create
  - fx_file_delete
  - fx_file_attributes_set
  - fx_file_attributes_read
  - fx_file_read
  - fx_file_seek
  - fx_file_write
