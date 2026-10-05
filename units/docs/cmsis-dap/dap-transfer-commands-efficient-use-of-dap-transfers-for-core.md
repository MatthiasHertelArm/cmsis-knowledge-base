---
id: "dap-transfer-commands-efficient-use-of-dap-transfers-for-core"
type: "concept"
domain: "debug"
title: "Transfer Commands: Efficient use of DAP Transfers for Core Register Reads"
summary: "By arranging the mask and value in a single DAP_Transfer request, the firmware will repeatedly execute the read until the masked value matches or the retry limit is reached."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_transfer_gr.html"
license: "Apache-2.0"
mode: "V"
---

By arranging the mask and value in a single DAP_Transfer request, the firmware will repeatedly execute the read
until the masked value matches or the retry limit is reached. The match mask remains in effect for subsequent transfers
in the same request. Additional match value reads can follow within the same DAP_Transfer request up to the
protocol limit of 255 transfers, subject to USB packet size constraints. Combining multiple mask/value match pairs in
this way can reduce USB overhead compared to separate transfers per read.

This value match and retry mechanism applies only to DAP_Transfer; it is not supported by DAP_TransferBlock.
There is no separate time-based timeout; the effective delay is determined by the configured Match Retry count and the
speed of the underlying debug interface.

For long sequences of transfers that must execute without USB round-trips between operations, the
DAP_QueueCommands_gr API exists; however, for typical polling reads using match mask/value match, queuing is not
required.
