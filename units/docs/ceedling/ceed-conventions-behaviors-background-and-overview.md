---
id: "ceed-conventions-behaviors-background-and-overview"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Test preprocessing / Background and overview"
summary: "Ceedling and CMock are advanced tools that both perform fairly sophisticated parsing."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#background-and-overview"
license: "MIT"
mode: "V"
---

_Part of: Test preprocessing_

Ceedling and CMock are advanced tools that both perform fairly sophisticated
parsing.

However, neither of these tools fully understands the entire C language,
especially C’s preprocessing statements.

Ceedling’s preprocessing features rely on `gcc`’s preprocessing mode to strip 
down / expand test files and headers to their raw code content that can then 
be parsed as text by Ceedling and CMock. These tools must be in your search 
path if Ceedling’s preprocessing is enabled.

See the [`:project` ↳ `:use_test_preprocessor`][project-settings] project 
configuration setting.

!!! warning
    Ceedling’s test preprocessing abilities are directly tied to the features and 
    output of `gcc`. The default tool definitions for these should not be 
    redefined for other toolchains. Future Ceedling improvements will allow for a 
    plugin-style ability to use your own tools in this highly specialized capacity.
