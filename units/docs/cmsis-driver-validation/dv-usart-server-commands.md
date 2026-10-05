---
id: "dv-usart-server-commands"
type: "concept"
domain: "drivers"
title: "USART Server: Commands"
summary: "Commands are human-readable (ASCII) for easier analysis with a USART bus analyzer."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_USART.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/usart_server.html"
license: "Apache-2.0"
mode: "V"
---

Commands are human-readable (ASCII) for easier analysis with a USART bus analyzer.

- **GET VER** - get Server version
- **GET CAP** - get Server capabilities (auto-detected upon reception)
- **SET BUF** - initialize Rx/Tx buffer content
- **GET BUF** - retrieve Rx/Tx buffer content
- **SET COM** - specify transfer configuration for the next **XFER**
- **XFER** - trigger a transfer
- **GET CNT** - retrieve number of items transferred in the last transfer
- **SET BRK** - generate break signal
- **GET BRK** - read break signal status
- **SET MDM** - activate modem lines
- **GET MDM** - read modem line status

**Note:** For detailed command descriptions, see **README.md** in project root.

Example capture: validating the **Send** function in **Asynchronous** mode:
 width=100%
