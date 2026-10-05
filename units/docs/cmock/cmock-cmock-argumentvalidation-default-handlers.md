---
id: "cmock-cmock-argumentvalidation-default-handlers"
type: "concept"
domain: "test"
title: "CMock ArgumentValidation: Default Handlers"
summary: "CMock ships with a built-in :treat_as list that already covers the most common type aliases found in embedded C codebases. You get all of these for free without any configuration:"
status: "draft"
collection: "cmock"
source: "ThrowTheSwitch/CMock@f2a70b4:docs/CMock_ArgumentValidation.md"
doc_source: "https://github.com/ThrowTheSwitch/CMock/blob/f2a70b4/docs/CMock_ArgumentValidation.md#default-handlers"
license: "MIT"
mode: "V"
---

CMock ships with a built-in `:treat_as` list that already covers the
most common type aliases found in embedded C codebases. You get all
of these for free without any configuration:

| C Type              | Unity Assertion Used      |
|---------------------|---------------------------|
| `int`               | `INT`                     |
| `char`              | `INT8`                    |
| `short`             | `INT16`                   |
| `long`              | `INT`                     |
| `unsigned int`      | `HEX32`                   |
| `unsigned long`     | `HEX32`                   |
| `unsigned short`    | `HEX16`                   |
| `unsigned char`     | `HEX8`                    |
| `int8_t` / `INT8_T` / `int8` | `INT8`         |
| `int16_t` / `INT16_T` / `int16` | `INT16`     |
| `int32_t` / `INT32_T` / `int32` | `INT`       |
| `uint8_t` / `UINT8_T` / `uint8` / `UINT8` | `HEX8` |
| `uint16_t` / `UINT16_T` / `uint16` / `UINT16` | `HEX16` |
| `uint32_t` / `UINT32_T` / `uint32` / `UINT32` | `HEX32` |
| `bool` / `bool_t` / `BOOL` / `BOOL_T` | `INT`  |
| `char*`             | `STRING`                  |
| `pCHAR` / `cstring` / `CSTRING` | `STRING`   |
| `void*`             | `HEX8_ARRAY`              |
| `float` / `double`  | `FLOAT`                   |

The right-hand side of each mapping is the suffix of the Unity assertion
that will be used. `HEX8` means CMock will call `TEST_ASSERT_EQUAL_HEX8`,
for instance. Pointer variants (ending in `*`) map to the corresponding
array assertion (e.g. `HEX8*` → `TEST_ASSERT_EQUAL_HEX8_ARRAY`).
