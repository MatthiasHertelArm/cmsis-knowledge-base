---
id: "ceed-module-generator-patterns"
type: "concept"
domain: "test"
title: "Module Generator: Patterns"
summary: "A pattern creates a set of related modules at once. Name it after the module:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/module-generator.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/module-generator/#patterns"
license: "MIT"
mode: "V"
---

A pattern creates a set of related modules at once. Name it after the module:

```sh
ceedling "module:create[SecretLair,mch]"
```

This creates nine files: a source, header, and test file each for `SecretLair_Model`,
`SecretLair_Conductor`, and `SecretLair_Hardware`. With `:naming` set to `:bumpy`, the
same call creates `SecretLairModel`, `SecretLairConductor`, and `SecretLairHardware`.
Each generated module includes the headers its role depends on, and each test includes
the mocks of those headers.

The module generator understands the following patterns:

- `src` — a source, header, and test file (the default)
- `test` — only a test file
- `mch` — 9 files for the [model-conductor-hardware (pdf)][mch-paper] pattern ([html][mch-article])
- `mvp` — 9 files for the [model-view-presenter][mvp-wikipedia] pattern
- `dh` — 6 files for the driver-hardware pattern
- `dih` — 9 files for the driver-interrupt-hardware pattern

The `dh` and `dih` patterns are alternate namings and conceptual organizations of the
model-conductor-hardware pattern.

[mch-paper]: https://cdn.prod.website-files.com/628fcc1631ad0b25b32f223e/62e43a26764867e95fe5a138_ESC-413Paper_KarleskyWilliams.pdf
[mch-article]: https://www.methodsandtools.com/archive/archive.php?id=59
[mvp-wikipedia]: https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter

A pattern applies to every module in the call, and a call takes one pattern. The first
argument is always a module name, even one spelled like a pattern.
