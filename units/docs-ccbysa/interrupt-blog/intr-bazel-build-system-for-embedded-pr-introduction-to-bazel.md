---
id: "intr-bazel-build-system-for-embedded-pr-introduction-to-bazel"
type: "concept"
domain: "debug"
title: "Bazel Build System for Embedded Projects: Introduction to Bazel"
summary: "Before jumping into the subject, let's first cover a short introduction to Bazel."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-30-bazel-build-system-for-embedded-projects.md"
doc_source: "https://interrupt.memfault.com/blog/bazel-build-system-for-embedded-projects#introduction-to-bazel"
license: "CC-BY-SA-4.0"
mode: "V"
---

Before jumping into the subject, let's first cover a short introduction to Bazel.

A Bazel workspace is a directory tree that contains the source files for the software you want to build and it is defined by a `WORKSPACE` file at its root. This file may contain instructions for Bazel to create additional repositories that will be used during the build phase, such as fetching external tools, libraries, etc.

> The concept of workspace is being replaced by [modules](https://bazel.build/external/module). Their function and syntax are very similar, since this is a recent concept and does not add to this article, I will not cover it in this post.

A workspace is a collection of `packages` that are defined by a `BUILD` file. These files contain declarations of build `rules` that are uniquely identified through their relative path to the root and a unique name within this file. This is called the `target name`. Each of these rules defines build `actions`, for example, a `cc_binary` rule defines actions such as compilation and linking.

When Bazel is invoked, it will operate in 3 distinct phases, it will first load all `BUILD` files, then analyze all the rules and their dependencies to create an `action graph` and finally execute all the actions until the final outputs are produced.

The behavior and configuration of Bazel can be changed through command line arguments (also called flags). A file named `.bazelrc` can be used at the root of the workspace to collect all flags that should be added when invoking Bazel.
