---
id: "sds-theory-buffer-size"
type: "concept"
domain: "test"
title: "theory: Buffer Size"
summary: "The size of the data stream buffer depends on several factors such as:"
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/theory.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/theory.md#buffer-size"
license: "Apache-2.0"
mode: "V"
---

The size of the data stream buffer depends on several factors such as:

- the communication interface technology that may impose specific buffer size requirements to maximize data transfer rates.
- the frequency of the algorithm execution. Fast execution speeds may require a larger buffer.

As a guideline, the buffer size should be at least **(2 × block size) + 2 KB**.  
The minimum recommended buffer size is **4 KB**.
