---
id: "ceed-module-generator-stubbing"
type: "concept"
domain: "test"
title: "Module Generator: Stubbing"
summary: "module:stub writes a source file containing a stub for each function its header declares:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/module-generator.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/module-generator/#stubbing"
license: "MIT"
mode: "V"
---

`module:stub` writes a source file containing a stub for each function its header
declares:

```sh
ceedling "module:stub[SecretLair]"
```

This reads `SecretLair.h` from your include path and writes `SecretLair.c` to your
source path. If `SecretLair.c` already exists, only stubs for newly declared functions
are added, and your existing code is left alone.

Hints and slashes work as they do for `module:create`. `"module:stub[lab:rev/SecretLair]"`
reads `rev/SecretLair.h` below the include path `lab:` matches and writes
`rev/SecretLair.c` below the matching source path.

Headers are parsed with your project’s [`:cmock`][cmock] settings, the same ones that generate
your mocks, so options like `:strippables` and `:treat_as` apply to stubs too.
