---
id: "ceed-accessing-static-variables-file-scoped-static-variables"
type: "concept"
domain: "test"
title: "Accessing Static Variables: File-Scoped Static Variables"
summary: "A file-scoped static variable is declared at the top level of a .c file with the static keyword."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/partials/variables.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/variables/#file-scoped-static-variables"
license: "MIT"
mode: "V"
---

A file-scoped `static` variable is declared at the top level of a `.c` file
with the `static` keyword. Like a `static` function, it has _internal linkage_ 
-- the linker cannot see it outside the translation unit in which it is defined.
This means test code in a separate translation unit cannot read or write it,
making it impossible to inspect state or reset it between test cases without
modifying the production source.

When Ceedling generates a Partial it automatically copies every file-scoped 
`static` variable found in the source module into the Partial and strips the 
`static` keyword. The resulting definition in the generated `_impl.c` file 
has external linkage. A matching `extern` declaration is emitted in the 
generated `_impl.h` header. Including any `TEST_PARTIAL_*_MODULE` macro brings 
that `extern` declaration into scope, causing the variable to accessible in 
test code directly by its **original name** — no renaming or helper macro is 
required.

### Partial file-scoped static variable example

Extending the sensor module with a file-scoped error counter:

```c
// sensor.c -----------------------------------------------
// File-scoped; invisible outside sensor.c
static uint32_t g_error_count = 0;

int Sensor_ReadCelsius(void)
{
    uint16_t raw = HAL_SensorRead();
    // Sentinel value signals hardware error
    if (raw == 0xFFFF) {
        g_error_count++;
        return -1;
    }
    return _ConvertRawToMilliCelsius(raw) / 1000;
}
```

Ceedling strips `static` when generating the test Partial:

```c
// ceedling_partial_sensor_impl.c (generated) ---------------
// `static` stripped -- now has external linkage
uint32_t g_error_count = 0;
// ...
int Sensor_ReadCelsius(void)
{
    uint16_t raw = HAL_SensorRead();
    if (raw == 0xFFFF) {
        g_error_count++;
        return -1;
    }
    return _ConvertRawToMilliCelsius(raw) / 1000;
}
```

```c
// ceedling_partial_sensor_impl.h (generated) ---------------
// `extern` declaration -- immediately available in test code
extern uint32_t g_error_count;
// ...
```

Because `#include TEST_PARTIAL_*_MODULE()` automatically causes the generated
Partial header file to be included in your test, the `extern`ed variable is
immediately available to you in your test.

In the test file, the variable is accessed directly by its original name:

```c
// test_sensor_partial.c -----------------------------------
#include "unity.h"
#include "ceedling.h"
#include "mock_hal.h"

// Brings `extern g_error_count` into scope
#include TEST_PARTIAL_ALL_MODULE(sensor)

void setUp(void) {
    // Reset to known state before each test
    g_error_count = 0;
}

void test_ReadCelsius_counts_hardware_errors(void)
{
    // Simulate hardware error
    HAL_SensorRead_ExpectAndReturn(0xFFFF);
    TEST_ASSERT_EQUAL_INT(-1, Sensor_ReadCelsius());
    // Access the previously inaccessible `g_error_count`
    TEST_ASSERT_EQUAL_UINT32(1, g_error_count);
}
```
