---
id: "txmw-chapter-3-functional-components-of-notes-on-timestamps"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional components of FileX: **FAT12/16/32 Directory Description** / Notes on Timestamps"
summary: "Part of: FAT12/16/32 Directory Description"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter3.md#notes-on-timestamps"
license: "MIT"
mode: "V"
---

_Part of: **FAT12/16/32 Directory Description**_

- **Timestamp Entry**
    The timestamp fields are interpreted as follows:

- **10ms Increment Fields**
    The value in the 10ms increment field provides finer granularity to the timestamp value. The valid values are between 0 (0ms) and 199 (1990ms).

     (figure: 10ms Increment Fields)

- **UTC Offset Field**

     (figure: UTC Offset Field)

- **Offset Value**

    7-bit signed integer represents offset from UTC time, in 15 minutes increments.

- **Valid**

    Whether or not the value in the offset field is valid. 0 indicates the value in the offset value field is invalid. 1 indicates the value is valid.
