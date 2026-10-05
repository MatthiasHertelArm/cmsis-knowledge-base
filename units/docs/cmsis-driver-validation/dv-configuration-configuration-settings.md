---
id: "dv-configuration-configuration-settings"
type: "concept"
domain: "drivers"
title: "Configuration: Configuration settings"
summary: "For example if we want to test <c>Driver_CAN2</c> then this setting would be set to <c>2</c>."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_CAN.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/can_config.html"
license: "Apache-2.0"
mode: "V"
---

**Driver_CAN#** selects the driver instance that will be tested.

For example if we want to test `<c>`Driver_CAN2</c> then this setting would be set to `<c>`2</c>.

**CAN bitrates** section specifies which bitrate settings will be tested.
If a setting is not to be tested then set the value to 0.

**Ratio data/arbitration bitrate** setting specifies ratio between data and arbitration bitrate 
which is used for CAN FD.

**Percentual trigger for bitrate tests** setting specifies allowed deviation of measured bitrate 
in comparison to requested bitrate, expressed in percents.

**Transfer timeout** setting specifies maximum timeout for a transfer, expressed in microseconds.

**Tests** section contains selections of tests to be executed.

For details on tests performed by each test function please refer to CAN Tests.
