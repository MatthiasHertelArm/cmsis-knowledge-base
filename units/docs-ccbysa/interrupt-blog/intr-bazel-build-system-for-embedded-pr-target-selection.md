---
id: "intr-bazel-build-system-for-embedded-pr-target-selection"
type: "concept"
domain: "debug"
title: "Bazel Build System for Embedded Projects: Target selection"
summary: "In addition selecting the correct toolchain, a platform can also be used to conditionally select targets during the build. For example, let’s imagine we have a library called my_library that relies on different backends depending on the architecture used."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-30-bazel-build-system-for-embedded-projects.md"
doc_source: "https://interrupt.memfault.com/blog/bazel-build-system-for-embedded-projects#target-selection"
license: "CC-BY-SA-4.0"
mode: "V"
---

In addition selecting the correct toolchain, a platform can also be used to conditionally select targets during the build.
For example, let’s imagine we have a library called `my_library` that relies on different backends depending on the architecture used.

We can do the selection at build time as follow:

```python
cc_library(
    name = “my_library“,
    srcs = ["my_library.cc"],
    deps = select({
        ":arm_build": [":arm_lib"],
        ":x86_build": [":x86_lib"],
        "//conditions:default": [":generic_lib"],
    }),
)
```

The `select` built-in can be used for anything, such as compilation options, defines, dependencies, source files, etc. It lets you deal with variance at build time.
Conditions can also be associative with the use of `selects.with_or` and `selects.config_setting_group` to achieve OR and AND boolean operations.
