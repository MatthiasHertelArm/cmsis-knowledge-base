---
id: "ceed-paths-paths-configuration-options-notes"
type: "concept"
domain: "test"
title: "`:paths`: `:paths` configuration options & notes"
summary: "`:paths`: `:paths` configuration options & notes"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/paths.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/paths/#paths-configuration-options-notes"
license: "MIT"
mode: "V"
---

1. A path can be absolute (fully qualified) or relative.
1. A path can include a glob matcher (more on this below).
1. A path can use [inline Ruby string expansion][inline-ruby-string-expansion].
1. Subtractive paths are possible and useful. See the documentation below.
1. Path order beneath a subsection (e.g. `:paths` ↳ `:include`) is preserved
   when the list is iterated internally or passed to a tool.
