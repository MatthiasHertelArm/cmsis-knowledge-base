---
id: "intr-improving-compilation-time-of-c-c-first-steps-and-suggestions"
type: "concept"
domain: "debug"
title: "Improving Compilation Time of C/C++ Projects: First Steps and Suggestions"
summary: "These are some up-front suggestions that you should take before trying to speed up the build using the latter, more time-consuming methods. If one of these isn't satisfied, I'd start there."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-11-improving-compilation-times-c-cpp-projects.md"
doc_source: "https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects#first-steps-and-suggestions"
license: "CC-BY-SA-4.0"
mode: "V"
---

These are some up-front suggestions that you should take before trying to speed
up the build using the latter, more time-consuming methods. If one of these
isn't satisfied, I'd start there.

- Don't settle for less than a quad-core CPU & solid-state disk on your
  development machine.
- Don't work on virtual file systems or network drives. Ensure your project is
  on the host's file system.
- Exclude your working directories from your your corporate or built-in
  anti-virus software. I've seen 2-3x slowdowns without the exclusion.
- Use the newest set of compilers and tools that you can reasonably use.
- The build shouldn't require a "clean" before each "build", nor should changing
  one file trigger a rebuild of most of the files in your project.
- Ensure no timestamps are injected into the build which would force rebuilds.
- Try [not to enable link-time optimizations
  (LTO)](https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#-flto)
  as the linking step sometimes becomes as slow as the entire build itself! If
  you have enabled it due to code size constraints, I suggest checking out
  Interrupt's
  [code size posts]() for
  easy wins.
