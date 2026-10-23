---
id: "tbx-experimental-features-trace-component-registers"
type: "concept"
domain: "project"
title: "Experimental Features: Trace Component Registers"
summary: "The following ITM register values are used for ctrace-disable::"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#trace-component-registers"
license: "Apache-2.0"
mode: "V"
---

### ITM

The following ITM register values are used for `ctrace-disable:`:

Name | Offset | `value:` | `mask:`
:----|:-------|:--------|:----
`ITM_TER0` | `0xE00` | `0x00000000` | `None`
`ITM_TPR`  | `0xE40` | `0x00000000` | `None`
`ITM_TCR`  | `0xE80` | `0x00000000` | `None`

### DWT

The following DWT register values are used for `ctrace-disable:`:

Name | Offset | `value:` | `mask:`
:----|:-------|:--------|:----
`DWT_CTRL` | `0x000` | `0x00000000` | `0x007F1FFE`
`DWT_COMP<n>` | `0x020 + <n>*0x010` | `0x00000000` | `None`
`DWT_MASK<n>` (Armv7-M only) | `0x024 + <n>*0x010` | `0x00000000` | `None`
`DWT_FUNCTION<n>` | `0x028 + <n>*0x010` | `0x00000000` | `None`
`DWT_VMASK<n>` (Armv8-M only) | `0x02C + <n>*0x010` | `0x00000000` | `None`

The `DWT_CTRL` disable mask preserves `CYCCNTENA` because application software may use the DWT cycle counter. It also preserves `CYCDISS` on Armv8-M processors with the Security Extension. This bit controls whether the counter increments in Secure state.
