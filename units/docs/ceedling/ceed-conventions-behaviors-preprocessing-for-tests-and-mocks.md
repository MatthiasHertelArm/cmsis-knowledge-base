---
id: "ceed-conventions-behaviors-preprocessing-for-tests-and-mocks"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Test preprocessing / Preprocessing for tests and mocks"
summary: "If your test files rely on macros and #ifdef conditionals used in certain ways (see examples below), there’s a chance that Ceedling will break on trying to process your test files, or, alternatively, your test suite will build …"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#preprocessing-for-tests-and-mocks"
license: "MIT"
mode: "V"
---

_Part of: Test preprocessing_

If your test files rely on macros and `#ifdef` conditionals used in certain
ways (see examples below), there’s a chance that Ceedling will break on trying
to process your test files, or, alternatively, your test suite will build but 
not execute as expected.

Similarly, generating mocks of header files with macros and `#ifdef`
conditionals around or in function signatures can get weird. Of course, it’s 
often in sophisticated projects with complex header files that mocking is most 
desired in the first place.

Ceedling includes an optional ability to preprocess the following files before 
then extracting test cases and functions to be mocked with text parsing.

1. Your test files, or
1. Mockable header files, or
1. Both of the above
