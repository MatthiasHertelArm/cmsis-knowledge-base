---
id: "dap-transfer-commands-usage-example"
type: "concept"
domain: "debug"
title: "Transfer Commands: Usage Example"
summary: "A common use case for this mechanism is polling the Cortex-M debug registers via SWD."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_transfer_gr.html"
license: "Apache-2.0"
mode: "V"
---

A common use case for this mechanism is polling the Cortex-M debug registers via SWD. For example, reading a core
register through the Debug Core Register Selector (DCRSR) requires writing the register identifier and then polling
DHCSR until the S_REGRDY bit indicates the result is ready. The match mask/value match mechanism in DAP_Transfer
can implement this pattern without explicit looping in the host:

- Call DAP_TransferConfigure to set the retry behavior. Typical implementations use defaults of Idle Cycles = 0,
  WAIT Retry = 100, and Match Retry set to a value sufficient for the expected polling duration. The Match Retry count
  need only be set once; it persists until reconfigured.

- Issue a DAP_Transfer with a Transfer Count of at least two transfers in the same request. The first transfer
  writes the match mask (using the Match Mask bit set in the request). The mask defines which bits in the read value
  are relevant for comparison (for example, selecting the S_REGRDY bit). The second transfer performs the actual read
  with the Value Match bit set and includes the expected Match_Value in the transfer data.
