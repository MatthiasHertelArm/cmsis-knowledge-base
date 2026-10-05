---
id: "dap-dap-transferblock"
type: "concept"
domain: "debug"
title: "DAP_TransferBlock"
summary: "Read/Write a block of data from/to a single register."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_TransferBlock.html"
license: "Apache-2.0"
mode: "V"
---

Read/Write a block of data from/to a single register.


The **DAP_TransferBlock Command** read or write a data block to the same CoreSight register.
A data block are multiple 32-bit values which are read or written from/to the same CoreSight register.
The CoreSight register is addressed with DPBANKSEL/APBANKSEL and address lines A2, A3 (A0 = 0 and A1 = 0).
The command can execute several read/write operations to a single DP/AP register.

The data transfer is aborted on a communication error:
  - Protocol Error
  - Target FAULT response
  - Target WAIT responses exceed configured value

**DAP_TransferBlock Command**:
```
| BYTE | BYTE *****| SHORT**********| BYTE *************| WORD *********|
> 0x06 | DAP Index | Transfer Count | Transfer Request  | Transfer Data |
|******|***********|****************|*******************|+++++++++++++++|
```

- **DAP Index**: Zero based device index of the selected JTAG device. For SWD mode the value is ignored.

- **Transfer Count**: Number of transfers: 1 .. 65535.

- **Transfer Request**: Contains information about requested access from host
  - Bit 0: APnDP: 0 = DP (Debug Port), 1 = AP (Access Port)
  - Bit 1: RnW: 0 = Write Register, 1 = Read Register
  - Bit 2: A2 := Register Address bit 2
  - Bit 3: A3 := Register Address bit 3

- **Transfer Data**: register values
  - for Write Register transfer request: the register values written to the CoreSight register.
  - no data is sent for Read Register operations.

**DAP_TransferBlock Response**:
```
| BYTE | SHORT *********| BYTE *************| WORD *********|
< 0x06 | Transfer Count | Transfer Response | Transfer Data |
|******|****************|*******************|+++++++++++++++|
```

- **DAP Index**: Zero based device index of the selected JTAG device. For SWD mode the value is ignored.

- **Transfer Count**: Number of transfers (1 .. 65535) that are executed.

- **Transfer Response**: Contains information about last response from target
  - Bit 2..0: ACK (Acknowledge) value:
      - 1 = OK (for SWD protocol), OK or FAULT (for JTAG protocol),
      - 2 = WAIT
      - 4 = FAULT
      - 7 = NO_ACK (no response from target)
  - Bit 3: Protocol Error (SWD)

- **Transfer Data**: register values
  - no data is receive for Write Register operations.
  - for Read Register transfer request: the register values read from CoreSight register.
