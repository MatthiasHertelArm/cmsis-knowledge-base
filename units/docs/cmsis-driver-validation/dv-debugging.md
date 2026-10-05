---
id: "dv-debugging"
type: "concept"
domain: "drivers"
title: "Debugging"
summary: "After running the CMSIS-Driver Validation output report is used to see if the driver is compliant to the CMSIS-Driver specification."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DriverValidation.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/debugging.html"
license: "Apache-2.0"
mode: "V"
---

After running the CMSIS-Driver Validation output report is used to see if the driver is compliant to the CMSIS-Driver specification.

If the result of the driver testing under `<c>`Test Summary</c> contains any `<c>`Failed</c> tests then the driver needs to be corrected.

Example of report in the Plain Text format of a non-compliant SPI driver:
```
CMSIS-Driver SPI Test Report   May  6 2020   10:47:11

TEST 01: SPI_GetVersion
  DV_SPI.c (1023): [INFO] Driver API version 2.3, Driver version 2.15
                                          PASSED
TEST 02: SPI_GetCapabilities              PASSED
TEST 03: SPI_Initialize_Uninitialize
  DV_SPI.c (1106): [FAILED]
  DV_SPI.c (1109): [FAILED]
  DV_SPI.c (1112): [FAILED]
                                          FAILED
TEST 04: SPI_PowerControl
  DV_SPI.c (1314): [WARNING] PowerControl (ARM_POWER_LOW) is not supported
                                          PASSED
...

Test Summary: 56 Tests, 24 Passed, 1 Failed.
Test Result: FAILED
```

From previous report it is clear that one test function has failed.

By Inspecting the details in previous report it is clear that `<c>`TEST 03: SPI_Initialize_Uninitialize</c> has failed
on multiple assertions.

Each failed assertion is recorded as a single  line in the test report.

The failed assert information in the output report contains additional information about the **source module** and **line**
in that module where the assertion is located with additional debugging info if available.

The documentation can be consulted regarding the failed function, for example in previous case
documentation on the SPI_Initialize_Uninitialize can be consulted.

Main way of fixing the driver consists of opening reported file mentioned as failed and inspecting the
line in which failure was reported.

If there are many failures, it is recommended to deselect all tests except first failing one
so it is easier to focus on just that failure.
Also, selecting only first failing test removes potential clutter from following failing tests that
are all failing due to same cause.

In the previous report, opening **DV_SPI.c** module (available in the project) and inspecting the **1106** line
which states:
```
  // Driver is uninitialized and peripheral is powered-off:
  // Call PowerControl(ARM_POWER_FULL) function and assert that it returned ARM_DRIVER_ERROR status
  TEST_ASSERT(drv->PowerControl (ARM_POWER_FULL) == ARM_DRIVER_ERROR);
```

informs us that call to `<c>`PowerControl (ARM_POWER_FULL)`</c>`, when driver is not initialized, is expected to
return `<c>`ARM_DRIVER_ERROR</c> status code but it has returned a different status code instead.

We should put a breakpoint to this line and start the debug session.

When the breakpoint is hit we can see that a call to `<c>`PowerControl (ARM_POWER_FULL)`</c>` has returned `<c>`ARM_DRIVER_OK</c>
instead of expected `<c>`ARM_DRIVER_ERROR</c> status code.

We can now go into source code of the driver and fix this.

After we have fixed the driver, the report now looks like below:

```
CMSIS-Driver SPI Test Report   May  6 2020   11:15:30

TEST 01: SPI_GetVersion
  DV_SPI.c (1023): [INFO] Driver API version 2.3, Driver version 2.15
                                          PASSED
TEST 02: SPI_GetCapabilities              PASSED
TEST 03: SPI_Initialize_Uninitialize      PASSED
TEST 04: SPI_PowerControl
  DV_SPI.c (1314): [WARNING] PowerControl (ARM_POWER_LOW) is not supported
                                          PASSED
...

Test Summary: 56 Tests, 25 Passed, 0 Failed.
Test Result: PASSED
```

The fix for the assertion failing in line 1106 has also fixed subsequent assertions
in lines 1109 and 1112 thus the driver now reports no failed tests and reports that all
of the 25 executed tests have passed.

This report could be used as an insurance that the SPI Driver on this device is compliant to the CMSIS-Driver specification.
