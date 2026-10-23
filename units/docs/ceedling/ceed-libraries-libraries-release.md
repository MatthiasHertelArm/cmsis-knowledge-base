---
id: "ceed-libraries-libraries-release"
type: "concept"
domain: "test"
title: "`:libraries`: `:libraries` ↳ `:release`"
summary: "Libraries that should be injected into your release build when linking occurs."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/libraries.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/libraries/#libraries-release"
license: "MIT"
mode: "V"
---

Libraries that should be injected into your release build when linking occurs.

These can be specified as naked library names or with relative paths if search
paths are specified with `:paths` ↳ `:libraries`. Otherwise, absolute paths
may be used here.

These library files **must** exist when the release build occurs **unless** you
are using the [`dependencies`](https://throwtheswitch.github.io/Ceedling/configuration/reference/libraries/../../plugins/dependencies.md) plugin. In that case, the plugin will attempt to
build the needed library for you as a dependency.

**Default**: `[]` (empty)
