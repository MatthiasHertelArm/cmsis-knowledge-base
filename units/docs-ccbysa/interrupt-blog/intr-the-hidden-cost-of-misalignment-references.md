---
id: "intr-the-hidden-cost-of-misalignment-references"
type: "concept"
domain: "debug"
title: "The Hidden Cost of Misalignment: References"
summary: "[^endianness]: Endianness is another portability concern when designing binary formats -- see the portability aside in the embedded database post. Here we'll focus on what pack(1) does to your generated code."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-03-the-hidden-cost-of-misalignment.md"
doc_source: "https://interrupt.memfault.com/blog/the-hidden-cost-of-misalignment#references"
license: "CC-BY-SA-4.0"
mode: "V"
---

[^endianness]:
    Endianness is another portability concern when designing binary formats --
    see the [portability
    aside](https://interrupt.memfault.com/blog/choosing-or-building-an-embedded-db#aside-portability-of-records)
    in the embedded database post. Here we'll focus on what `pack(1)` does to
    your generated code.

[^aligned8]:
    On a 32-bit ISA there is no single 64-bit store instruction, so two 32-bit
    stores is already optimal and `aligned(4)` is sufficient. If you target a
    64-bit core (e.g. RV64, AArch64) and want a single `sd` or `str`, use
    `aligned(8)`.

[^stride]:
    A small bonus: array indexing is faster with a 20-byte stride than a 19-byte
    stride. Multiplying by 20 decomposes into simple shifts and adds, while
    multiplying by 19 requires an extra subtraction. The difference is minor but
    it's free.

[^bonus]:
    There's a bonus for misaligned reads, too. With `pack(1)`, reading
    `battery_mv` requires two byte-loads and a reassembly (4 ops). With
    `packed, aligned(4)`, the compiler knows offset 16 is 4-aligned, so it does
    a single word-load from there and shifts out the uint16_t (3 ops). Knowing
    where aligned boundaries are lets the compiler use wider loads even for
    misaligned fields.

- [struct-lint: DWARF-based struct alignment linter](https://github.com/chrismerck/struct-lint)
- [GCC Type Attributes: packed, aligned](https://gcc.gnu.org/onlinedocs/gcc/Common-Type-Attributes.html)
- [ARM Cortex-M0 Technical Reference Manual: Unaligned Access](https://developer.arm.com/documentation/ddi0432/c/programmers-model/unaligned-access-support)
