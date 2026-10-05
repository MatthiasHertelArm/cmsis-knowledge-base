---
id: "x-cmsis-debug-live-3"
type: "concept"
domain: "debug"
title: "When the variable and the peripheral disagree"
status: "draft"
extracted_from: "proc-cmsis-debug-live"
source: "cmsis-debug-live/SKILL.md"
---

**Read the address directly.** `read_memory` on the register address tells you what the bus sees. A mismatch against the C variable means the write never landed — wrong alias, missing `volatile`, or a peripheral clock that is off.
**Check the clock first.** A peripheral whose clock gate is closed reads back zeros or retains defaults and silently ignores writes. This is the single most common "the peripheral is broken" cause.
**Watch for caches and write buffers** on M7 and larger parts: what the core wrote may not be what DMA reads.
