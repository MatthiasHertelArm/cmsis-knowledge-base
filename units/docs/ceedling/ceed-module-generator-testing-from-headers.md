---
id: "ceed-module-generator-testing-from-headers"
type: "concept"
domain: "test"
title: "Module Generator: Testing from headers"
summary: "module:test writes a test file containing an ignored test for each function its module’s header declares, a starting point for testing a module that already exists:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/module-generator.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/module-generator/#testing-from-headers"
license: "MIT"
mode: "V"
---

`module:test` writes a test file containing an ignored test for each function its
module’s header declares, a starting point for testing a module that already exists:

```sh
ceedling "module:test[SecretLair]"
```

This reads `SecretLair.h` from your include path and writes `test_SecretLair.c` to your
test path, with a `test_<function>_NeedToImplement` test for each function. Each test
calls `TEST_IGNORE_MESSAGE()` until you fill it in.

Run it again after adding functions to the header, and only tests for the new functions
are added, ahead of the file’s closing `#endif`. A function already counts as tested by
any test named `test_<function>` or `test_<function>_<anything>`, so your own
descriptive test names are respected and your existing tests are left alone.

Hints and slashes work as they do for `module:create`. The test file uses your
configured [includes](#includes), [boilerplate](#boilerplates),
[test define](#test-defines), and [test guard](#test-guards). Headers are parsed with
your project’s [`:cmock`][cmock] settings, as for [stubbing](#stubbing).
