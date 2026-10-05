---
id: "intr-bazel-build-system-for-embedded-pr-why-bazel"
type: "concept"
domain: "debug"
title: "Bazel Build System for Embedded Projects: Why Bazel?"
summary: "Setting up a build system on a repository is long and fastidious, it’s a step most would want to go through only once. This is one of the many reasons why monolithic repositories (or monorepos) are so popular."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-30-bazel-build-system-for-embedded-projects.md"
doc_source: "https://interrupt.memfault.com/blog/bazel-build-system-for-embedded-projects#why-bazel"
license: "CC-BY-SA-4.0"
mode: "V"
---

Setting up a build system on a repository is long and fastidious, it’s a step most would want to go through only once. This is one of the many reasons why monolithic repositories (or monorepos) are so popular. While it is often a straightforward choice for most software projects, it also comes with several challenges for embedded projects: how to deal with multiple cross-compilation? How multiple toolchains can coexist in the same repository? How to reuse software components between different architectures? etc.

Fortunately, there is a great tool to solve these issues! Bazel is a build system that has multi-platform support at its core, a very powerful concept that I will try to introduce in the next chapter. In addition to what most build systems provide, Bazel also ensures the reproducibility of builds making every build action hermetic from the development environment. It is a multi-language build system that supports many languages out of the box (C, C++, Rust, Python…) and can be extended in Starlark (Bazel scripting language which is very similar to Python). Finally, it is designed to scale, from small to large repositories, making it a perfect candidate for monorepos.
