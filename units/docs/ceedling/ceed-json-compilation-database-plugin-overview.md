---
id: "ceed-json-compilation-database-plugin-overview"
type: "concept"
domain: "test"
title: "JSON Compilation Database: Plugin Overview"
summary: "For C and C++ projects, perhaps the most popular LSP server is the [clangd][clangd] backend."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/compile-commands-json-db.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/compile-commands-json-db/#plugin-overview"
license: "MIT"
mode: "V"
---

For C and C++ projects, perhaps the most popular LSP server is the [`clangd`][clangd] backend. In order to provide features like _go to definition_, `clangd` needs to understand how to build a project so that it can discover all the pieces to the puzzle. Because of the various flavors of builds Ceedling supports and especially because of the complexities of test suite builds, components of a build can easily go missing from the view of `clangd`.

This plugin gives `clangd` — or any tool that understands a [JSON compilation database][json-compilation-database] — full visibility into a Ceedling build.

Once enabled, this plugin generates the database as `<build root>/artifacts/compile_commands.json` for each new build. Tools that understand JSON Compilation Database files can then process it to make their features fully available to you.

[clangd]: https://clangd.llvm.org
[json-compilation-database]: https://clang.llvm.org/docs/JSONCompilationDatabase.html
