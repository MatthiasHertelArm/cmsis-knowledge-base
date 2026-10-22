---
id: "ceed-conventions-behaviors-preprocessing-for-include-directives"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Test preprocessing / Preprocessing for include directives"
summary: "In order for Ceedling to do its job, it needs an accurate picture of #include directives used by mockable headers and test files. For simple projects, this can be done with simple text scanning."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#preprocessing-for-include-directives"
license: "MIT"
mode: "V"
---

_Part of: Test preprocessing_

In order for Ceedling to do its job, it needs an accurate picture of `#include`
directives used by mockable headers and test files. For simple projects, this can
be done with simple text scanning.

For projects with conditional compilation (e.g. `#ifdef`) around include 
directives or include directives with macros as targets, preprocessing is required.
Ceedling uses various passes of preprocessor modes to successfully extract
`#include` directives.

A test file’s `#include` directives are extracted with the preprocessor only when
test files are preprocessed, with `:use_test_preprocessor` set to `:tests` or `:all`.
With `:mocks`, only mockable headers are preprocessed, and a test file’s
`#include` directives come from text scanning.
