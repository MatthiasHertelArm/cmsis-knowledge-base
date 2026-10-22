---
id: "ceed-cmock-includes"
type: "concept"
domain: "test"
title: "`:cmock`: `:includes`"
summary: "In certain advanced testing scenarios, you may need to inject additional header files into generated mocks. The filenames in this list will be transformed into #include directives created at the top of every generated mock."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/cmock.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/cmock/#includes"
license: "MIT"
mode: "V"
---

In certain advanced testing scenarios, you may need to inject additional header
files into generated mocks. The filenames in this list will be transformed into
`#include` directives created at the top of every generated mock.

If `:unity_helper_path` is in use (see preceding), the filenames at the end of
any Unity helper file paths will be automatically injected into this list
provided to CMock.

**Default**: `[]` (empty)
