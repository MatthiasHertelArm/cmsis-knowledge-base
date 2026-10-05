---
id: "ceed-environment-variables-reference-project-configuration"
type: "concept"
domain: "test"
title: "Environment Variables Reference: Project configuration"
summary: "Points Ceedling at your project configuration file. This is one of several options for specifying the project file location."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/reference/environment-vars.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/environment-vars/#project-configuration"
license: "MIT"
mode: "V"
---

### `CEEDLING_PROJECT_FILE`

Points Ceedling at your project configuration file. This is
[one of several options](https://throwtheswitch.github.io/Ceedling/reference/environment-vars/../configuration/loading.md) for specifying the
project file location.

### `CEEDLING_MIXIN_#`

Environment variables named `CEEDLING_MIXIN_#` — where `#` is any positive
integer — specify filepaths to mixin YAML files to be merged into your base
project configuration. Multiple mixin environment variables are merged in
ascending numeric order (e.g. `CEEDLING_MIXIN_1` before `CEEDLING_MIXIN_5`
before `CEEDLING_MIXIN_99`).

See [_Loading Configuration_](https://throwtheswitch.github.io/Ceedling/reference/environment-vars/../configuration/mixins.md#environment-variables)
for the full details on Mixin environment variables.
