---
id: "ceed-project-configuration-reference"
type: "concept"
domain: "test"
title: "Project Configuration Reference"
summary: "Ceedling's project configuration is assembled from one or more sources and merged into a single in-memory data structure before any build begins. The base configuration comes from a YAML project file."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/reference/project-configuration.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/project-configuration/"
license: "MIT"
mode: "V"
---

Ceedling's project configuration is assembled from one or more sources and
merged into a single in-memory data structure before any build begins. The
base configuration comes from a YAML project file. That base can be extended
by [Mixins](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/mixins.md) — additional YAML files
merged in after the base is loaded. Mixins can be specified from the command
line, via environment variables, or from within the project file using the
`:mixins:` section listed below.

For the full details on how loading and merging work — including the search
order for the default project file and all Mixin sources — see
[Loading Configuration](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/loading.md). For the environment
variables that influence configuration loading, see
[Environment Variables](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/environment-vars.md).

For conceptual overview and project file conventions, see
[Configuration](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/index.md).
