---
id: "tfm-memory-mapped-iovecs-problem-statement"
type: "concept"
domain: "security"
title: "Memory-mapped IOVECs: Problem statement"
summary: "The current MM-IOVEC mechanism is restricted to partitions operating at IL1. This limitation prevents efficient transfer of large payloads for partitions at higher isolation levels."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/mm_iovec.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/mm_iovec.html#problem-statement"
license: "BSD-3-Clause"
mode: "V"
---

The current MM-IOVEC mechanism is restricted to partitions operating at IL1.
This limitation prevents efficient transfer of large payloads for partitions at
higher isolation levels.

The objective is to enable MM-IOVEC support for IL2/IL3 partitions while
preserving isolation guarantees and without affecting security properties.

Reasons to extend support to higher isolation levels are:
 - Process large payloads that do not fit in the client buffers
 - Enable multiple actors to process and forward the 'original' vectors
