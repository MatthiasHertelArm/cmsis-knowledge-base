---
id: "tbx-csolution-project-format-processor-attributes"
type: "concept"
domain: "project"
title: "CSolution Project Format: Processor Attributes"
summary: "The processor: keyword specifies the processor features used in this project."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#processor-attributes"
license: "Apache-2.0"
mode: "V"
---

### `processor:`

The `processor:` keyword specifies the processor features used in this project.

`processor:`                            | Content
:---------------------------------------|:------------------------------------
    `fpu:`               | Select usage of FPU instructions: `dp` (double precision) \| `sp` (single precision) \| `off` (disabled).
    `dsp:`               | Select usage of SIMD instructions: `on` (enabled) \| `off` (disabled).
    `mve:`               | Select usage of M-Profile vector extension: `fp` (floating point and integer instructions) \| `int` (integer instructions) \| `off` (disabled).
    `trustzone:`         | Select TrustZone mode: `secure` \| `secure-only` \| `non-secure` \| `off`.
    `branch-protection:` | Select Branch Protection mode: `bti` (branch target identification) \| `bti-signret` (branch target identification and pointer authentication) \| `off` (disabled).

The default setting enables the available features of the device. For example `fpu: dp` is selected for devices that offer double precision floating point hardware.

For `trustzone:` the possible settings are:

`trustzone:`  | Description
:-------------|:----------------
`off`         | TrustZone disabled, classic Cortex-M programmers model. Default for devices with configurable TrustZone feature.
`non-secure`  | Non-secure mode. Default for devices with enabled TrustZone feature.
`secure`      | Secure mode with veneers for non-secure calls. Related options to generate `cmse` library are enabled.
`secure-only` | Secure mode without veneers for non-secure calls. No `cmse` library generated (new in CMSIS-Toolbox 2.6.0).

**Example:**

```yml
project:
  processor:
    trustzone: secure
    fpu: off             # do not use FPU instructions
    mve: off             # do not use vector instructions.
```
