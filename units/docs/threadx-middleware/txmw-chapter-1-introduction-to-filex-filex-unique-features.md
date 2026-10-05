---
id: "txmw-chapter-1-introduction-to-filex-filex-unique-features"
type: "concept"
domain: "rtos"
title: "Chapter 1 - Introduction to FileX: FileX Unique Features"
summary: "FileX supports an unlimited number of media devices at the same time, including RAM disks, FLASH managers, and actual physical devices."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter1.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter1.md#filex-unique-features"
license: "MIT"
mode: "V"
---

FileX supports an unlimited number of media devices at the same time, including RAM disks, FLASH managers, and actual physical devices. It supports 12-, 16-, and 32-bit File Allocation Table (FAT) formats, and also supports contiguous file allocation, and is highly optimized for both size and performance. FileX also includes fault tolerant support, media open/ close, and file write callback functions.

Designed to meet the growing need for FLASH devices, FileX uses the same design and coding methods as ThreadX. Like all Eclipse Foundation products, FileX is distributed with full ANSI C source code, and it has no run-time royalties.

### Product Highlights

- Complete ThreadX processor support
- No royalties
- Complete ANSI C source code
- Real-time performance
- Responsive technical support
- Unlimited FileX objects (media, directories, and files)
- Dynamic FileX object creation/deletion
- Flexible memory usage
- Size scales automatically
- Small footprint (as low as 6 KBytes) instruction area size: 6-30K
- Complete integration with ThreadX
- Endian neutral
- Easy-to-implement FileX I/O drivers
- 12-, 16-, and 32-bit FAT support
- Long filename support
- Internal FAT entry cache
- Unicode name support
- Contiguous file allocation
- Consecutive sector and cluster read/write
- Internal logical sector cache
- RAM disk demonstration runs out-of-the-box
- Media format capability
- Error detection and recovery
- Fault tolerant options
- Built-in performance statistics
- Standalone support (No Eclipse ThreadX)
