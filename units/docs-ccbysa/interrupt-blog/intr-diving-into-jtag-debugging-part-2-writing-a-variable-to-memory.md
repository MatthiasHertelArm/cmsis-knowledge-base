---
id: "intr-diving-into-jtag-debugging-part-2-writing-a-variable-to-memory"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Debugging (Part 2): Writing a variable to memory"
summary: "Alright, let’s write the value 0xAA55AA55 to the address 0x20000000:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-29-diving-into-jtag-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-2#writing-a-variable-to-memory"
license: "CC-BY-SA-4.0"
mode: "V"
---

Alright, let’s write the value `0xAA55AA55` to the address `0x20000000`:

First, write `0b1010` (the `DPACC` register code) into the `IR` register. Some settings in the `AP` register `CSW` need to be configured. To access this register, we need to select the corresponding AP and register bank in the `DP SELECT` register. Write to the `DR` register:
  * DATA[31:0] = `0x00`
  * APSEL[31:24] = `0x00`
  * APBANKSEL[7:4] = `0x00`
  * A[3:2] = `0b10` (address of `SELECT` register)
  * RnW = `0b0`



Next, we need to write the `CSW` register. Since this is an `AP` register, we need to use the `APACC` register to access it:
  * Write `0b1011` (the `APACC` register code) into the `IR` register.

Create the data for the configuration: set the data size for writing to 32 bits (`Size[0:2] = 0b010`), disable the auto-increment function of the address (`AddrInc[5:4] = 0b00`). Write to `DR`.
  * DATA[31:0] = `0x00000002`
  * A[3:2] = `0b00` (address of CSW register)
  * RnW = `0b0`



Then we need to set the address of the memory cell to which we want to write the data. This is done through the `AP ` register `TAR`. And since this register belongs to the same `AP` as `CSW` and is in the same bank, we can omit the reference to the `DP SELECT` register and immediately write the address value. Write to DR:
  * DATA[31:0] = `0x20000000`
  * A[3:2] = `0b01` (address of `TAR` register)
  * RnW = `0b0`



The last step is to actually write the data. To do this, we need to write them to the DRW register. Write to DR:
  * DATA[31:0] = `0xAA55AA55`
  * A[3:2] = `0b11` (address of `DRW` register)
  * RnW = `0b0`


