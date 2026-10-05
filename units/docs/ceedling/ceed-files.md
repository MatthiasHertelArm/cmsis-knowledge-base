---
id: "ceed-files"
type: "concept"
domain: "test"
title: "`:files`"
summary: "Ceedling relies on file collections to do its work. These file collections are automagically assembled from paths, matching globs / wildcards, and file extensions. See project configuration :extension."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/files.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/files/"
license: "MIT"
mode: "V"
---

**Tailoring file collections**

Ceedling relies on file collections to do its work. These file collections are
automagically assembled from paths, matching globs / wildcards, and file
extensions. See [project configuration `:extension`](https://throwtheswitch.github.io/Ceedling/configuration/reference/files/extension.md).

Entries in `:files` accomplish filepath-oriented tailoring of the bulk file
collections created from `:paths` directory listings and filename pattern
matching.

On occasion you may need to remove from or add individual files to Ceedling’s
file collections.

The path grammar documented in the `:paths` configuration section largely
applies to `:files` path entries — albeit with regard to filepaths and not
directory paths. The `:files` grammar and YAML examples are documented below.
