---
id: "ceed-plugins-load-paths"
type: "concept"
domain: "test"
title: "`:plugins`: `:load_paths`"
summary: "Base paths to search for plugin subdirectories or extra Ruby functionality."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/plugins.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/plugins/#load-paths"
license: "MIT"
mode: "V"
---

Base paths to search for plugin subdirectories or extra Ruby functionality.

Ceedling maintains the Ruby load path for its built-in plugins. This list of
paths allows you to add your own directories for custom plugins or simpler
Ruby files referenced by your Ceedling configuration options elsewhere.

**Default**: `[]` (empty)
