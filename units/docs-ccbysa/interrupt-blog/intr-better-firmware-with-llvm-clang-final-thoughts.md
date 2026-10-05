---
id: "intr-better-firmware-with-llvm-clang-final-thoughts"
type: "concept"
domain: "debug"
title: "Better Firmware with LLVM/Clang: Final Thoughts"
summary: "I first experimented with Clang for Cortex-M in 2013 and at the time the backend for code-size optimization for ARM just didn't compete with other compilers like GCC."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-20-arm-cortexm-with-llvm-clang.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortexm-with-llvm-clang#final-thoughts"
license: "CC-BY-SA-4.0"
mode: "V"
---

I first experimented with Clang for Cortex-M in 2013 and at the time the backend for code-size
optimization for ARM just didn't compete with other compilers like GCC. These days it seems like
things are getting pretty close, and I'm quite impressed at how the toolchain has progressed overall.

I hope this post gave you a useful overview of how to cross-compile your embedded ARM project with
LLVM/Clang and some of the neat things you can do once you have that working.

I'd love to hear if you already using LLVM/Clang in your embedded project today and if so, whether
it is for static analysis or for generating actual binaries. Either way, let us know in the discussion area below!



{:.no_toc}
