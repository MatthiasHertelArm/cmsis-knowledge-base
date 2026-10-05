---
id: "vela-vela-performance-estimations-weights-data"
type: "concept"
domain: "edge-ai"
title: "Vela Performance Estimations: Weights data"
summary: "This section is only visible if the CLI option --verbose-weights is provided."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:PERFORMANCE.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/PERFORMANCE.md#weights-data"
license: "Apache-2.0"
mode: "V"
---

This section is only visible if the CLI option `--verbose-weights` is provided.
```
Original Weights Size                           84.91 KiB
NPU Encoded Weights Size                        89.30 KiB
```

### Original Weights Size

This is the total size of all weights in the network before optimization.

### NPU Weights Size

This is the total size of the weights rearranged and padded to fit the NPUs
block based processing.

### NPU Encoded Weights Size

This is the total size of the [NPU Weights](#NPU-Weights-Size) after being
encoded for the NPU.
