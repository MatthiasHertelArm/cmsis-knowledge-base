---
id: "devt-ctrace-ctf-profile-common-sample-fields"
type: "concept"
domain: "trace"
title: "ctrace CTF profile: Common sample fields"
summary: "ITM, DWT value/address/match, PC sample, and profiling records carry sample-quality information:"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/ctf-format.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/ctf-format.md#common-sample-fields"
license: "Apache-2.0"
mode: "V"
---

ITM, DWT value/address/match, PC sample, and profiling records carry sample-quality information:

```text
uint8_t  cmsis_sample_flags
uint32_t cmsis_overflow_count
```

`cmsis_sample_flags` uses these bits:

| Bit | Meaning |
| ---: | --- |
| 0 | An overflow is associated with this sample. |
| 1 | The reconstructed local timestamp is considered reliable. |
| 2 | The sample occurred before the first observed local timestamp. |
| 3–7 | Reserved; written as zero. |

`cmsis_overflow_count` is the cumulative overflow epoch for the Trace Bus ID, saturated at `UINT32_MAX`. Consumers
can use it to partition samples separated by lost trace data. A `TRACE_STATUS` record carries the same epoch counter
but not `cmsis_sample_flags`.

ITM and DWT values use a tagged CTF variant:

| Tag | Variant | CTF scalar |
| ---: | --- | --- |
| 0 | `i8` | signed 8-bit integer |
| 1 | `u8` | unsigned 8-bit integer |
| 2 | `i16` | signed 16-bit integer |
| 3 | `u16` | unsigned 16-bit integer |
| 4 | `i32` | signed 32-bit integer |
| 5 | `u32` | unsigned 32-bit integer |
| 6 | `f32` | IEEE-754 binary32 |

The variant tag immediately precedes the selected value. ITM input uses the unsigned variants. DWT selection comes
from the resolved `data-type` and `size` metadata; supported sizes are 1, 2, and 4 bytes, and `float` requires 4
bytes.

Optional DWT PC and data-address fragments use a separate width tag and variant:

| Tag | Variant | Meaning |
| ---: | --- | --- |
| 0 | `none` | No fragment; the variant value is ignored. |
| 1 | `u8` | Unsigned 8-bit raw fragment. |
| 2 | `u16` | Unsigned 16-bit raw fragment. |
| 4 | `u32` | Unsigned 32-bit raw fragment. |

The exact payload width is preserved; ctrace does not widen every address fragment to 16 or 32 bits.
