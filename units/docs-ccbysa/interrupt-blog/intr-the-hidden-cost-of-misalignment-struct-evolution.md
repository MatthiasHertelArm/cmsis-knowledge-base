---
id: "intr-the-hidden-cost-of-misalignment-struct-evolution"
type: "concept"
domain: "debug"
title: "The Hidden Cost of Misalignment: Struct Evolution"
summary: "Your struct is well-designed. The aligned fields get native access, the misaligned ones are handled correctly. You ship it."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-03-the-hidden-cost-of-misalignment.md"
doc_source: "https://interrupt.memfault.com/blog/the-hidden-cost-of-misalignment#struct-evolution"
license: "CC-BY-SA-4.0"
mode: "V"
---

Your struct is well-designed. The aligned fields get native access, the
misaligned ones are handled correctly. You ship it.

Six months later, someone extends the struct in a pull request. They append a
`uint32_t error_code`:

```c
typedef struct __attribute__((packed, aligned(4))) {
    int64_t  timestamp;
    int32_t  temperature_mc;
    int32_t  salinity_ppt;
    uint8_t  status_flags;
    uint16_t battery_mv;
    uint32_t error_code;      // NEW -- offset 19
} sensor_reading_t;
```

The struct was 19 bytes of content before, so `error_code` lands at offset 19 --
not 4-aligned. No compiler warning. No test failure. The code works fine. But
that field gets the full byte-decomposition treatment:

```asm
;; entry->error_code = code;
srli    a3, a1, 0x8
srli    a4, a1, 0x10
srli    a5, a1, 0x18
sb      a1, 19(a0)
sb      a3, 20(a0)
sb      a4, 21(a0)
sb      a5, 22(a0)
```

Seven ops for what should be one.



> **The bigger risk.** _Inserting_ fields into a packed struct breaks binary
> compatibility with anything already using the old layout -- devices in the
> field, stored records, protocol peers. Appending fields is safe (old readers
> simply ignore the extra bytes), but insertion shifts every subsequent offset.
> I recommend using defense in depth where CI rejects field insertion (by
> comparing struct layouts against a baseline) _and_ integration tests decode
> packets or records from old firmware versions. That's a topic for a future
> post.

The fix for this particular struct would be to insert explicit padding before
`error_code` so it lands at offset 20:

```c
    uint16_t battery_mv;
    uint8_t  _reserved;       // explicit padding to maintain alignment
    uint32_t error_code;      // now at offset 20 -- native access
```

This is easy to miss in code review, whether human or automated. This is why you
lint.

> **Catching misalignment with struct-lint.**
> [struct-lint](https://github.com/chrismerck/struct-lint) reads DWARF debug
> info from ELF binaries and reports fields that aren't naturally aligned within
> packed structs:
>
> ```
> $ struct-lint firmware.elf
>
> sensor_reading_evolved_t.battery_mv (uint16_t, 2 bytes) at offset 17 not naturally aligned (needs 2)
> sensor_reading_evolved_t.error_code (uint32_t, 4 bytes) at offset 19 not naturally aligned (needs 4)
>
> 2 issues in 1 structs across 1 file (2 alignment, 0 missing pack)
> ```
>
> It catches exactly the kind of silent misalignment that happens when structs
> evolve over time. Run it against your build artifacts and you'll know which
> fields are paying the byte-decomposition penalty.
>
> ---
>
> There is also a tool called [pahole](https://linux.die.net/man/1/pahole) which
> can inspect structs based on the DWARF info. Pahole has been around for almost
> 20 years and is even integrated into the Linux kernel build system. Output
> from `pahole` for the same example `sensor_reading_evolved_t` struct is:
>
> ```c
> type`def struct {
>       int64_t                    timestamp;            /*     0     8 */
>       int32_t                    temperature_mc;       /*     8     4 */
>       int32_t                    salinity_ppt;         /*    12     4 */
>       uint8_t                    status_flags;         /*    16     1 */
>       uint16_t                   battery_mv;           /*    17     2 */
>       uint32_t                   error_code;           /*    19     4 */
>
>       /* size: 24, cachelines: 1, members: 6 */
>       /* padding: 1 */
>       /* last cacheline: 24 bytes */
> } sensor_reading_evolved_t __attribute__((__aligned__(4)));>
> ```
>
> where you can see the offsets and sizes of each member of the structure. This
> output may be helpful for debugging and manual inspection of structures.
> `pahole` also offers flags where it can recommend restructuring for
> performance. `struct-lint` on the other hand is intended as a linter for your
> CI pipeline, and to provide feedback on stdout that looks like compiler errors
> so that it's maximally actionable for devs and coding agents.
