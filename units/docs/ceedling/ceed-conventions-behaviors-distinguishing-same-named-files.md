---
id: "ceed-conventions-behaviors-distinguishing-same-named-files"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Distinguishing same-named files"
summary: "Ceedling distinguishes files by their full relative path, not just their filename. A project may have, for example, both src/drivers/uart.c and src/sensors/uart.c without one hiding or colliding with the other."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#distinguishing-same-named-files"
license: "MIT"
mode: "V"
---

### Header / source files

Ceedling distinguishes files by their full relative path, not just their
filename. A project may have, for example, both `src/drivers/uart.c` and
`src/sensors/uart.c` without one hiding or colliding with the other.

Distinguishing files is mostly an issue in test builds. If two files share
a name without enough path to distinguish them, Ceedling resolves the reference 
to the first match among the file collection. File collections are ordered per
your project configuration (`:paths`). The ordering of collected files is
identical to the search path ordering provided to the compiler from the same
`:paths` configuration plus any use of
[`TEST_INCLUDE_PATH()`](https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/build-directives.md#test_include_path) directives in
a test file. When Ceedling finds more than one reference, it uses the first
in the ordered file list but logs an informational notice naming multi-file 
matches, so the choice is not silent.

If Ceedling uses the wrong match for lack of path information, your test build 
fails downstream with an ordinary compilation error indirectly revealing the
issue. Add enough path at the point of reference to select the file you actually 
meant.

* Use paths in `#include` directives in your test files to distinguish header 
  files of the same name (mocks are distiguished by the same filepath as the 
  headers from which they are generated). Examples: `#include "foo/bar/file.h"`
  and/or `#include "foo/bar/mock_file.h"`.
* Use the [`TEST_SOURCE_FILE()` build directive macro][build-directive-macros]
  to provide a path to distinguish source files of the same name to be 
  compiled and linked with a test executable.

!!! tip "Mocking two same-named headers in one test file"
    Include each mock through its folder, as in `#include "drivers/uart/mock_config.h"`
    and `#include "drivers/spi/mock_config.h"`. With
    [`:cmock` ↳ `:mock_name_include_folder`](https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/../configuration/reference/cmock.md#mock_name_include_folder),
    enabled by default, each mock is named by that folder, and the two do not collide.

`TEST_SOURCE_FILE()` also takes precedence over the header/source correspondence
convention above. If a test both `#include`s a header and separately names a
same-named source via `TEST_SOURCE_FILE()`, the directive’s own path wins outright
— its source is the one compiled, and the header/source convention does not also
compile whatever it would otherwise have found on its own for that same name. This
holds even when the header’s own `#include` was already unambiguous; a
`TEST_SOURCE_FILE()` entry sharing that basename is always authoritative. (The
header itself is still validated/resolved as usual — only which *source* file gets
compiled for a shared basename is affected.) Like the search-path resolution
above, this override is logged with an informational notice naming the winning
`TEST_SOURCE_FILE()` entry and the `#include` it overrode, so the substitution
is not silent either.

### Test files (CLI test tasks)

Execute [`ceedling test:` tasks][ceedling-test] at the command line with an
optional partial path to distinguish test executables (e.g. `test:foo/bar.c`),
recalling that multiple conventions exist for finding/executing a test
executable via `test:` task.

Unlike the cases above, a same-named test file given at the command line is 
**not** auto-resolved. You must supply enough path yourself in the task
name. Ceedling will complain about colliding task names and provide a list
of matching candidates to help you provide path to disambiguate test files.

[build-directive-macros]: build-directives.md
[ceedling-test]: ../getting-started/command-line.md
[test-source-file-subtractive]: build-directives.md#test_source_file-subtractive-notation
