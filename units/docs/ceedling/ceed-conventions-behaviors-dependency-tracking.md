---
id: "ceed-conventions-behaviors-dependency-tracking"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Dependency tracking"
summary: "Previous versions of Ceedling used features of Rake to offer various kinds of smart rebuilds — that is, only regenerating files, recompiling code files, or relinking executables when changes within the project had occurred since the last build."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#dependency-tracking"
license: "MIT"
mode: "V"
---

Previous versions of Ceedling used features of Rake to offer
various kinds of smart rebuilds — that is, only regenerating files, 
recompiling code files, or relinking executables when changes within 
the project had occurred since the last build. Optional Ceedling 
features discovered “deep dependencies” such that, for example, a 
change in a header file several nested layers deep in `#include` 
statements would cause all the correct test executables to be 
updated and run.

These features have been temporarily disabled and/or removed for 
test suites and remain in limited form for release build while
Ceedling undergoes a major overhaul.

Please see the [Release Notes](https://github.com/ThrowTheSwitch/Ceedling/blob/master/docs/ReleaseNotes.md).

### (Not so) smart rebuilds

* New features that are a part of the Ceedling overhaul can 
  significantly speed up test suite execution and release builds 
  despite the present behavior of brute force running all build 
  steps. See the discussion of enabling multi-threaded builds in 
  later sections.

* When smart rebuilds return, they will further speed up builds as
  will other planned optimizations.
