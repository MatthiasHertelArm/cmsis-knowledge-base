---
id: "ceed-json-compilation-database-background"
type: "concept"
domain: "test"
title: "JSON Compilation Database: Background"
summary: "Syntax highlighting and code completion are hard. Historically each editor or IDE has implemented their own and then competed amongst themselves to offer the best experience for developers."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/compile-commands-json-db.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/compile-commands-json-db/#background"
license: "MIT"
mode: "V"
---

Syntax highlighting and code completion are hard. Historically each editor or IDE has implemented their own and then competed amongst themselves to offer the best experience for developers. Good syntax highlighting can be so valuable as to outweigh the consideration of alternate editors. If implementing syntax highlighting and related features in a tool is hard for one language — and it is — imagine doing it for dozens of them. Further, on the flip side, imagine the complexities involved for a developer working with multiple languages at once.

In June of 2016, Microsoft with Red Hat and Codenvy got together to create the [Language Server Protocol (LSP)][lsp-microsoft] ([community site][lsp-community]). The idea was simple. By standardizing, any conforming IDE or editor would only need to support LSP instead of custom plugins for each language. In turn, the backend code that performs syntax highlighting and similar features can be written once and used by any IDE that supports LSP. Today, [Many editors support LSP][lsp-tools].

[lsp-microsoft]: https://microsoft.github.io/language-server-protocol/
[lsp-community]: https://langserver.org/
[lsp-tools]: https://microsoft.github.io/language-server-protocol/implementors/tools/
