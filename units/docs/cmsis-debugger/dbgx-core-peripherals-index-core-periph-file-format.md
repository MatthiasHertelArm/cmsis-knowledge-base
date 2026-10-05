---
id: "dbgx-core-peripherals-index-core-periph-file-format"
type: "concept"
domain: "debug"
title: "Core Peripherals Index (`core-peripherals-index.yml`): File format"
summary: "Core Peripherals Index (`core-peripherals-index.yml`): File format"
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@28c1601:configs/core-peripherals/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/28c1601/configs/core-peripherals/README.md#file-format"
license: "Apache-2.0"
mode: "V"
---

```yaml
core-peripherals:
  - file: Nested_Vectored_Interrupt_Controller_M33_with_TZ.scvd
    cpu-type: Cortex-M33
    cpu-features:
      trustzone: present
    info: Example for a CPU specific NVIC description.

  - file: My_M55_M85_CorePeripheral.scvd
    cpu-type:
      - Cortex-M55
      - Cortex-M85
    cpu-features:
      mve: fp
      dsp: present
      fpu: dp
    info: Example for a core peripheral description valid for multiple CPU types with available CPU features.

  - file: Memory_Protection_Unit.scvd
    cpu-type: "*"
    cpu-features:
      mpu: present
      fpu: "*"
    info: Example for wildcard usage
```

- `file` (required): Path to an SCVD file, relative to this folder (`configs/core-peripherals`).
- `cpu-type` (optional): String or list of strings matching processor `core` from `system-resources`>`processors` in `*.cbuild-run.yml`.
- `cpu-features` (optional): Key/value map matched against processor properties.
- `info` (optional): Free-text description.
