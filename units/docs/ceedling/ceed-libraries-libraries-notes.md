---
id: "ceed-libraries-libraries-notes"
type: "concept"
domain: "test"
title: "`:libraries`: `:libraries` notes"
summary: "`:libraries`: `:libraries` notes"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/libraries.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/libraries/#libraries-notes"
license: "MIT"
mode: "V"
---

* If you've specified your own link step, you are going to want to add `${4}` to
  your argument list in the position where library files should be added to the
  command line. For `gcc`, this is often at the very end. Other tools may vary.
  See the `:tools` section for more.
