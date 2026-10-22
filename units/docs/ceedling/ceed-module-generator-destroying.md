---
id: "ceed-module-generator-destroying"
type: "concept"
domain: "test"
title: "Module Generator: Destroying"
summary: "module:destroy removes the files module:create would make for the same arguments, pattern and hints included:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/module-generator.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/module-generator/#destroying"
license: "MIT"
mode: "V"
---

`module:destroy` removes the files `module:create` would make for the same arguments,
pattern and hints included:

```sh
ceedling "module:destroy[lab:SecretLair,mch]"
```

A file that does not exist is reported and skipped.
