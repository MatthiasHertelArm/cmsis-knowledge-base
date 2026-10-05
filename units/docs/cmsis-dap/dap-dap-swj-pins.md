---
id: "dap-dap-swj-pins"
type: "concept"
domain: "debug"
title: "DAP_SWJ_Pins"
summary: "The DAP_SWJ_Pins Command is used to monitor and control the I/O Pins including the nRESET Device reset line."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_SWJ_Pins.html"
license: "Apache-2.0"
mode: "V"
---

Control and monitor SWD/JTAG Pins


The **DAP_SWJ_Pins Command** is used to monitor and control the I/O Pins including the nRESET Device reset line.

The **Pin Wait** time is useful in systems where the nRESET pin is implemented as open-drain output.
After nRESET is de-asserted by the debugger, external circuit may still hold the target Device
under reset for a time. Using the **Pin Wait** time, the debugger may monitor
selected I/O Pins and wait until they the expected value appears or a timeout expires.

**I/O Pin Mapping** for the fields **Pin Output**, **Pin Select**, and **Pin Input**:
  - Bit 0: SWCLK/TCK
  - Bit 1: SWDIO/TMS
  - Bit 2: TDI
  - Bit 3: TDO
  - Bit 5: nTRST
  - Bit 7: nRESET


**DAP_SWJ_Pins Command**:
```
| BYTE | BYTE ******| BYTE ******| Word ****|
> 0x10 | Pin Output | Pin Select | Pin Wait |
|******|************|************|**********|
```

- **Pin Output**: Value for selected output pins
- **Pin Select**: Selects which output pins will be modified
- **Pin Wait**: Wait timeout for the selected output to stabilize
  - 0 = no wait
  - 1 .. 3000000 = time in µs (max 3s)

**DAP_SWJ_Pins Response:**
```
| BYTE | BYTE *****|
< 0x10 | Pin Input |
|******|***********|
```
- **Pin Input**: Pin state read from target Device.
