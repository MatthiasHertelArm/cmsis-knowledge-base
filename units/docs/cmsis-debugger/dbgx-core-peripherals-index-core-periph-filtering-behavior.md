---
id: "dbgx-core-peripherals-index-core-periph-filtering-behavior"
type: "concept"
domain: "debug"
title: "Core Peripherals Index (`core-peripherals-index.yml`): Filtering behavior"
summary: "Core Peripherals Index (`core-peripherals-index.yml`): Filtering behavior"
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:configs/core-peripherals/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/configs/core-peripherals/README.md#filtering-behavior"
license: "Apache-2.0"
mode: "V"
---

### Processor selection

- If the core connection's `pname` matches a child node of `system-resources`>`processors`, then that processor is used.
- If `pname` is missing, then a single-core system is assumed. Hence, the first processor in the list is used.
- If no processors are available, the collector treats the processor as unknown. In this case only entries without `cpu-type`/`cpu-features`
constraints, those using the "*" wildcard, and those using value `none` will match; entries requiring a specific `cpu-type` or specific feature values are excluded.

### `cpu-type` matching

- If omitted or set to the `"*"` wildcard, then entry is valid for all CPU types.
- Otherwise, SCVD files are loaded if the connection's core matches one of the given `core` values.
Matching is case-insensitive.

### `cpu-features` matching

- If omitted, no feature constraints are applied.
- All listed feature conditions must match (`AND` logic).
- Feature must exist in the selected processor object and values must match (case-insensitive).
- Feature value `"*"` matches any value for that key that indicates presence of the feature.
