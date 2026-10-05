---
id: "dv-configuration-configuration-settings-3"
type: "concept"
domain: "drivers"
title: "Configuration: Configuration settings"
summary: "For example if we want to test <c>Driver_GPIO0</c> then this setting would be set to <c>0</c>."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_GPIO.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/gpio_config.html"
license: "Apache-2.0"
mode: "V"
---

**Driver_GPIO#** selects the driver instance that will be tested.

For example if we want to test `<c>`Driver_GPIO0</c> then this setting would be set to `<c>`0</c>.

**Configuration** section contains configuration of two pins:
- **Pin Under Test** specifying the pin that will be tested.

- **Auxiliary Pin** specifies the auxiliary pin with serial low resistance resistor connected to Pin Under Test.
  Suggested resistance of this serial resistor is around 1 kOhm.


**Pins** should not have any external resistors or any external devices connected to it except the low resistance resistor used for testing.


**Tests** section contains selections of tests to be executed.
For details on tests performed by each test function please refer to GPIO Tests.
