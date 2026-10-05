---
id: "ceed-module-generator-stubbing"
type: "concept"
domain: "test"
title: "Module Generator: Stubbing"
summary: "Similarly, you can create stubs for all functions in a header file just by making a single call to your handy stub feature, like this:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/module-generator.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/module-generator/#stubbing"
license: "MIT"
mode: "V"
---

Similarly, you can create stubs for all functions in a header file just by making a single call
to your handy `stub` feature, like this:

```sh
ceedling module:stub[SecretLair]
```

This call will look in `SecretLair.h` and will generate a file `SecretLair.c` that contains a stub
for each function declared in the header! Even better, if `SecretLair.c` already exists, it will
add only new functions, leaving your existing calls alone so that it doesn't cause any problems.
