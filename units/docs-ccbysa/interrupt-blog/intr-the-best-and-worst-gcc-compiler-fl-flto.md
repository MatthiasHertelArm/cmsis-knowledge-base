---
id: "intr-the-best-and-worst-gcc-compiler-fl-flto"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: The Worst / -flto"
summary: "LTO (link time optimization), is an optimization pass made across all compilation units, that can help reduce the overall size of a binary."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#flto"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Worst_

LTO (link time optimization), is an optimization pass made across all compilation units, that can
help reduce the overall size of a binary. While at first this sounds great (and I've used it
extensively on several large scale embedded projects), it should be viewed as a **last resort
optimization** if you are desperate to save codespace in an embedded project. Here's why:

- It's slow. If you are trying to do bringup on a new device driver or quickly run some experiments
  on hardware, compilation time becomes critical. Waiting minutes for a build to complete instead
  of seconds can be the difference to debugging an issue in a couple of minutes or a couple of
  hours. Since the LTO pass runs at the link phase, it will _always_ need to run even if only one
  line in one c file changed.
- It's very hard to control memory placement when using LTO. Many embedded projects operate on
  systems with several regions of RAM that have different properties -- some regions are slower to access
  than others, some are non-executable, etc. For example, you may want a graphics library function to
  live in the fastest single-cycle access RAM since it's called all the time but you may not care if the
  graphics stack initialization is in a slow RAM region since it's only called once when the
  system boots. However LTO may decide to inline all of this code into the same function and then place it all in the slower
  region. It is extremely hard to try and prevent LTO from doing this!
- It makes your application substantially harder to debug. This is getting better in newer releases
  but after an LTO pass, a lot of debug information cannot be captured due to the nature of the
  optimization. If a chain of seven functions across several c files is only called once, LTO may
  chose to inline them all together. If you crash somewhere in the seventh function, the backtrace
  may just show one function instead of all seven.
- LTO typically causes large increases to the stack space needed. Since LTO results in aggressive cross-object
  inlining, a bunch of local variables from many different functions now wind up getting allocated
  at the same time. When you enable LTO for the first time, expect to see some stack overflows!
