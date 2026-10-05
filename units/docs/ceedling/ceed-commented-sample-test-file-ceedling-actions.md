---
id: "ceed-commented-sample-test-file-ceedling-actions"
type: "concept"
domain: "test"
title: "Commented Sample Test File: Ceedling actions"
summary: "From the test file specified above Ceedling will generate test_foo_runner.c. This runner file will contain main() and will call both of the example test case functions."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/test-sample.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/test-sample/#ceedling-actions"
license: "MIT"
mode: "V"
---

From the test file specified above Ceedling will generate 
`test_foo_runner.c`. This runner file will contain `main()` and will call 
both of the example test case functions.

The final test executable will be `test_foo.exe` (Windows) or `test_foo.out` 
for Unix-based systems (extensions are configurable). Based on the `#include` 
list and test directive macro above, the test executable will be the output 
of the linker having processed `unity.o`, `foo.o`, `mock_bar.o`, `mock_baz.o`, 
`more.o`, `test_foo.o`, and `test_foo_runner.o`. 

Ceedling finds the needed code files, generates mocks, generates a runner, 
compiles all the code files, and links everything into the test executable. 
Ceedling will then run the test executable and collect test results from it 
to be reported to the developer at the command line.
