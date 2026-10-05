---
id: "ceed-conventions-behaviors-directory-structure-filenames"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Directory structure & filenames"
summary: "Much of Ceedling's functionality is driven by collecting files matching certain patterns inside the paths it's configured to search."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#directory-structure-filenames"
license: "MIT"
mode: "V"
---

Much of Ceedling's functionality is driven by collecting files
matching certain patterns inside the paths it's configured
to search. See the documentation for the `:extension` section
of your configuration file (found in the [configuration reference](https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/../configuration/index.md)) to
configure the file extensions Ceedling uses to match and collect
files. Test file naming is covered later in this section.

Test files and source files must be segregated by directories.
Any directory structure will do. Tests can be held in subdirectories
within source directories, or tests and source directories
can be wholly separated at the top of your project's directory
tree.
