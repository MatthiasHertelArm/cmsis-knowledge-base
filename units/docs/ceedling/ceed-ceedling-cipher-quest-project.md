---
id: "ceed-ceedling-cipher-quest-project"
type: "concept"
domain: "test"
title: "Ceedling Cipher Quest Project"
summary: "A small field-text toolkit for the discerning intelligence agent. Cipher Quest encodes messages, decodes intercepted communications, and analyzes text — but only if you tell it which tools to pack."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/snapshot/examples/cipher_quest/README.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/snapshot/examples/cipher_quest/"
license: "MIT"
mode: "V"
---

A small field-text toolkit for the discerning intelligence agent. Cipher Quest
encodes messages, decodes intercepted communications, and analyzes text — but
only if you tell it which tools to pack.

This example project illustrates:

- **Test builds and release builds of the same project** using Ceedling
- **Per-test-file symbol definitions** via the `:defines` matcher section in
  `project.yml`
- **Conditional compilation** with `#ifdef` to enable/disable feature modules
- **Release build variants** driven by mixins — the project file itself has no
  release symbols; each variant is supplied externally
- **A compile-time `#error`** that prevents building a featureless release binary

This project is limited to string manipulation and relies solely on basic 
assertions for its test suite (i.e. no mocks or Partials).

---
