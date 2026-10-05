---
id: "intr-c-structure-padding-initialization-update-2022-05-19"
type: "concept"
domain: "debug"
title: "C Structure Padding Initialization: Update 2022-05-19"
summary: "GCC 12 has added a new flag, -ftrivial-auto-var-init=choice which enables zero-initialization of struct padding by the compiler:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-01-c-struct-padding-initialization.md"
doc_source: "https://interrupt.memfault.com/blog/c-struct-padding-initialization#update-2022-05-19"
license: "CC-BY-SA-4.0"
mode: "V"
---

GCC 12 has added a new flag, `-ftrivial-auto-var-init=choice` which enables
zero-initialization of struct padding by the compiler:

<https://gcc.gnu.org/onlinedocs/gcc-12.2.0/gcc/Optimize-Options.html#index-ftrivial-auto-var-init>

This flag has been present in Clang for a while, but it seems like it may be
removed in the future; it requires setting this somewhat amusingly named flag to
use:

```plaintext
-enable-trivial-auto-var-init-zero-knowing-it-will-be-removed-from-clang
```

The flag is documented
[here](https://releases.llvm.org/14.0.0/tools/clang/docs/ClangCommandLineReference.html#cmdoption-clang-enable-trivial-auto-var-init-zero-knowing-it-will-be-removed-from-clang).

This flag definitely incurs runtime penalties, so it might make sense to enable
it when compiling some sensitive subset of your application (eg a security
library). Definitely an interesting compiler feature!









{:.no_toc}
