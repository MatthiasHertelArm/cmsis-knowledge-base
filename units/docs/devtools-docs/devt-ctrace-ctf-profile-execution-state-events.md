---
id: "devt-ctrace-ctf-profile-execution-state-events"
type: "concept"
domain: "trace"
title: "ctrace CTF profile: Execution-state events"
summary: "The action is entered (0), exited (1), or returned (2). cmsis_exception_number provides the generated architectural label, while cmsis_exception_number_value preserves the numeric value for generic consumers."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/ctf-format.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/ctf-format.md#execution-state-events"
license: "Apache-2.0"
mode: "V"
---

### EXCEPTION (event ID 4)

```text
cmsis_exception_number_t cmsis_exception_number
cmsis_exception_action_t cmsis_exception_action
uint16_t                 cmsis_exception_number_value
cmsis_exception_origin_t cmsis_exception_origin
```

The action is `entered` (`0`), `exited` (`1`), or `returned` (`2`). `cmsis_exception_number` provides the generated
architectural label, while `cmsis_exception_number_value` preserves the numeric value for generic consumers.

`cmsis_exception_origin` distinguishes a decoded trace transition (`trace`, `0`) from a record synthesized by ctrace
(`synthetic`, `1`). Synthetic records close the previously active context and establish mutually exclusive timeline
lanes; they do not claim that another exception packet existed in the raw trace.

If at least one decoded exception transition was emitted, the generated Trace Compass time graph orders Thread Mode
first, Exception Return second, and the observed exceptions below them. Synthetic bootstrap records alone do not
create the view. Overflow and data loss close the active context and leave a gap until a later trace transition
establishes the state again.

### PC_SAMPLE (event ID 6)

```text
uint8_t  cmsis_pc_sample_state
uint32_t cmsis_pc[cmsis_pc_sample_state]
uint8_t  cmsis_sample_flags
uint32_t cmsis_overflow_count
```

State `0` denotes processor sleep and leaves the PC array empty. State `1` denotes a periodic PC sample and stores one
32-bit PC. The state therefore doubles as the zero-or-one array length.

Four-byte PC values and one-byte `0x00` sleep indications use this event. The Armv8-M one-byte `0xff`
trace-prohibited marker uses [`PC_SAMPLE_PROHIBITED`](#pc_sample_prohibited-event-id-10); other payloads produce
a decoder Error.

PC samples are point observations and are available in the CTF event table. Trace Compass does not invent execution
duration between sampled PCs. If a sleep indication was emitted, the generated `Processor State` view opens a
`Sleep` interval; the next PC sample, trace-prohibited marker, overflow, or data loss closes it. Ordinary PC samples
alone do not create this view.

### PC_SAMPLE_PROHIBITED (event ID 10)

```text
uint8_t  cmsis_sample_flags
uint32_t cmsis_overflow_count
```

The Armv8-M one-byte DWT PC-sampling payload `0xff` reports `Trace prohibited`. It is a valid point observation,
not a PC address, decoder error, or data-loss boundary. Its timestamp and sample quality are preserved; the marker
does not increment the overflow count or reset exception state.

This additive event keeps the existing `PC_SAMPLE` binary layout and profile version unchanged. Adding another
`cmsis_pc_sample_state` value instead would change the PC array length and misalign consumers. Both event kinds remain
part of the `pcsample` output selection.

The event is visible in the CTF event table. If a `Processor State` view exists, it closes any open `Sleep` interval
for that route, leaving the state unknown. It neither establishes running state nor creates a trace-prohibited
duration or a graphical view by itself.
