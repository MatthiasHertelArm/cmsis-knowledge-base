---
id: "txmw-chapter-2-module-requirements-module-properties-bit-map"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Module requirements: Module properties bit map"
summary: "The table below shows an example of the properties bit map. Port-specific properties bitmaps are in the appendix."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter2.md#module-properties-bit-map"
license: "MIT"
mode: "V"
---

The table below shows an example of the properties bit map. Port-specific properties bitmaps are in the [appendix](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/appendix.md).

| Bit | Value | Meaning |
|---|---|---|
| 0 | 0
1 | Privileged mode execution
User mode execution |
| 1 | 0
1 | No MPU protection
MPU protection (must have user mode selected) |
| 2 | 0
1 | Disable shared/external memory access
Enable shared/external memory access |
| [23-3] | 0 | Reserved
| [31-24] | 
0x01
0x02
0x03 | **Compiler ID**
IAR
ARM
GNU |
