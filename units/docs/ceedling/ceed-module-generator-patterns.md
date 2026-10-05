---
id: "ceed-module-generator-patterns"
type: "concept"
domain: "test"
title: "Module Generator: Patterns"
summary: "You can also create an entire pattern of files. To do that, just add a second argument to the pattern ID. Something like this:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/module-generator.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/module-generator/#patterns"
license: "MIT"
mode: "V"
---

You can also create an entire pattern of files. To do that, just add a second argument
to the pattern ID. Something like this:

```sh
ceedling module:create[SecretLair,mch]
```

In this example, we'd create 9 files total: 3 headers, 3 source files, and 3 test files. These
files would be named `SecretLairModel`, `SecretLairConductor`, and `SecretLairHardware`. Isn't
that nice?

The module generator understands the following patterns:

- `src` -- generate only a source file
- `test` -- generate only a test file
- `dh` -- generate 6 files for the driver-hardware pattern
- `dih` -- generate 9 files for the driver-interrupt-hardware pattern
- `mch` -- generate 9 files for the model-conductor-hardware pattern
- `mvp` -- generate 9 files for the model-view-presenter pattern
