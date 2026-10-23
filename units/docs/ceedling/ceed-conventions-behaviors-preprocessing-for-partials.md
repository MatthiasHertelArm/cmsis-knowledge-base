---
id: "ceed-conventions-behaviors-preprocessing-for-partials"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Test preprocessing / Preprocessing for Partials"
summary: "When [Partials][partials] are enabled, Ceedling expands the use of preprocessing beyond only include directives, mockable headers, and test files to partialized source files as well."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#preprocessing-for-partials"
license: "MIT"
mode: "V"
---

_Part of: Test preprocessing_

When [Partials][partials] are enabled, Ceedling expands the use of preprocessing
beyond only include directives, mockable headers, and test files to partialized
source files as well. In order to extract and surgically alter your source code
to become a generated Partial, your source code must be run through various passes
of preprocessig to resolve conditional compilation, expand macros, etc.

!!! note
    The use of Partials automatically enables test preprocessing regardless of 
    your configuration setting and logs the setting update.
