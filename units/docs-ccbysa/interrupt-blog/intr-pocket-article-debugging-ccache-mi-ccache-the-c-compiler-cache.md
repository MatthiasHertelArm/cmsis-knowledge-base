---
id: "intr-pocket-article-debugging-ccache-mi-ccache-the-c-compiler-cache"
type: "concept"
domain: "debug"
title: "Pocket article: Debugging ccache misses: ccache: The C Compiler Cache"
summary: "We've written about the excellent ccache tool on Interrupt before:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-10-04-ccache-debugging.md"
doc_source: "https://interrupt.memfault.com/blog/ccache-debugging#ccache-the-c-compiler-cache"
license: "CC-BY-SA-4.0"
mode: "V"
---

We've written about the excellent `ccache` tool on Interrupt before:

["Improving Compilation Time of C/C++ Projects"](https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects)

`ccache` provides a wrapper around C/C++ compiler calls that _caches_ the output
object file, so that future calls with unmodified source files will just copy
the output file from the cache instead of wasting computation time recompiling
for the same result.

Getting the most out of `ccache` has a lot of overlap with Reproducible Builds,
which we've also covered on Interrupt:

[Reproducible Firmware Builds](https://interrupt.memfault.com/blog/reproducible-firmware-builds)

Using `ccache` can improve compilations times _dramatically_; often a 25x
speedup or faster, depending on the project. Keeping `ccache` working well can
also have a big impact on snappy CI builds, which improves developer quality of
life!

Let's dive right in.
