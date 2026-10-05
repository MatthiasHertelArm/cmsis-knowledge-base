---
id: "dap-dap-transferconfigure"
type: "concept"
domain: "debug"
title: "DAP_TransferConfigure"
summary: "The DAP_TransferConfigure Command sets parameters for DAP_Transfer and DAP_TransferBlock."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_TransferConfigure.html"
license: "Apache-2.0"
mode: "V"
---

Configure Transfers

The **DAP_TransferConfigure Command** sets parameters for DAP_Transfer and DAP_TransferBlock.

**DAP_TransferConfigure Command:**
```
| BYTE | BYTE ******** SHORT *****| SHORT ******|
> 0x04 | Idle Cycles | WAIT Retry | Match Retry |
|******|*************|************|*************|
```

- **Idle Cycles**: Number of extra idle cycles after each transfer.
- **WAIT Retry**: Number of transfer retries after WAIT response.
- **Match Retry**: Number of retries on reads with Value Match in DAP_Transfer. On value mismatch the
    Register is read again until its value matches or the **Match Retry** count exceeds.\n
```
  retry = Match_Retry;
  do {
    if ((Register_Value & Match_Mask) == Match_Value) break;
  } while (retry--);
```

**DAP_TransferConfigure Response**:
```
| BYTE | BYTE **|
< 0x04 | Status |
|******|********|
```

- **Status:** DAP_Response_Status
