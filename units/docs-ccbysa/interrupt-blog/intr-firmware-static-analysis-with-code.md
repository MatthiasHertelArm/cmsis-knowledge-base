---
id: "intr-firmware-static-analysis-with-code"
type: "concept"
domain: "debug"
title: "Firmware Static Analysis with CodeChecker"
summary: "The pitfalls of C programming are well known: undefined behavior abounds, uninitialized variables lie in wait, memory leaks, and buffers overflow."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-05-19-static-analysis-with-codechecker.md"
doc_source: "https://interrupt.memfault.com/blog/static-analysis-with-codechecker"
license: "CC-BY-SA-4.0"
mode: "V"
---

The pitfalls of C programming are well known: undefined behavior abounds,
uninitialized variables lie in wait, memory leaks, and buffers overflow.

While we wait for the utopia of memory-safe languages, our best bet is to rely
on tools to catch some of the more egregious errors in our code for us.
Compiler warnings are a great place to start, but today I want to take it one
step further and talk about static analysis.

Static analysis is simply the analysis of a piece of software while it is not
executing. Some static analyzers are very simple, while other rely on symbolic
execution to trace through code paths and find potential problems.

Many of you will be familiar with proprietary tools like Coverity or Klocwork
for static analysis. Or perhaps you had to run Fortify to fulfill a requirement
from your employer’s security team. However, an open source alternative has
emerged recently: CodeChecker.

Codechecker[^codechecker_gh] is built on top of the excellent clang static
analyzer, an open source tool with support for cross-translation-unit analysis
and an impressive number of checkers. Adding CodeChecker to your product is
easy, and is a quick way to catch a wide array of bugs in your code before they
reach your customers.

 In this post, I go over how to set up CodeChecker on a
firmware project to reap the benefits of static analysis. I’ll also cover ways
to deal with false positives, and configure your assert functions to be
analysis-friendly.
