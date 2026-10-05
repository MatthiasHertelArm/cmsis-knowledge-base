---
id: "intr-bazel-build-system-for-embedded-pr-toolchains"
type: "concept"
domain: "debug"
title: "Bazel Build System for Embedded Projects: Toolchains"
summary: "One of the key features that Bazel solves with platforms is the ability to deal with different toolchains."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-30-bazel-build-system-for-embedded-projects.md"
doc_source: "https://interrupt.memfault.com/blog/bazel-build-system-for-embedded-projects#toolchains"
license: "CC-BY-SA-4.0"
mode: "V"
---

One of the key features that Bazel solves with platforms is the ability to deal with different toolchains.
Out of the box, Bazel will try to figure out which tools are available locally and use them transparently to make it easy to get started.

For example, given the following `BUILD` file:

```python
cc_binary(
    name = "main",
    srcs = ["main.cc"],
)
```

When running, `bazel run //:main`, Bazel will use your locally installed C++ toolchain (gcc for example) and compile and link with gcc using a default recipe. The code above is all you need with Bazel to get started with a C or C++ project.
This is convenient but not when you need a reproducible build or need to cross-compile for example. For such use cases, you will need to use a custom toolchain.
