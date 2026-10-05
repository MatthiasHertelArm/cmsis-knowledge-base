---
id: "intr-better-firmware-with-llvm-clang-background-of-gcc-and-clang"
type: "concept"
domain: "debug"
title: "Better Firmware with LLVM/Clang: Background of GCC and Clang"
summary: "The advent of open source compilers and toolchains traces back over 30 years to 1987 and the release of GCC 1.0. Originally, GCC was meant to compile GNU open source software written in C."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-20-arm-cortexm-with-llvm-clang.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortexm-with-llvm-clang#background-of-gcc-and-clang"
license: "CC-BY-SA-4.0"
mode: "V"
---

The advent of open source compilers and toolchains traces back over 30 years to 1987 and the
release of GCC 1.0. Originally, GCC was meant to compile GNU open source
software written in C. The toolchain grew organically over time to target numerous architectures and support a
variety of different languages. As a consequence, many aspects of the codebase have become complex to extend and work with.

The LLVM project is the "new" open source compiler on the block. It began as a research project at the
University of Illinois at Urbana–Champaign in 2000[^12]. The early goals of the project were to create a
more modular compiler toolchain by designing a collection of standalone libraries. The LLVM project really took root in 2005 when Apple hired one of the original designers, Chris
Lattner, and invested heavily in making LLVM the default used for its own developer ecosystem. This
bore Clang, the C, C++, and objective-C frontend to LLVM and modern day GNU GCC competitor.

Today, the LLVM toolchain has become ubiquitous in the software world and, in recent years, it has seen
adoption in the embedded world as well. Its favorable license in comparison to the GNU
toolchain (Apache 2 vs GPL3) along with its more modular architecture has made the LLVM toolchain a
default choice in the proprietary embedded compiler market. ARM scrapped their original compiler in
favor of an LLVM/Clang based one with the release of ARM Compiler 6 (`armclang`) and, more recently,
SEGGER built an ARM compiler based on the LLVM/Clang toolchain as
well[^11].
