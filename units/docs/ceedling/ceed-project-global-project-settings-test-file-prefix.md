---
id: "ceed-project-global-project-settings-test-file-prefix"
type: "concept"
domain: "test"
title: "`:project`: Global project settings: `:test_file_prefix`"
summary: "Ceedling collects test files by convention from within the test file search paths. The convention includes a unique name prefix and a file extension matching that of source files."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/project.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/project/#test-file-prefix"
license: "MIT"
mode: "V"
---

Ceedling collects test files by convention from within the test file search
paths. The convention includes a unique name prefix and a file extension
matching that of source files.

Why not simply recognize all files in test directories as test files? By using
the given convention, we have greater flexibility in what we do with C files in
the test directories.

**Default**: "test_"
