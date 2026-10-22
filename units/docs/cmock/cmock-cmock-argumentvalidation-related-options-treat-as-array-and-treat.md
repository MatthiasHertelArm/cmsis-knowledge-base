---
id: "cmock-cmock-argumentvalidation-related-options-treat-as-array-and-treat"
type: "concept"
domain: "test"
title: "CMock ArgumentValidation: Related Options: :treat_as_array and :treat_as_void"
summary: "Two narrower variants of :treat_as handle specific edge cases:"
status: "draft"
collection: "cmock"
source: "ThrowTheSwitch/CMock@34c26e5:docs/CMock_ArgumentValidation.md"
doc_source: "https://github.com/ThrowTheSwitch/CMock/blob/34c26e5/docs/CMock_ArgumentValidation.md#related-options-treat-as-array-and-treat-as-void"
license: "MIT"
mode: "V"
---

Two narrower variants of `:treat_as` handle specific edge cases:

**`:treat_as_array`** — for types that are themselves `typedef`'d arrays,
such as `typedef int TenIntegers[10];`. This is a hash of typedef name
to element type:

```yaml
:cmock:
  :treat_as_array:
    TenIntegers: int
    MyBuffer:    uint8_t
```

This lets CMock treat parameters of these types the same way it would
treat a pointer-plus-count, enabling features like `ExpectWithArray`
and `ReturnArrayThruPtr`.

**`:treat_as_void`** — for legacy codebases that typedef `void` to a
custom name (e.g. `typedef void MY_VOID;`). Add such names here so
CMock knows functions returning or accepting that type are effectively
`void`:

```yaml
:cmock:
  :treat_as_void:
    - MY_VOID
    - NORETURN_T
```

Option 3: Custom Assertions for Custom Types
--------------------------------------------

CMock has the ability to use custom assertions, if you form them 
according to certain specifications. Creating a custom assertion 
can be a bit of work, But the reward is that, once you've done so,
you can use those assertions within your own tests AND CMock will
magically use them within its own mocks.

To accomplish this, we're going tackle multiple steps:

  1. Write a custom assertion function
  2. Wrap it in a `UNITY_TEST_` macro
  3. Wrap it in a `TEST_` macro
  4. Inform CMock that it exists

Let's look at each of those steps in detail:
