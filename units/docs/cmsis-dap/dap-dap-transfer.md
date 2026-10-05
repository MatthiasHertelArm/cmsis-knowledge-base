---
id: "dap-dap-transfer"
type: "concept"
domain: "debug"
title: "DAP_Transfer"
summary: "Read/write single and multiple registers."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_Transfer.html"
license: "Apache-2.0"
mode: "V"
---

Read/write single and multiple registers.


The **DAP_Transfer Command** reads or writes data to CoreSight registers.
Each CoreSight register is accessed with a single 32-bit read or write.
The CoreSight registers are addressed with DPBANKSEL/APBANKSEL and address lines A2, A3 (A0 = 0 and A1 = 0).
This command executes several read/write operations on the selected DP/AP registers.
The Transfer Data in the Response are in the order of the Transfer Request in the Command but might be shorter in case of communication failures.
The data transfer is aborted on a communication error:
  - Protocol Error
  - Target FAULT response
  - Target WAIT responses exceed configured value
  - Value Mismatch (Read Register with Value Match)

**DAP_Transfer Command:**
```
| BYTE | BYTE *****| BYTE **********| BYTE *************| WORD *********|
> 0x05 | DAP Index | Transfer Count | Transfer Request  | Transfer Data |
|******|***********|****************|+++++++++++++++++++++++++++++++++++|
```

- **DAP Index**: Zero based device index of the selected JTAG device. For SWD mode the value is ignored.

- **Transfer Count**: Number of transfers: 1 .. 255. For each transfer a Transfer Request BYTE is sent. Depending on the request an additional Transfer Data WORD is sent.

- **Transfer Request**: Contains information about requested access from host debugger.
  - Bit 0: APnDP: 0 = Debug Port (DP), 1 = Access Port (AP).
  - Bit 1: RnW: 0 = Write Register, 1 = Read Register.
  - Bit 2: A2 Register Address bit 2.
  - Bit 3: A3 Register Address bit 3.
  - Bit 4: Value Match (only valid for Read Register): 0 = Normal Read Register, 1 = Read Register with Value Match.
  - Bit 5: Match Mask (only valid for Write Register): 0 = Normal Write Register, 1 = Write Match Mask (instead of Register).
  - Bit 7: TD_TimeStamp request: 0 = No time stamp, 1 = Include time stamp value from Test Domain Timer before every Transfer Data word (restrictions see note).

- **Transfer Data**: register value or match value
  - for Write Register transfer request: the register value for the CoreSight register.
  - for Match Mask transfer request: the match mask for the CoreSight register.
  - for Value Match transfer request: the match value of the CoreSight register.
  - no data is sent for other operations.

**Note:**
**Transfer Request** - Bit 7 (Time Stamp) cannot be combined with Bit 4 (Value Match) or Bit 5 (Match Mask).



**DAP_Transfer Response:**
```
| BYTE | BYTE **********| BYTE *************| WORD ********| WORD *********|
< 0x05 | Transfer Count | Transfer Response | TD_TimeStamp | Transfer Data |
|******|****************|*******************|//////////////|+++++++++++++++|
```

- **Transfer Count**: Number of transfers: 1 .. 255 that are executed.

- **Transfer Response**: Contains information about last response from target Device.
  - Bit 2..0: ACK (Acknowledge) value:
      - 1 = OK (for SWD protocol), OK or FAULT (for JTAG protocol),
      - 2 = WAIT
      - 4 = FAULT
      - 7 = NO_ACK (no response from target)
  - Bit 3: 1 = Protocol Error (SWD)
  - Bit 4: 1 = Value Mismatch (Read Register with Value Match)

- **TD_TimeStamp**: current Test Domain Timer value is added before each Transfer Data word when Transfer Request - bit 7: TD_TimeStamp request is set.

- **Transfer Data**: register value or match value in the order of the **Transfer Request**.
  - for Read Register transfer request: the register value of the CoreSight register.
  - no data is sent for other operations.
