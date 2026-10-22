---
id: "cmock-cmock-argumentvalidation-pointer-types-in-treat-as"
type: "concept"
domain: "test"
title: "CMock ArgumentValidation: Pointer Types in :treat_as"
summary: "You can map pointer-to-custom-type the same way. Use a  suffix on the right-hand side to indicate the comparison should use the array variant of the assertion:"
status: "draft"
collection: "cmock"
source: "ThrowTheSwitch/CMock@34c26e5:docs/CMock_ArgumentValidation.md"
doc_source: "https://github.com/ThrowTheSwitch/CMock/blob/34c26e5/docs/CMock_ArgumentValidation.md#pointer-types-in-treat-as"
license: "MIT"
mode: "V"
---

You can map pointer-to-custom-type the same way. Use a `*` suffix on
the right-hand side to indicate the comparison should use the array
variant of the assertion:

```yaml
:treat_as:
  MY_DATA_PTR: HEX8*    # compares the bytes pointed to, not the address
```
