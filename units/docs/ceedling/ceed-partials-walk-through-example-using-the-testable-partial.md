---
id: "ceed-partials-walk-through-example-using-the-testable-partial"
type: "concept"
domain: "test"
title: "Partials Walk-Through Example: Using the testable partial"
summary: "Partials Walk-Through Example: Using the testable partial"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/partials/example.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/example/#using-the-testable-partial"
license: "MIT"
mode: "V"
---

```c
// test_sensor_partials_test.c -----------------------------------
#include "unity.h"
#include "ceedling.h" // Required -- defines Partial directive macros
#include "mock_hal.h" // Traditional mocking still available

// Make all functions in the sensor module available for direct testing
#include TEST_PARTIAL_ALL_MODULE(sensor)

// Test the `static` conversion helper internal to source module under test
void test_ConvertRawToMilliCelsius(void)
{
    // `_ConvertRawToMilliCelsius()` is accessible in the Partial 
    // linked in this test executable build
    TEST_ASSERT_EQUAL_INT(-40000, _ConvertRawToMilliCelsius(0));
}
```

### Partials processing step-by-step

1. Reads `sensor.c` and `sensor.h` and extracts all function definitions.
1. `TEST_PARTIAL_ALL_MODULE()` instructs Partial generation to gather and 
   expose all functions from the `sensor` module to be made testable.
1. Generates `ceedling_partial_sensor_impl.c` containing all source functions
   including `_ConvertRawToMilliCelsius()` (stripped of `static` decorator).
1. Compiles and links the Partial implementation source (in place of the original 
   `sensor` source module) and the test file into the test executable. The 
   symbols and includes of `sensor.h` and `sensor.c` are duplicated in the 
   Partials while the original `sensor.c` is omitted from the build.
