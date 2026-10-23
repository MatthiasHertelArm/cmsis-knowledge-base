---
id: "ceed-configuration-reference-compilation-linking"
type: "concept"
domain: "test"
title: "Configuration Reference: Compilation & Linking"
summary: "Add -D symbols to compiler command lines for release builds, all tests, or individual test executables matched by name, substring, or regex."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/#compilation-linking"
license: "MIT"
mode: "V"
---

-   :material-book-open-variant: **[`:defines` — Compilation Symbols][ref-defines]**

    ---

    Add `-D` symbols to compiler command lines for release builds, all tests, or
    individual test executables matched by name, substring, or regex.

-   :material-book-open-variant: **[`:flags` — Compilation & Link Flags][ref-flags]**

    ---

    Add flags to preprocessor, compiler, assembler, and linker command lines for
    release builds, all tests, or individual test executables via matchers.

-   :material-book-open-variant: **[`:libraries` — Libraries][ref-libraries]**

    ---

    Specify test, release, and system libraries to include at link time, with
    configurable flag formats and library search paths.
