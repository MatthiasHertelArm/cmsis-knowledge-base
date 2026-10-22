---
id: "ceed-defines"
type: "concept"
domain: "test"
title: "`:defines`"
summary: "Ceedling’s internal, default compiler tool configurations (see later :tools section) execute compilation of test and source C files."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/defines.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/defines/"
license: "MIT"
mode: "V"
---

**Command line symbols used in compilation**

Ceedling’s internal, default compiler tool configurations (see later `:tools`
section) execute compilation of test and source C files.

These default tool configurations are a one-size-fits-all approach. If you need
to add to the command line symbols for individual tests or a release build, the
`:defines` section allows you to easily do so.

Particularly in testing, symbol definitions in the compilation command line are
often needed:

1. You may wish to control aspects of your test suite. Conditional compilation
   statements can control which test cases execute in which circumstances.
   (Preprocessing must be enabled, `:project` ↳ `:use_test_preprocessor`.)

1. Testing means isolating the source code under test. This can leave certain
   symbols unset when source files are compiled in isolation. Adding symbol
   definitions in your Ceedling project file for such cases is one way to meet
   this need.

Entries in `:defines` modify the command lines for compilers used at build time.
In the default case, symbols listed beneath `:defines` become `-D<symbol>`
arguments.
