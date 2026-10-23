---
id: "ceed-partials-walk-through-example-using-the-mockable-partial"
type: "concept"
domain: "test"
title: "Partials Walk-Through Example: Using the mockable partial"
summary: "Partials Walk-Through Example: Using the mockable partial"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/partials/example.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/example/#using-the-mockable-partial"
license: "MIT"
mode: "V"
---

```c
// test_sensor_partials_mocks.c -----------------------------------
#include "unity.h"
#include "ceedling.h" // Required -- defines Partial directive macros
#include "mock_hal.h" // Traditional mocking still available

// Create two complementary Partials:
//  1. All the non-static functions for testing
//  2. Mocked static functions to be used in test cases
//
// We need both Partials with non-overlapping lists of functions in
// order to separate the testable functions from the mocked functions
// extracted from the same source module.

// Make all the non-static functions available for testing
#include TEST_PARTIAL_PUBLIC_MODULE(sensor)

// Make the static helper function available as a mock
#include MOCK_PARTIAL_PRIVATE_MODULE(sensor)

// Test Sensor_ReadCelsius() using a mock of the helper function
void test_Sensor_ReadCelsius(void)
{
    // Traditional mock of external HAL interface
    HAL_SensorRead_ExpectAndReturn(1234);

    // Partial mock of `static` function internal to source module under test
    _ConvertRawToMilliCelsius_ExpectAndReturn(1234, 1000);

    TEST_ASSERT_EQUAL_INT(1, Sensor_ReadCelsius());
}
```

### Partials processing step-by-step

1. Reads `sensor.c` and `sensor.h`, extracts all function definitions.
1. Classifies `_ConvertRawToMilliCelsius` as **private** (from the `static`
   decorator).
1. Generates `ceedling_partial_sensor_interface.h` containing only
   `_ConvertRawToMilliCelsius()`.
1. Collects all non-static functions in the `sensor` module and
   generates `ceedling_partial_sensor_impl.h` and 
   `ceedling_partial_sensor_impl.c` containing those functions segregated
   from the mockable function signature organized in (3).
1. Runs CMock on the Partial interface header to produce mock source.
1. Compiles and links the mocked Partial interface source from (3), the 
   Partial implementation source from (4) in place of the original `sensor` 
   source module, and the test file into the test executable. The 
   symbols and includes of `sensor.h` and `sensor.c` are duplicated in the 
   Partials while the original `sensor.c` is omitted from the build.
