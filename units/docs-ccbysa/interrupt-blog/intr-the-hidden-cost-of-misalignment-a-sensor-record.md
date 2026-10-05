---
id: "intr-the-hidden-cost-of-misalignment-a-sensor-record"
type: "concept"
domain: "debug"
title: "The Hidden Cost of Misalignment: A Sensor Record"
summary: "Here's a struct you might find in any embedded codebase -- a timestamped sensor reading destined for flash storage or transmission over the wire:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-03-the-hidden-cost-of-misalignment.md"
doc_source: "https://interrupt.memfault.com/blog/the-hidden-cost-of-misalignment#a-sensor-record"
license: "CC-BY-SA-4.0"
mode: "V"
---

Here's a struct you might find in any embedded codebase -- a timestamped sensor
reading destined for flash storage or transmission over the wire:

```c
#pragma pack(push, 1)
typedef struct {
    int64_t  timestamp;       // offset 0,  8 bytes
    int32_t  temperature_mc;  // offset 8,  4 bytes (millidegrees C)
    int32_t  salinity_ppt;    // offset 12, 4 bytes (parts per thousand)
    uint8_t  status_flags;    // offset 16, 1 byte
    uint16_t battery_mv;      // offset 17, 2 bytes
} sensor_reading_t;           // 19 bytes, no padding
#pragma pack(pop)
```

The structure is packed to preserve offsets between platforms (so the same C
code can read it out on a PC, for example), and secondarily to eliminate padding
bytes that would waste space. This is reasonable and very common in embedded
code.

> **Why pack structs at all?** Without packing, the compiler inserts padding
> bytes between fields to satisfy alignment requirements. Historically, the size
> and placement of that padding differed quite a bit across
> architectures[^endianness] -- modern compilers are somewhat more consistent,
> but the padding bytes still waste space and can surprise you when designing a
> wire or storage format. Packing removes this instability: you get a fixed,
> deterministic byte layout regardless of where the code is compiled.

Here's what that looks like. The unpacked version of this struct is 24 bytes --
5 bytes of hidden padding:



But you will see that we labeled most of the entries in the packed structure as
"byte-decomposed", even for fields that are aligned relative to the start of the
struct! This is a hidden performance bomb.
