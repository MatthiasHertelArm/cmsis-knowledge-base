---
id: "ceed-defines-defines-options"
type: "concept"
domain: "test"
title: "`:defines`: `:defines` options"
summary: "If enabled, add a symbol to test compilation derived from the test file name. The resulting symbol is a sanitized, uppercase, ASCII version of the test file name. Any non ASCII characters (e.g."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/defines.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/defines/#defines-options"
license: "MIT"
mode: "V"
---

* `:use_test_definition`:

  If enabled, add a symbol to test compilation derived from the test file name.
  The resulting symbol is a sanitized, uppercase, ASCII version of the test file
  name. Any non ASCII characters (e.g. Unicode) are replaced by underscores as
  are any non-alphanumeric characters. Underscores and dashes are preserved. The
  symbol name is wrapped in underscores unless they already exist in the leading
  and trailing positions. Example: _test_123abc-xyz😵.c_ ➡️ `_TEST_123ABC-XYZ_`.

  **Default**: False
