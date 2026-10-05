---
id: "intr-a-shallow-dive-into-gnu-make-outro"
type: "concept"
domain: "debug"
title: "A Shallow Dive into GNU Make: Outro"
summary: "I hope this article has provided a few useful pointers around GNU Make!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-03-gnu-make-guidelines.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-make-guidelines#outro"
license: "CC-BY-SA-4.0"
mode: "V"
---

I hope this article has provided a few useful pointers around GNU Make!

Make remains common in C language projects, most likely due to its usage in the
Linux kernel. Many recently developed statically compiled programming
languages, such as Rust or Go, provide their own build infrastructure. However, when
integrating Make-based software into those languages, for example when building
a C library to be called from Rust, it can be surprisingly helpful to understand
some Make concepts!

You may also encounter [automake](https://www.gnu.org/software/automake/) in
open source projects (look for a `./configure` script). This is a related tool
that generates Makefiles, and is worth a look (especially if you are writing
C software that needs to be very widely portable).

There are many competitors to GNU Make available today, I encourage everyone to
look into them. Some examples:

- [CMake](https://cmake.org/) is pretty popular (the Zephyr project uses this)
  and worth a look. It makes out-of-tree builds pretty easy
- [Bazel](https://docs.bazel.build/versions/master/tutorial/cpp.html) uses a
  declarative syntax (vs. Make's imperative approach)
- [Meson](https://mesonbuild.com/) is a meta-builder like `cmake`, but by
  default uses Ninja as the backend, and can be very fast
