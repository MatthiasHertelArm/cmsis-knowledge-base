---
id: "intr-diving-into-jtag-debugging-part-2-reading-a-variable-from-memory"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Debugging (Part 2): Reading a variable from memory"
summary: "Let’s try to read the value from the memory cell at the address 0x20000000."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-29-diving-into-jtag-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-2#reading-a-variable-from-memory"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let’s try to read the value from the memory cell at the address `0x20000000`.

First, write `0b1010` (the `DPACC` register code) into the `IR` register. Next, we need to configure some settings in the `CSW` register of the `AP`. To access this register, we need to select the corresponding `AP` and register bank in the `DP SELECT` register. Using the data from the table, we form 35 bits of data that we write to the `DR` register:
  * DATA[31:0] = `0x00`
  * APSEL[31:24] = `0x00`
  * APBANKSEL[7:4] = `0x00`
  * A[3:2] = `0b10` (address of `SELECT` register)
  * RnW = `0b0`



Next, we need to write directly to the `CSW` register. Since this is an `AP` register, we need to use the `APACC` register to access it:
  * Write `0b1011` (the `APACC` register code) into the `IR` register.

We create the data for configuration: we set the data size for writing to 32 bits (`Size[0:2] = 0b010`) and disable the auto-increment address function (`AddrInc[5:4] = 0b00`). Write to `DR`:
  * DATA[31:0] = `0x00000002`
  * A[3:2] = 0b00 (address of `CSW` register)
  * RnW = `0b0`



Next, we need to set the address of the memory cell from which we will read the data. This is done through the `TAR` register of the `AP`. And since this register belongs to the same `AP` as `CSW` and is in the same bank, we can skip the `DP SELECT` register access and immediately write the address value:
  * DATA[31:0] = `0x20000000`
  * A[3:2] = `0b01` (address of `TAR` register)
  * RnW = `0b0`



We form a read request. To do this, we write to the `DRW` register:
  * DATA[31:0] = `0x00`
  * A[3:2] = `0b11` (address of `DRW` register)
  * RnW = `0b1`



Read the `DRW` register by reading 35 bits from the `DR` register.


