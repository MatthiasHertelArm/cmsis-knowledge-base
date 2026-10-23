---
id: "ceed-fake-function-framework-for-ceedli-helper-macros"
type: "concept"
domain: "test"
title: "Fake Function Framework for Ceedling: Helper macros"
summary: "For convenience, there are also some helper macros that create new Unity-style asserts:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/fff.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/fff/#helper-macros"
license: "MIT"
mode: "V"
---

For convenience, there are also some helper macros that create new Unity-style asserts:

- `TEST_ASSERT_CALLED(function)`: Asserts that a function was called once.
- `TEST_ASSERT_NOT_CALLED(function)`: Asserts that a function was never called.
- `TEST_ASSERT_CALLED_TIMES(times, function)`: Asserts that a function was called a particular number of times.
- `TEST_ASSERT_CALLED_IN_ORDER(order, function)`: Asserts that a function was called in a particular order.

Here's how you might use one of these instead of simply checking the call_count value:

```c
void
test_whenTheDeviceIsReset_thenTheStatusLedIsTurnedOff()
{
    // When
    event_deviceReset();

    // Then
    // This how to directly use fff...
    TEST_ASSERT_EQUAL(1, display_turnOffStatusLed_fake.call_count);
    // ...and this is how to use the helper macro.
    TEST_ASSERT_CALLED(display_turnOffStatusLed);
}
```
