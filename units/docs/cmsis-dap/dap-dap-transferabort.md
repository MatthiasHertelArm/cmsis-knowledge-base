---
id: "dap-dap-transferabort"
type: "concept"
domain: "debug"
title: "DAP_TransferAbort"
summary: "The DAP_TransferAbort Command aborts the current transfer. The command can be executed while DAP_Transfer or DAP_TransferBlock command is still in progress. The command is ignored if there is no transfer in progress."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_TransferAbort.html"
license: "Apache-2.0"
mode: "V"
---

Abort current Transfer

The **DAP_TransferAbort Command** aborts the current transfer. The command can be executed while DAP_Transfer or DAP_TransferBlock command
is still in progress. The command is ignored if there is no transfer in progress. The command itself has no response, however the
aborted DAP_Transfer or DAP_TransferBlock command will respond with information about the actually transferred data.

**DAP_TransferAbort Command**:
```
| BYTE |
> 0x07 |
|******|
```
