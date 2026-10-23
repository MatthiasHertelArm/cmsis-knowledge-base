---
id: "ceed-configuration-reference-files-paths-extensions"
type: "concept"
domain: "test"
title: "Configuration Reference: Files, Paths & Extensions"
summary: "Directory path lists for source, tests, headers, support files, and libraries. Supports globs, subtractive entries, and inline Ruby string expansion."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/#files-paths-extensions"
license: "MIT"
mode: "V"
---

-   :material-book-open-variant: **[`:paths` — Search Paths][ref-paths]**

    ---

    Directory path lists for source, tests, headers, support files, and libraries.
    Supports globs, subtractive entries, and inline Ruby string expansion.

-   :material-book-open-variant: **[`:files` — File Collections][ref-files]**

    ---

    Fine-grained tailoring of the file collections assembled from `:paths` —
    add or subtract individual files with globs and subtractive entries.

-   :material-book-open-variant: **[`:extension` — File Extensions][ref-extension]**

    ---

    Override the default filename extensions for source, header, object, assembly,
    executable, and other file types.
