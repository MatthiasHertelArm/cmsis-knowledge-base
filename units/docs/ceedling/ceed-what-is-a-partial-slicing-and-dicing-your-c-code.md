---
id: "ceed-what-is-a-partial-slicing-and-dicing-your-c-code"
type: "concept"
domain: "test"
title: "What Is a Partial?: Slicing and dicing your C code"
summary: "Ceedling reads your real source and header files, extracts their C contents, and generates new C files that comprise a Partial."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/partials/overview.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/overview/#slicing-and-dicing-your-c-code"
license: "MIT"
mode: "V"
---

Ceedling reads your real source and header files, extracts their C contents,
and generates new C files that comprise a Partial.

Ceedling can create two kinds of Partials:

1. A **_Test Partial_** for exposing otherwise inaccessible functions and 
   variables to your test case assertions.
1. A **_Mock Partial_** for mocking otherwise inaccessible functions in your
   source code.

!!! warning "A function cannot be both tested and mocked in the same test file"
    A core restriction of the C language remains. A partialized function cannot
    be both tested and mocked in the same test. Attempting to do so would duplicate
    the function and cause a doubly-defined symbol failure during linking.
    
    We solve this by simply creating two peer test files for the different Partials
    usage scenarios.

When a test file references a Partial, Ceedling excludes the original source
file from that test executable's build. The generated Partial 
source is compiled and linked in place of the original source C.

!!! note "Purpose-specific C language handling"
    Ceedling includes its own custom, purpose-specific lexing for recognizing
    C language elements. This was the best way to handle all cases across
    platforms. This custom lexer even handles many compiler extensions 
    (e.g. Microsoft's `__declspec` and GCC's `__attribute__()`).
    
    On the upside, this approach provides everything Partials need. On the 
    downside, until exercised by a great deal of real world code, this custom 
    C handling will likely have failings and gaps.
