---
id: "txmw-chapter-3-levelx-nand-support-nand-bad-block-support"
type: "concept"
domain: "rtos"
title: "Chapter 3 - LevelX NAND support: NAND Bad Block Support"
summary: "NAND memory is also more likely to have bad blocks than NOR memory. This is largely because NAND manufacturers can increase yield by allowing bad blocks and requiring software to work-around such bad blocks."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter3.md#nand-bad-block-support"
license: "MIT"
mode: "V"
---

NAND memory is also more likely to have bad blocks than NOR memory. This is largely because NAND manufacturers can increase yield by allowing bad blocks and requiring software to work-around such bad blocks. LevelX handles NAND bad block management by simply mapping around bad blocks.

LevelX also provides APIs for 256-byte Hamming Error Correction Codes (ECC) for the underlying LevelX driver to utilize for calculating new ECC codes or to perform 1-bit error correction on page reading within each 256-byte section of the page.
