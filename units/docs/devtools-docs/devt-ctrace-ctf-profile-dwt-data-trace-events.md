---
id: "devt-ctrace-ctf-profile-dwt-data-trace-events"
type: "concept"
domain: "trace"
title: "ctrace CTF profile: DWT data-trace events"
summary: "cmsis_dwt_access is read (0) or write (1). DWT comparator labels and data types are resolved from ctrace-run.yml; fallback labels are DWT0 through DWT3."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/ctf-format.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/ctf-format.md#dwt-data-trace-events"
license: "Apache-2.0"
mode: "V"
---

### DWT_VALUE (event ID 1)

```text
cmsis_dwt_comparator_t cmsis_dwt_comparator
cmsis_dwt_access_t     cmsis_dwt_access
value tag and selected value variant
PC width tag and selected cmsis_dwt_pc variant
address width tag and selected cmsis_dwt_address variant
uint8_t                cmsis_sample_flags
uint32_t               cmsis_overflow_count
```

`cmsis_dwt_access` is `read` (`0`) or `write` (`1`). DWT comparator labels and data types are resolved from
`ctrace-run.yml`; fallback labels are `DWT0` through `DWT3`.

The configured value size controls the CTF scalar type. If it differs from the decoded payload size, `ctrace` emits
one warning per affected comparator and route. Trace Compass provides the standard event table and, when such data
was emitted, a generated XY view with one series per comparator.

### DWT_ADDR (event ID 2)

```text
cmsis_dwt_comparator_t cmsis_dwt_comparator
PC width tag and selected cmsis_dwt_pc variant
address width tag and selected cmsis_dwt_address variant
uint8_t                cmsis_sample_flags
uint32_t               cmsis_overflow_count
```

The independent tags state whether a PC fragment, data-address fragment, or both are present and preserve each raw
fragment's exact width. Trace Compass provides the standard event table and, when a data-address fragment was
emitted, a generated address XY view with one series per comparator.

### DWT_MATCH (event ID 9)

```text
cmsis_dwt_comparator_t cmsis_dwt_comparator
uint8_t                cmsis_sample_flags
uint32_t               cmsis_overflow_count
```

The event indicates that an Armv8-M DWT comparator matched without supplying a PC, address, or value. It is a point
event without architectural duration. When such data was emitted, the generated Trace Compass time graph shows a
`Something happened` pulse on the comparator lane for one microsecond; this artificial width is visualization only.
