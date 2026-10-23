---
id: "ceed-json-compilation-database-configuration"
type: "concept"
domain: "test"
title: "JSON Compilation Database: Configuration"
summary: "There is no additional configuration necessary to run this plugin."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/compile-commands-json-db.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/compile-commands-json-db/#configuration"
license: "MIT"
mode: "V"
---

There is no additional configuration necessary to run this plugin.

`clangd` will search your build directory for the JSON compilation database, but in some instances on Unix-based platforms it can be easier and necessary to symlink the file into the root directory of your project (e.g. `ln -s ./build/artifacts/compile_commands.json .`).
