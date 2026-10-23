---
id: "ceed-conventions-behaviors-source-files-release-artifacts"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Source files & release artifacts"
summary: "Your binary release artifact results from the compilation and linking of all source files Ceedling finds in the specified source directories. At present only source files with a single (configurable) extension are recognized."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#source-files-release-artifacts"
license: "MIT"
mode: "V"
---

Your binary release artifact results from the compilation and
linking of all source files Ceedling finds in the specified source
directories. At present only source files with a single (configurable)
extension are recognized. That is, `*.c` and `*.cc` files will not
both be recognized - only one or the other. See the configuration
options and defaults in the documentation for the `:extension`
sections of your configuration file (found in the [configuration reference](https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/../configuration/index.md)).
