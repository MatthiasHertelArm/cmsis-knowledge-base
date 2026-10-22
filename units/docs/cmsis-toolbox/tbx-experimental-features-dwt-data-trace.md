---
id: "tbx-experimental-features-dwt-data-trace"
type: "concept"
domain: "project"
title: "Experimental Features: DWT Feature Variants / DWT Data Trace"
summary: "DWT comparator functions vary between architectures and implementations."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#dwt-data-trace"
license: "Apache-2.0"
mode: "V"
---

_Part of: DWT Feature Variants_

DWT comparator functions vary between architectures and implementations.

- Armv7-M DWT implementations generally require comparator pairing for data-value matching.
- Armv8-M adds linked comparator functions and compact match packets.
- The `match` output mode is Armv8-M-specific.
- The `PC+offset` output mode is Armv8-M-specific.
- Address range support, address masks, access sizes, data-value matching, linked comparators, and emitted packet types must be checked for each comparator through `DWT_FUNCTIONn`.
- Some comparator numbers can support fewer functions than other comparators in the same DWT.

A requested range can require:

- One comparator using an address mask.
- Two linked comparators.
- Multiple comparators when the range is not naturally aligned.

A value match can also require more than one comparator. Comparator allocation therefore depends on the DWT architecture, requested function, alignment, and range. The statement that a size greater than four bytes “may require two comparators” is not sufficient as a complete allocation rule.
