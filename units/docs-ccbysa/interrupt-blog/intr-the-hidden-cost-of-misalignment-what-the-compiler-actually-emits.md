---
id: "intr-the-hidden-cost-of-misalignment-what-the-compiler-actually-emits"
type: "concept"
domain: "debug"
title: "The Hidden Cost of Misalignment: What the Compiler Actually Emits"
summary: "Look at temperature_mc at offset 8. It's a 4-byte integer sitting at a 4-byte-aligned offset. One would think the compiler would emit a single store instruction for this, but take a look at what actually happens."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-03-the-hidden-cost-of-misalignment.md"
doc_source: "https://interrupt.memfault.com/blog/the-hidden-cost-of-misalignment#what-the-compiler-actually-emits"
license: "CC-BY-SA-4.0"
mode: "V"
---

Look at `temperature_mc` at offset 8. It's a 4-byte integer sitting at a
4-byte-aligned offset. One would think the compiler would emit a single store
instruction for this, but take a look at what actually happens.

Here's the RISC-V disassembly (compiled with `riscv64-elf-gcc` at `-O2`):

```asm
;; entry->temperature_mc = value;
;; value in a1, entry pointer in a0

srli    a3, a1, 0x8       ; extract byte 1
srli    a4, a1, 0x10      ; extract byte 2
srli    a5, a1, 0x18      ; extract byte 3
sb      a1, 8(a0)         ; store byte 0
sb      a3, 9(a0)         ; store byte 1
sb      a4, 10(a0)        ; store byte 2
sb      a5, 11(a0)        ; store byte 3
```

Seven ops! Three shifts and 4 byte-stores -- to write a single `int32_t` to a
perfectly aligned offset. Without `pack(1)`:

```asm
sw      a1, 8(a0)         ; one op
```

Every field in the struct gets this treatment. Writing the 64-bit `timestamp` at
offset 0 is even worse -- 14 ops instead of 2. Not just the misaligned fields.
All of them.

> **Why this happens.** `#pragma pack(1)` sets the _type's_ maximum alignment
> to 1. That means a pointer to this struct could legally point to any byte
> address. The compiler can't look at your code and determine that in practice,
> these structs always live in `malloc`'d memory (aligned), on the stack
> (aligned), or in larger aligned structures. The type system says alignment is
> 1, so every access gets byte-decomposed. This isn't a bug. You told the
> compiler "trust nothing about this struct's alignment." The compiler took you
> at your word.
