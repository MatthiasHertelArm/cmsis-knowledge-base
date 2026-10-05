---
id: "dv-spi-server-commands"
type: "concept"
domain: "drivers"
title: "SPI Server: Commands"
summary: "Commands are human-readable (ASCII) for simpler analysis with an SPI bus analyzer."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_SPI.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/spi_server.html"
license: "Apache-2.0"
mode: "V"
---

Commands are human-readable (ASCII) for simpler analysis with an SPI bus analyzer.

- **GET VER** - get Server version
- **GET CAP** - get capabilities (auto-detected)
- **SET BUF** - initialize Rx/Tx buffer content
- **GET BUF** - retrieve Rx/Tx buffer content
- **SET COM** - specify transfer configuration for the next **XFER**
- **XFER** - trigger a transfer
- **GET CNT** - retrieve number of transferred items in the last transfer

**Note:** For detailed command descriptions, see **README.md** in project root.

Example capture (Master transfer validation):
 width=100%
