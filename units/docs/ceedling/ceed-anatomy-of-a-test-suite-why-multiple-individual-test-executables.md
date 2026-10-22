---
id: "ceed-anatomy-of-a-test-suite-why-multiple-individual-test-executables"
type: "concept"
domain: "test"
title: "Anatomy of a Test Suite: Why multiple individual test executables in a suite?"
summary: "Anatomy of a Test Suite: Why multiple individual test executables in a suite?"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/test-suite-anatomy.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/test-suite-anatomy/#why-multiple-individual-test-executables-in-a-suite"
license: "MIT"
mode: "V"
---

For several reasons:

* This greatly simplifies the building of your tests.
* C lacks any concept of namespaces or reflection abilities able to segment and 
  distinguish test cases.
* This allows the same release code to be built differently under different
  testing scenarios. Think of how different `#define`s, compiler flags, and
  linked libraries might come in handy for different tests of the same 
  release C code. One source file can be built and tested in different ways
  with multiple test files.
