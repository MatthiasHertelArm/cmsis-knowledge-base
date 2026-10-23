---
id: "ceed-conventions-behaviors-limitations-gotchas"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Test preprocessing / Limitations & gotchas"
summary: "Ceedling’s preprocessing abilities are generally quite useful — especially in projects with multiple build configurations for different feature sets or multiple targets, legacy code that cannot be refactored, and complex header files provided by vendors."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#limitations-gotchas"
license: "MIT"
mode: "V"
---

_Part of: Test preprocessing_

#### Preprocessing limitations cheatsheet

Ceedling’s preprocessing abilities are generally quite useful — especially in 
projects with multiple build configurations for different feature sets or 
multiple targets, legacy code that cannot be refactored, and complex header 
files provided by vendors.

However, best applying Ceedling’s preprocessing abilities requires understanding 
how the feature works, when to use it, and its limitations.

At a high level, Ceedling’s preprocessing is applicable for cases where macros 
or conditional compilation preprocessing statements (e.g. `#ifdef`):

* Generate or hide/reveal your test files' `#include` statements.
* Generate or hide/reveal your test files' test case function signatures 
  (e.g. `void test_foo()`).
* Generate or hide/reveal mockable header files' `#include` statements.
* Generate or hide/reveal header files' mockable function signatures.

!!! note
    You do not necessarily need to enable Ceedling’s preprocessing only
    because you have preprocessing statements in your test files or mockable
    header files. The feature is only truly needed if your project meets the 
    conditions above.

The sections that follow flesh out the details of the bulleted list above.

#### Preprocessing gotchas

##### `TEST_INCLUDE_PATH()` incompatibe with `#ifdef`

!!! note
    The build directive macro `TEST_INCLUDE_PATH()`, available as of Ceedling 
    1.0.0, is incompatible with enclosing conditional compilation C preprocessing 
    statements.

Wrapping `TEST_INCLUDE_PATH()` in conditional compilation statements 
(e.g. `#ifdef`) will not behave as you expect. This macro is used as a marker
for advanced abilities discovered by Ceedling parsing a test file as plain text.
Whether or not Ceedling preprocessing is enabled, Ceedling will always discover 
this marker macro in the plain text of a test file.

Why is `TEST_INCLUDE_PATH()` incompatible with `#ifdef`? Well, it’s because of
a cyclical dependency that cannot be resolved. In order to perform test 
preprocessing, we need a full complement of `#include` search paths. These 
could be provided, in part, by `TEST_INCLUDE_PATH()`. But, if we allow 
`TEST_INCLUDE_PATH()` to be placed within conditional compilation C 
preprocessing statements, our search paths may be different after test 
preprocessing! The only solution is to disallow this and scan a test file as
plain text looking for this macro at the beginning of a test build.

**_Notes:_**

* `TEST_SOURCE_FILE()` _can_ be placed within conditional compilation
  C preprocessing statements.
* `TEST_INCLUDE_PATH()` & `TEST_SOURCE_FILE()` can be “hidden” from Ceedling’s
  text scanning with traditional C comments.
