---
id: "intr-the-hidden-cost-of-misalignment-not-just-risc-v"
type: "concept"
domain: "debug"
title: "The Hidden Cost of Misalignment: Not Just RISC-V"
summary: "The examples above are RISC-V, but this affects all embedded architectures. Here's the same 32-bit write (temperature_mc at offset 8) across seven targets:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-03-the-hidden-cost-of-misalignment.md"
doc_source: "https://interrupt.memfault.com/blog/the-hidden-cost-of-misalignment#not-just-risc-v"
license: "CC-BY-SA-4.0"
mode: "V"
---

The examples above are RISC-V, but this affects all embedded architectures.
Here's the same 32-bit write (`temperature_mc` at offset 8) across seven
targets:

| Architecture             | `pack(1)`                            | `packed, aligned(4)` | Ratio |
| ------------------------ | ------------------------------------ | -------------------- | ----- |
| **RISC-V 32** (rv32imac) | 7 ops (3 `srli` + 4 `sb`)            | 1 op (`sw`)          | 7x    |
| **Xtensa** (ESP32)       | 7 ops (3 `extui` + 4 `s8i`)          | 1 op (`s32i.n`)      | 7x    |
| **ARM Cortex-M0**        | 7 ops (2 `lsrs` + `lsls` + 4 `strb`) | 1 op (`str`)         | 7x    |
| **MIPS32**               | 2 ops (`swl` + `swr`)                | 1 op (`sw`)          | 2x    |
| **macOS arm64**          | 1 op (`str`)                         | 1 op (`str`)         | 1x    |
| **i686**                 | 1 op (`movl`)                        | 1 op (`movl`)        | 1x    |
| **x86_64**               | 1 op (`movl`)                        | 1 op (`movl`)        | 1x    |

Most embedded targets we tested show the same 7× byte-decomposition overhead --
different ISAs, different compilers, same pattern. The exception is MIPS32,
which has dedicated unaligned store instructions (`swl` / `swr`) that reduce the
overhead to 2×.

Desktop architectures (arm64, x86) produce identical code regardless of packing.
They handle unaligned access in hardware and may pay a microarchitectural
penalty (cache line split, extra cycles) -- but thankfully on embedded targets
we can just inspect the disassembly to know exactly what we're paying.
