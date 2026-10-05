---
id: "spec-debug-description-caching-of-dp-and-ap-registers"
type: "concept"
domain: "pack"
title: "Debug Description: Writing debug access sequences / Caching of DP and AP registers"
summary: "Part of: Writing debug access sequences"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html"
license: "Apache-2.0"
mode: "V"
---

_Part of: Writing debug access sequences_

The debug access functions access target memory or directly access DP and AP registers using
`ReadAP,` `WriteAP,` `ReadAccessAP,` `WriteAccessAP,` `ReadDP,` `WriteDP,` and `DAP_WriteABORT.`

To accelerate target memory accesses, a host debugger may cache DP and AP registers such as the AP CSW and DP SELECT.
If a debugger implements such caching, the direct register access functions listed above must behave as follows:

- A direct register read must always access the target register rather than return a cached value. The debugger must update
  the corresponding register cache with the latest value read from the target.
- A direct register write must always access the target register and update the corresponding register cache with the written
  value. This is particularly important for write-only registers such as DP SELECT.
