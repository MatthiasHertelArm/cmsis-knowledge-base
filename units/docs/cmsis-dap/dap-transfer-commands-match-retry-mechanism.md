---
id: "dap-transfer-commands-match-retry-mechanism"
type: "concept"
domain: "debug"
title: "Transfer Commands: Match Retry Mechanism"
summary: "The Match Retry parameter configured by DAP_TransferConfigure directly affects how DAP_Transfer processes read operations that use the match mask and value match features."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_transfer_gr.html"
license: "Apache-2.0"
mode: "V"
---

The _Match_ _Retry_ parameter configured by DAP_TransferConfigure directly affects how DAP_Transfer
processes read operations that use the match mask and value match features.

When a transfer uses the _value_ _match_ mechanism, the _match_ _mask_ previously set in the same DAP_Transfer
request is applied to the value read from the target register. The firmware compares (Register_Value & Match_Mask) with
the provided Match_Value on each read. If the masked value does not equal the expected value, the controller will
automatically retry the read until either the masked value matches or the configured _Match_ _Retry_ count is
exhausted. If the retry limit is reached without a match, Bit 4 (_Value_ _Mismatch)_ is set in the response and the
DAP_Transfer command aborts. This behavior is governed by the _Match_ _Retry_ parameter documented in
DAP_TransferConfigure (see Match Retry: Number of retries on reads with Value Match in DAP_Transfer).
