---
id: "dv-configuration-configuration-settings-2"
type: "concept"
domain: "drivers"
title: "Configuration: Configuration settings"
summary: "For example if we want to test <c>Driver_ETH_MAC2</c> then this setting would be set to <c>2</c>."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_ETH.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/eth_config.html"
license: "Apache-2.0"
mode: "V"
---

**Driver_ETH_MAC#** selects the driver instance that will be tested.

For example if we want to test `<c>`Driver_ETH_MAC2</c> then this setting would be set to `<c>`2</c>.

**Link timeout** specifies timeout for link check, expressed in milliseconds.

**Transfer timeout** setting specifies maximum timeout for a transfer, expressed in milliseconds.

**Time duration for PTP Control Time** setting specifies referent time interval used for PTP testing, expressed in milliseconds.

**Tolerance for PTP Control Time** setting specifies allowed deviation of measured time 
in comparison to expected time in PTP frames, expressed in nanoseconds.

**Tests** section contains selections of tests to be executed.
For details on tests performed by each test function please refer to Ethernet Tests.
