---
id: "ceed-cexception-defines"
type: "concept"
domain: "test"
title: "`:cexception`: `:defines`"
summary: "List of symbols used to configure CException’s features in its source and header files at compile time."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/cexception.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/cexception/#defines"
license: "MIT"
mode: "V"
---

List of symbols used to configure CException’s features in its source and
header files at compile time.

See [Using Unity, CMock & CException](https://throwtheswitch.github.io/Ceedling/configuration/reference/cexception/../../testing-guide/frameworks.md) for
much more on configuring and making use of these frameworks in your build.

To manage overall command line length, these symbols are only added to
compilation when a CException C source file is compiled.

!!! note
    No symbols must be set unless CException’s defaults are inappropriate for your
    environment and needs.

Note CException must be enabled for it to be added to a release or test build
and for these symbols to be added to a build of CException (see link referenced
earlier for more). Enable it with `:project` ↳ `:use_exceptions`. Ceedling also
enables it automatically when `:cmock` ↳ `:plugins` includes `:cexception`.

**Default**: `[]` (empty)
