---
id: "ceed-plugins-enabled"
type: "concept"
domain: "test"
title: "`:plugins`: `:enabled`"
summary: "List of plugins to be used — a plugin's name is identical to the subdirectory that contains it."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/plugins.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/plugins/#enabled"
license: "MIT"
mode: "V"
---

List of plugins to be used — a plugin's name is identical to the subdirectory
that contains it.

**Default**: `[]` (empty)

Plugins can provide a variety of added functionality to Ceedling. In general
use, it's assumed that at least one reporting plugin will be used to format
test results (usually `report_tests_pretty_stdout`).

If no reporting plugins are specified, Ceedling will print to `$stdout` the
(quite readable) raw test results from all test fixtures executed.

[custom-plugins]: ../../development/plugins/index.md
[ceedling-plugins]: ../../plugins/index.md
[command-hooks]: ../../plugins/command-hooks.md
