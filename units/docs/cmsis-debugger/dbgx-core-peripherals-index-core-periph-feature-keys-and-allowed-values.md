---
id: "dbgx-core-peripherals-index-core-periph-feature-keys-and-allowed-values"
type: "concept"
domain: "debug"
title: "Core Peripherals Index (`core-peripherals-index.yml`): Feature keys and allowed values"
summary: "Use feature keys that can appear on a processor entry in system-resources>processors of .cbuild-run.yml."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@28c1601:configs/core-peripherals/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/28c1601/configs/core-peripherals/README.md#feature-keys-and-allowed-values"
license: "Apache-2.0"
mode: "V"
---

Use feature keys that can appear on a processor entry in `system-resources`>`processors` of `*.cbuild-run.yml`.

- `fpu`: `sp`, `dp`, `none`
- `mpu`: `present`, `none`
- `dsp`: `present`, `none`
- `trustzone`: `present`, `none`
- `mve`: `int`, `fp`, `none`
- `pacbti`: `present`, `none`
- `endian`: `little`, `big`, `configurable`

Additional notes for filter behavior:

- `cpu-features` keys are matched exactly by key name (for example `mpu`, not `MPU`).
- Feature value comparison is case-insensitive after converting values to strings.
- If a key is listed in `cpu-features` but missing on the selected processor, the entry only matches if it has the value `none`.
This is to reflect that a missing processor feature usually means it is not implemented.
- Use `"*"` as a feature value to accept any value for that key that indicates presence of the feature.
