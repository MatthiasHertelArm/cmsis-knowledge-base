---
id: "intr-improving-compilation-time-of-c-c-use-a-faster-compiler"
type: "concept"
domain: "debug"
title: "Improving Compilation Time of C/C++ Projects: Steps Towards Faster Builds / Use A Faster Compiler"
summary: "Some compilers are faster than others. The build times of our example project shown below were calculated by taking the average time among 5 builds for each setup."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-11-improving-compilation-times-c-cpp-projects.md"
doc_source: "https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects#use-a-faster-compiler"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Steps Towards Faster Builds_

Some compilers are faster than others. The build times of our example project
shown below were calculated by taking the average time among 5 builds for each
setup.

(figure: comparison of compiler build times)

GCC for macOS, Linux, and Windows performed the best regardless of operating
system, coming in just under 10 seconds. ARM Compiler 6 with Keil then IAR
followed close behind. Keil with ARM Compiler 5 (armcc) was significantly
slower. If you are using ARM Compiler 5, I'd try to upgrade ASAP.
