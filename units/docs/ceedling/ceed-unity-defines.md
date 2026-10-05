---
id: "ceed-unity-defines"
type: "concept"
domain: "test"
title: "`:unity`: `:defines`"
summary: "Adds list of symbols used to configure Unity’s features in its source and header files at compile time."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/unity.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/unity/#defines"
license: "MIT"
mode: "V"
---

Adds list of symbols used to configure Unity’s features in its source and
header files at compile time.

See [Using Unity, CMock & CException](https://throwtheswitch.github.io/Ceedling/configuration/reference/unity/../../testing-guide/frameworks.md) for
much more on configuring and making use of these frameworks in your build.

To manage overall command line length, these symbols are only added to
compilation when a Unity C source file is compiled.

!!! note
    No symbols must be set unless Unity’s defaults are inappropriate
    for your environment and needs.

**Default**: `[]` (empty)
