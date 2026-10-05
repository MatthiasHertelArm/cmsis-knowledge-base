---
id: "intr-improving-compilation-time-of-c-c-preamble"
type: "concept"
domain: "debug"
title: "Improving Compilation Time of C/C++ Projects: Preamble"
summary: "To set things straight, I don't love build systems. They are complex, unintuitive, and require a deep understanding of each one to do things correctly."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-11-improving-compilation-times-c-cpp-projects.md"
doc_source: "https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects#preamble"
license: "CC-BY-SA-4.0"
mode: "V"
---

To set things straight, I don't love build systems. They are complex,
unintuitive, and require a deep understanding of each one to do things
correctly. The
[GNU Make Manual](https://www.gnu.org/software/make/manual/make.html) is one of
the few manuals I've read cover to cover, and it was one of the best uses of my
time (and my employer's). When you mash together parallel build issues, shelling
out to single-threaded Python scripts, downloading files from remote servers and
package managers, and auto-generating source files, the build infrastructure
could very easy slow down to a crawl if not done properly.

In this post, we will primarily focus on speeding up the compilation side of the
build system by testing out different compilers and compilation strategies.
