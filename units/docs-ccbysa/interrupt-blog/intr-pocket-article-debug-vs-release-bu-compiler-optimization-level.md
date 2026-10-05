---
id: "intr-pocket-article-debug-vs-release-bu-compiler-optimization-level"
type: "concept"
domain: "debug"
title: "Pocket article: Debug vs. Release Builds Considered Harmful: Compiler optimization level"
summary: "Setting a lower (or zero) compiler optimization level can help in some step-debugging scenarios. It prevents the compiler from optimizing away variables when they're no longer relevant, or rearranging/combining fragments of code during optimization passes."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-04-25-debug-vs-release-builds.md"
doc_source: "https://interrupt.memfault.com/blog/debug-vs-release-builds#compiler-optimization-level"
license: "CC-BY-SA-4.0"
mode: "V"
---

Setting a lower (or zero) compiler optimization level can help in some
step-debugging scenarios. It prevents the compiler from optimizing away
variables when they're no longer relevant, or rearranging/combining fragments of
code during optimization passes.

Optimization can make step-debugging confusing, but the meaningful information,
such as data structures, variables, and the call stack, is still present.

Anecdotally, I've personally never encountered a roadblock due to compiler
optimization in step-debugging. In the worst case, I need to peek at a few
assembly instructions to see what's going on, but that's very rare.

I've also used the compiler `#pramga GCC optimize ("O0")` or
`__attribute__((optimize("O0")))` to disable optimizations temporarily while
debugging a particular chunk of code or a single file, instead of disabling it
across an entire build.

There's a HUGE downside to having different optimization levels for debug vs.
release builds: we end up with a **different** executable:

- Sizes will likely be different: stack or heap usage (affecting program
  stability!), code space (affecting flash memory allocation, OTA)
- Different machine code executed by the CPU: this can impact **timing** (often
  where the nastiest bugs show up) and actual **program validity**, e.g.
  assumptions you are making about certain spots in your program may no longer
  be valid with different optimization levels (the classic one is instruction
  reordering causing concurrent access bugs!)

Because your debug (testing) build is not running the same code, you may see
these bugs only show up during field test, rather than when the device is on
your desk and connected to a debugger!

It's also generally not desirable to adjust compiler optimization level when a
project is nearing time to ship, to decrease risk. If the debug + release builds
are using the same optimization settings, it's less likely to hit a surprise
out-of-space issue that can stop a project in its tracks 😱.

**Summary: use the same optimization settings for all builds to decrease risk**
