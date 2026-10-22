---
id: "ceed-flags"
type: "concept"
domain: "test"
title: "`:flags`"
summary: "Ceedling’s internal, default tool configurations execute compilation and linking of test and source files among a variety of other tooling needs. (See later :tools section.)"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/flags.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/flags/"
license: "MIT"
mode: "V"
---

**Configure preprocessing, compilation, and linking command line flags**

Ceedling’s internal, default tool configurations execute compilation and linking
of test and source files among a variety of other tooling needs. (See later
`:tools` section.)

These default tool configurations are a one-size-fits-all approach. If you need
to add flags to the command line for individual tests or a release build, the
`:flags` section allows you to easily do so.

Entries in `:flags` modify the command lines for tools used at build time.
