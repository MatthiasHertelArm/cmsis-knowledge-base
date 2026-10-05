---
id: "ceed-files-files-options-notes"
type: "concept"
domain: "test"
title: "`:files`: `:files` options & notes"
summary: "`:files`: `:files` options & notes"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/files.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/files/#files-options-notes"
license: "MIT"
mode: "V"
---

1. A path can be absolute (fully qualified) or relative.
1. A path can include a glob matcher (more on this below).
1. A path can use [inline Ruby string expansion][inline-ruby-string-expansion].
1. Subtractive paths prepended with a `-:` decorator are possible and useful.
   See the documentation below.
