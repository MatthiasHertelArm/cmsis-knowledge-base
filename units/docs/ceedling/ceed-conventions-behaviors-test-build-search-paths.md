---
id: "ceed-conventions-behaviors-test-build-search-paths"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Test build search paths"
summary: "Test builds in C are fairly complex. Each test file becomes a test executable. Each test executable needs generated runner code and optionally generated mocks."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#test-build-search-paths"
license: "MIT"
mode: "V"
---

Test builds in C are fairly complex. Each test file becomes a test
executable. Each test executable needs generated runner code and 
optionally generated mocks. Slicing and dicing what files are 
compiled and linked and how search paths are assembled is tricky
business. That’s why Ceedling exists in the first place. Because
of these issues, search paths, in particular, require quite a bit
of special handling.

Unless your project is relying exclusively on `extern` statements and
uses no mocks for testing, Ceedling _**must**_ be told where to find 
header files. Without search path knowledge, mocks cannot be generated, 
and test file compilation will fail for lack of symbol definitions
and function declarations.

Ceedling provides two mechanisms for configuring search paths:

1. The [`:paths` ↳ `:include`](https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/../configuration/reference/paths.md) section within your 
   project file (or mixin files).
1. The [`TEST_INCLUDE_PATH(...)`](https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/build-directives.md#test_include_path) build directive 
   macro. This is only available within test files.

In testing contexts, you have three options for assembling the core of 
the search path list used by Ceedling for test builds:

1. List all search paths within the `:paths` ↳ `:include` subsection 
   of your project file. This is the simplest and most common approach.
1. Create the search paths for each test file using calls to the 
  `TEST_INCLUDE_PATH(...)` build directive macro within each test file.
1. Blending the preceding options. In this approach the subsection
   within your project file acts as a common, base list of search 
   paths while the build directive macro allows the list to be 
   expanded upon for each test file. This method is especially helpful 
   for large and/or complex projects in trimming down 
   problematically long compiler command lines.

As for the complete search path list for test builds created by Ceedling,
it is assembled from a variety of sources. In order:

1. Mock generation build path (if mocking is enabled)
1. Paths provided via `TEST_INCLUDE_PATH(...)` build directive macro
1. Any paths within `:paths` ↳ `:test` list containing header files
1. `:paths` ↳ `:support` list from your project configuration
1. `:paths` ↳ `:include` list from your project configuration
1. `:paths` ↳ `:libraries` list from your project configuration
1. Internal path for Unity’s unit test framework C code
1. Internal paths for CMock’s C code (if respective feature enabled)
1. `:paths` ↳ `:test_toolchain_include` list from your project 
   configuration

The paths lists above are documented in detail in the discussion of 
project configuration.

_**Notes:**_

* The order of your `:paths` entries directly translates to the ordering
  of search paths.
* The logic of the ordering above is essentially that:
    * Everything above (5) should have precedence to allow test-specific 
     symbols, function signatures, etc. to be found before that of your 
     source code under test. This is the necessary pattern for effective 
     testing and test builds.
    * Everything below (5) is supporting symbols and function signatures
     for your source code. Your source code should be processed before
     these for effective builds generally.
* (3) is a balancing act. It is entirely possible that test developers
  will choose to create common files of symbols and supporting code 
  necessary for unit tests and choose to organize it alongside their 
  test files. A test build must be able to find these references. At the
  same time it is highly unlikely every test directory path in a project
  is necessary for a test build — particularly in large and sophisticated
  projects. To reduce overall search path length and problematic command
  lines, this convention tailors the search path. This is low risk
  tailoring but could cause gotchas in edge cases or when Ceedling is 
  combined with other tools. Any other such tailoring is avoided as it
  could too easily cause maddening build problems.
* Remember that the ordering of search paths is impacted by the merge 
  order of any Mixins. Paths specified with Mixins will be added to 
  path lists in your project configuration in the order of merging.
