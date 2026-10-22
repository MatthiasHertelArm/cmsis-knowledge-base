---
id: "vela-vela-cli-options-separate-persistent-region"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / Separate persistent region"
summary: "Allocate persistent (variable) tensors in a separate region, region 5, instead of the scratch region. The region is allocated linearly and is never reused for other tensors, so it keeps its contents between inferences."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#separate-persistent-region"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

Allocate persistent (variable) tensors in a separate region, region 5, instead
of the scratch region. The region is allocated linearly and is never reused for
other tensors, so it keeps its contents between inferences. The runtime must
provide a base address for region 5, copy each variable's initial data to its
address once, and keep the region alive across inferences. Requires the raw
output format.

```bash
vela network.tosa --separate-persistent-region --output-format raw
```
