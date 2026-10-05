---
id: "vela-vela-performance-estimations-estimated-memory-bandwidth"
type: "concept"
domain: "edge-ai"
title: "Vela Performance Estimations: Estimated memory bandwidth"
summary: "The next section shows the estimated memory bandwidth for each memory type. Data is provided for average, batch and per data type."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:PERFORMANCE.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/PERFORMANCE.md#estimated-memory-bandwidth"
license: "Apache-2.0"
mode: "V"
---

The next section shows the estimated memory bandwidth for each memory type.
Data is provided for average, batch and per data type.

```
Average SRAM bandwidth                           0.04 GB/s
Input   SRAM bandwidth                           0.01 MB/batch
Weight  SRAM bandwidth                           0.00 MB/batch
Output  SRAM bandwidth                           0.00 MB/batch
Total   SRAM bandwidth                           0.01 MB/batch
Total   SRAM bandwidth            per input      0.01 MB/inference (batch size 1)

Average Off-chip Flash bandwidth                 0.46 GB/s
Input   Off-chip Flash bandwidth                 0.01 MB/batch
Weight  Off-chip Flash bandwidth                 0.09 MB/batch
Output  Off-chip Flash bandwidth                 0.00 MB/batch
Total   Off-chip Flash bandwidth                 0.10 MB/batch
Total   Off-chip Flash bandwidth  per input      0.10 MB/inference (batch size 1)
```

### Average bandwidth

This shows the average memory bandwidth usage for the memory type.

### Input bandwidth

This shows the memory bandwidth usage for reading feature maps for the memory
type per batch.

### Weight bandwidth

This shows the memory bandwidth usage for reading and writing weights for the
memory type per batch.

### Output bandwidth

This shows the memory bandwidth usage for writing feature maps for the memory
type per batch.

### Total bandwidth

This shows the total memory bandwidth usage the memory
type per batch and per inference.
