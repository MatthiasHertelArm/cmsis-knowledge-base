---
id: "ceed-build-directive-macros-test-source-file"
type: "concept"
domain: "test"
title: "Build Directive Macros: `TEST_SOURCE_FILE()`"
summary: "The TEST_SOURCE_FILE() build directive allows the simple injection of a specific source file into a test executable’s build."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/build-directives.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/build-directives/#test-source-file"
license: "MIT"
mode: "V"
---

### `TEST_SOURCE_FILE()` Purpose

The `TEST_SOURCE_FILE()` build directive allows the simple injection of 
a specific source file into a test executable’s build.

The Ceedling [convention](https://throwtheswitch.github.io/Ceedling/testing-guide/build-directives/conventions.md) of compiling and linking 
any C file that corresponds in name to an `#include`d header file does 
not always work. A given source file may not have a header file that 
corresponds directly to its name. In some specialized cases, a source 
file may not rely on a header file at all.

Attempting to `#include` a needed C source file directly is both ugly and
can cause various build problems with duplicated symbols, etc.

`TEST_SOURCE_FILE()` is the way to cleanly and simply add a given C file
to the executable built from a test file. `TEST_SOURCE_FILE()` is also one 
of the best methods for adding an assembly file to the build of a given 
test executable—if assembly support is enabled for test builds.

### `TEST_SOURCE_FILE()` Usage

The argument for the `TEST_SOURCE_FILE()` build directive macro is a 
single filename or filepath as a string enclosed in quotation marks. Use
forward slashes for path separators. The filename or filepath must be 
present within Ceedling’s source file collection.

To understand your source file collection:

- See the documentation for project file configuration section 
  [`:paths`](https://throwtheswitch.github.io/Ceedling/testing-guide/build-directives/../configuration/reference/paths.md).
- Dump a listing your project’s source files with the command line task
  `ceedling files:source`.

Multiple uses of `TEST_SOURCE_FILE()` are perfectly fine. You'll likely
want one per line within your test file.

### `TEST_SOURCE_FILE()` & the Header/Source Convention

`TEST_SOURCE_FILE()` takes precedence over Ceedling’s usual convention of
compiling and linking whatever C file corresponds by name to an `#include`d
header. If your test file both `#include`s a header and separately names a
same-named source with `TEST_SOURCE_FILE()`, the directive’s own file is the
one compiled. Ceedling does not also compile whatever the header/source
convention would have found on its own.

Ceedling logs an informational notice naming the winning `TEST_SOURCE_FILE()`
entry and the `#include` it overrode, so the substitution is never silent.

See [Distinguishing same-named files](https://throwtheswitch.github.io/Ceedling/testing-guide/build-directives/conventions.md#header-source-files)
for the full discussion of this and Ceedling’s other file-disambiguation
conventions.

### `TEST_SOURCE_FILE()` Subtractive Notation

A `TEST_SOURCE_FILE()` entry can also be prefixed with `-:` to remove a
named file from a test executable’s compile/link list outright, rather
than add one. This uses the same `+:` / `-:` convention available for
[`:paths` list entries](https://throwtheswitch.github.io/Ceedling/testing-guide/build-directives/../configuration/reference/paths.md#subtractive-entries).

Unlike the override behavior above that only modifies the header/source 
convention for same-named files, a `-:` decorated entry applies to the fully 
assembled list for a test. It removes the named file regardless of how 
that file was added to the list and acts only after every other source 
has already been added to the list.

This is useful whenever Ceedling’s convention of compiling and linking any
`.c` file matching an `#include`d header’s name pulls in a file that
should not be part of a particular test executable. Certain splits of 
headers, source, and arranging of symbols can lead to duplicate symbols
if Ceedling’s convention operates without intervention.

As with the override behavior, Ceedling logs an informational notice
naming the removed file, so a `-:` entry is never silent.

Like in `:paths` entries, a `+:` decorator is assumed. That is omitting any
decorator yields an additive file path. The `+:` decorator is available
solely for formatting or self-documentation purposes.

### `TEST_SOURCE_FILE()` Example

```c
/*
 * Test file test_mycode.c to exercise functions in mycode.c.
 */
 
#include "unity.h"    // Contains TEST_SOURCE_FILE() definition
#include "support.h"  // Needed symbols and macros
//#include "mycode.h" // Header file corresponding to mycode.c by convention does not exist

// Tell Ceedling to compile and link mycode.c as part of the test_mycode executable
TEST_SOURCE_FILE("foo/bar/mycode.c")

// --- Unit test framework calls ---

void setUp(void) {
  ...
}

void test_MyCode_FooBar(void) {
  ...
}
```
