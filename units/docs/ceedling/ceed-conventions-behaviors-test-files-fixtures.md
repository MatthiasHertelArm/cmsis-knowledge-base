---
id: "ceed-conventions-behaviors-test-files-fixtures"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Test files & fixtures"
summary: "Ceedling builds each individual test file with its accompanying source file(s) into a single, monolithic test fixture executable."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#test-files-fixtures"
license: "MIT"
mode: "V"
---

Ceedling builds each individual test file with its accompanying
source file(s) into a single, monolithic test fixture executable.

### Test file naming

Ceedling recognizes test files by a naming convention — a (configurable)
prefix such as "`test_`" at the beginning of the file name with the same 
file extension as used by your C source files. See the configuration options
and defaults in the documentation for the `:project` and `:extension`
sections of your configuration file (found in the [configuration reference](https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/../configuration/index.md)).

Depending on your configuration options, Ceedling can recognize
a variety of test file naming patterns in your test search paths.
For example, `test_some_super_functionality.c`, `TestYourSourceFile.cc`,
or `testing_MyAwesomeCode.C` could each be valid test file
names. Note, however, that Ceedling can recognize only one test
file naming convention per project.

### Source & mock files to compile and link

Ceedling knows what files to compile and link into each individual
test executable by way of the `#include` list contained in each
test file and optional test directive macros.

The `#include` list directs Ceedling in two ways:

1. Any C source files in the configured project directories
   corresponding to `#include`d header files will be compiled and 
   linked into the resulting test fixture executable.
1. If you are using mocks, header files with the appropriate 
   mocking prefix (e.g. `mock_foo.h`) direct Ceedling to find the
   source header file (e.g. `foo.h`), generate a mock from it, and
   compile & link that generated code into into the test executable 
   as well.

Sometimes the source file you need to add to your test executable has
no corresponding header file — e.g. `file_abc.h` contains symbols 
present in `file_xyz.c`. In these cases, you can use the test 
directive macro `TEST_SOURCE_FILE(...)` to tell Ceedling to compile 
and link the desired source file into the test executable (see 
[macro documentation](https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/build-directives.md)).

That was a lot of information and many clauses in a very few 
sentences; the commented example test file code that follows in a 
bit will make it clearer.

### Test case functions & runner generation

By naming your test functions according to convention, Ceedling
will extract and collect into a generated test runner C file the 
appropriate calls to all your test case functions. This runner 
file handles all the execution minutiae so that your test file 
can be quite simple. As a bonus, you'll never forget to wire up 
a test function to be executed.

In this generated runner lives the `main()` entry point for the 
resulting test executable. There are no configurable options for 
the naming convention of your test case functions.

A test case function signature must have these elements:

1. `void` return
1. `void` parameter list
1. A function name prepended with lowercase "`test`".

In other words, a test function signature should look like this: 
`void test<any_name_you_like>(void)`.
