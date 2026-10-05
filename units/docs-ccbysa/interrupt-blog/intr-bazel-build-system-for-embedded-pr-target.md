---
id: "intr-bazel-build-system-for-embedded-pr-target"
type: "concept"
domain: "debug"
title: "Bazel Build System for Embedded Projects: Target"
summary: "Finally, when building all targets in the repository with a specific target platform, the incompatible ones will be skipped."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-30-bazel-build-system-for-embedded-projects.md"
doc_source: "https://interrupt.memfault.com/blog/bazel-build-system-for-embedded-projects#target"
license: "CC-BY-SA-4.0"
mode: "V"
---

Finally, when building all targets in the repository with a specific target platform, the incompatible ones will be skipped.

Compatibility or incompatibility of a target is described with the `target_compatible_with` attribute of any rule. Note that this attribute propagates from its dependencies as well. In other words, if a target depends on a Windows library for example, and the latter is described with the appropriate `target_compatible_with` values, then if built on for a Linux platform, this all its parent target(s) will be skipped (not built).

Here is for example how this could look like:

```python
cc_library(
    name = "windows_lib",
    srcs = ["windows_lib.cc"],
    target_compatible_with = [
        "@platforms//os:windows",
    ],
)
```

> Note that targets will be skipped only if all targets are requested to be built, using `bazel build //...` or `bazel test //...` for example. If a specific target is built and is incompatible, the build will fail.

This is very useful when one wants to test all targets that are compatible with a specific platform either locally after a change or in CI for example.
