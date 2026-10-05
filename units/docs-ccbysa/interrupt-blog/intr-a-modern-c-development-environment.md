---
id: "intr-a-modern-c-development-environment"
type: "concept"
domain: "debug"
title: "A Modern C Development Environment"
summary: "Sometimes, C/C++ projects have a long development cycle. When working on such a project, it can be easy to take our development environment for granted, and forget about the effort invested in its bring-up."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-09-a-modern-c-dev-env.md"
doc_source: "https://interrupt.memfault.com/blog/a-modern-c-dev-env"
license: "CC-BY-SA-4.0"
mode: "V"
---

Sometimes, `C/C++` projects have a long development cycle. When working on such a project, it can be easy to take our development environment for granted, and forget about the effort invested in its bring-up. The build environment works like *magic*, the test framework is neatly integrated, and the CI/CD pipeline relieves us of tedious, repetitive tasks.

For me, all it took was a simple thought: How do I best develop a `C` library, consisting of only a handful of files, but developed out of the context of my current, comfortable development environment? And there I was, back in the cold reality of `C/C++`, where you have the freedom - or obligation - to choose the entire development environment yourself.


In this article we'll go over how to set up a containerized development environment for C projects. We'll touch on setting up a build system using CMake, a testing environment using Unity, and even how to use our containerized environment in our CI pipeline!


Maybe this little writeup helps the next person that is feeling a little overwhelmed when trying to start a new `C/C++` project from scratch, with their hands frozen over the keyboard, thinking about all those things that need to be done before even starting to write a single line of code...
