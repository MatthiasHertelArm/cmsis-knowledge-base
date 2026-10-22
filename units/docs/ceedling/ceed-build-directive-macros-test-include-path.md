---
id: "ceed-build-directive-macros-test-include-path"
type: "concept"
domain: "test"
title: "Build Directive Macros: `TEST_INCLUDE_PATH()`"
summary: "The TEST_INCLUDE_PATH() build directive allows a header search path to be injected into the build of an individual test executable."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/build-directives.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/build-directives/#test-include-path"
license: "MIT"
mode: "V"
---

### `TEST_INCLUDE_PATH()` Purpose

The `TEST_INCLUDE_PATH()` build directive allows a header search path to
be injected into the build of an individual test executable.

Unless you have a pretty funky C project, generally at least one search path entry
is necessary for every test executable build. That path can come from a `:paths`  
↳ `:include` entry in your project configuration or by using `TEST_INCLUDE_PATH()` 
in a test file.

Please see [Configuring Your Header File Search Paths](https://throwtheswitch.github.io/Ceedling/testing-guide/build-directives/conventions.md#test-build-search-paths)
for an overview of Ceedling’s options and conventions for header file search paths.

### `TEST_INCLUDE_PATH()` Usage

`TEST_INCLUDE_PATH()` entries in your test file are only an additive customization.
The path will be added to the base / common path list specified by 
`:paths`  ↳ `:include` in the project file. If no list is specified in your project 
configuration, `TEST_INCLUDE_PATH()` entries will comprise the entire header search 
path list.

The argument for the `TEST_INCLUDE_PATH()` build directive macro is a single 
filepath as a string enclosed in quotation marks. Use forward slashes for 
path separators.

**_Note_**: At present, a limitation of the `TEST_INCLUDE_PATH()` build directive 
macro is that paths are relative to the working directory from which you are 
executing `ceedling`. A change to your working directory could require updates to 
the path arguments of dall instances of `TEST_INCLUDE_PATH()`.

Multiple uses of `TEST_INCLUDE_PATH()` are perfectly fine. You'll likely want one 
per line within your test file.

### `TEST_INCLUDE_PATH()` Example

```c
/*
 * Test file test_mycode.c to exercise functions in mycode.c.
 */

#include "unity.h"    // Contains TEST_INCLUDE_PATH() definition
#include "somefile.h" // Needed symbols and macros

// Add the following to the compiler’s -I search paths used to
// compile all components comprising the test_mycode executable.
TEST_INCLUDE_PATH("foo/bar/")
TEST_INCLUDE_PATH("/usr/local/include/baz/")

// --- Unit test framework calls ---

void setUp(void) {
  ...
}

void test_MyCode_FooBar(void) {
  ...
}
```
