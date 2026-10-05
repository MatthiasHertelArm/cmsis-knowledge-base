---
id: "intr-the-hidden-cost-of-misalignment-the-fix-packed-aligned"
type: "concept"
domain: "debug"
title: "The Hidden Cost of Misalignment: The Fix: `packed` + `aligned`"
summary: "GCC and Clang support combining _attribute_((packed)) with _attribute_((aligned(N))). The packed attribute controls internal layout (no padding between fields), while aligned sets the struct's own alignment requirement:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-03-the-hidden-cost-of-misalignment.md"
doc_source: "https://interrupt.memfault.com/blog/the-hidden-cost-of-misalignment#the-fix-packed-aligned"
license: "CC-BY-SA-4.0"
mode: "V"
---

GCC and Clang support combining `__attribute__((packed))` with
`__attribute__((aligned(N)))`. The `packed` attribute controls internal layout
(no padding between fields), while `aligned` sets the struct's own alignment
requirement:

```c
typedef struct __attribute__((packed, aligned(4))) {
    int64_t  timestamp;       // offset 0  -- native access
    int32_t  temperature_mc;  // offset 8  -- native access
    int32_t  salinity_ppt;    // offset 12 -- native access
    uint8_t  status_flags;    // offset 16 -- byte access either way
    uint16_t battery_mv;      // offset 17 -- still byte-decomposed
} sensor_reading_t;           // 20 bytes (19 content + 1 byte tail padding)
```

The field offsets are identical. The struct gains 1 byte of tail padding (so its
size is a multiple of 4), but the binary layout of the fields themselves doesn't
change. What changes is what the compiler knows: the base pointer is always
4-byte aligned.

That lets the compiler do the math:

- `timestamp` at offset 0: 4-aligned base + 0 = aligned. **Native store (2
  ops).**[^aligned8]
- `temperature_mc` at offset 8: 4-aligned + 8 = aligned. **Native store (1
  op).**
- `salinity_ppt` at offset 12: 4-aligned + 12 = aligned. **Native store.**
- `status_flags` at offset 16: byte access regardless. **No change.**
- `battery_mv` at offset 17: 4-aligned + 17 is odd. **Still byte-decomposed** --
  correctly.



The genuinely misaligned field (`battery_mv` at offset 17) is still handled
safely.[^bonus] But the aligned fields -- which are the majority of this struct
-- go from 7 ops to 1.

> **When you can't switch: arrays of packed structs.** If your packed struct is
> already used in a contiguous array -- in flash, in a file format, over the
> wire -- switching to `packed, aligned(4)` changes the array stride. Elements
> that were at offsets 0, 19, 38, 57... would now be spaced 20 bytes apart. This
> breaks binary compatibility with existing data.
>
> For existing formats with arrays of packed structs, you're stuck with
> `pack(1)` unless you can migrate the data. For _new_ formats, use
> `packed, aligned(4)` from the start.

Here's what that looks like in practice. With `pack(1)`, elements pack tightly
at 19-byte intervals. With `packed, aligned(4)`, each element is padded to 20
bytes[^stride] so the next element starts at a 4-byte-aligned offset:
