---
id: "ceed-extension"
type: "concept"
domain: "test"
title: "`:extension`"
summary: "Ceedling uses path lists and wildcard matching against filename extensions to collect file lists."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/extension.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/extension/"
license: "MIT"
mode: "V"
---

**Filename extensions used to collect lists of files searched in [`:paths`](https://throwtheswitch.github.io/Ceedling/configuration/reference/extension/paths.md)**

Ceedling uses path lists and wildcard matching against filename extensions to collect file lists.

Each file type below accepts either a single extension or a list of extensions. A single
extension is written as a plain string. A list is useful when a project mixes conventions for
a given file type (e.g. source files named with both `.c` and `.C`).

Ceedling searches for and collects files under any extension in the list.
