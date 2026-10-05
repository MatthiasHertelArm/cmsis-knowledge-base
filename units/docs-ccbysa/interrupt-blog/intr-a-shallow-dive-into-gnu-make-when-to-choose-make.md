---
id: "intr-a-shallow-dive-into-gnu-make-when-to-choose-make"
type: "concept"
domain: "debug"
title: "A Shallow Dive into GNU Make: When to choose Make"
summary: "Make is suitable for building small C/C++ projects or libraries that would be included in another project's build system. Most build systems will have a way to integrate Make-based sub-projects."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-03-gnu-make-guidelines.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-make-guidelines#when-to-choose-make"
license: "CC-BY-SA-4.0"
mode: "V"
---

Make is suitable for building small C/C++ projects or libraries that would
be included in another project's build system. Most build systems will have a
way to integrate Make-based sub-projects.

For larger projects, you will find a more modern build system easier to work with.

I would suggest a build system other than Make in the following situations:

- When the number of targets (or files) being built is (or will eventually be) in the hundreds.
- A "configure" step is desired, which sets up and persists variables, target definitions, and environment configurations.
- The project is going to remain internal or private and will not need to be built by end users.
- You find debugging a frustrating exercise.
- You need the build to be cross platform that can build on macOS, Linux, and Windows.

In these situations, you might find using
[CMake](https://cmake.org/), [Bazel](https://bazel.build/),
[Meson](https://mesonbuild.com/), or another modern build system a more pleasurable experience.
