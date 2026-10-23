---
id: "zepb-frdm-mcxn947-hardware"
type: "concept"
domain: "bring-up"
title: "frdm_mcxn947: Hardware"
summary: "For more information about the MCX-N947 SoC and FRDM-MCXN947 board, see:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/nxp/frdm_mcxn947/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxn947/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

- MCX-N947 Dual Arm Cortex-M33 microcontroller running at 150 MHz
- 2MB dual-bank on chip Flash
- 512 KB RAM
- External Quad SPI flash over FlexSPI
- USB high-speed (Host/Device) with on-chip HS PHY. HS USB Type-C connectors
- 10x LP Flexcomms each supporting SPI, I2C, UART
- 2x FlexCAN with FD, 2x I3Cs, 2x SAI
- 1x Ethernet with QoS
- On-board MCU-Link debugger with CMSIS-DAP
- Arduino Header, FlexIO/LCD Header, SmartDMA/Camera Header, mikroBUS

For more information about the MCX-N947 SoC and FRDM-MCXN947 board, see:

- MCX-N947 SoC Website
- MCX-N947 Datasheet
- MCX-N947 Reference Manual
- FRDM-MCXN947 Website
- FRDM-MCXN947 User Guide
- FRDM-MCXN947 Board User Manual
- FRDM-MCXN947 Schematics


### Supported Features



### Shields for Supported Features


Some features in the table above are tested with Zephyr shields.  These shields
are tested on this board:

- lcd_par_s035 - supports the Display interface.  This board uses the
  MIPI_DBI interface of the shield, connected to the FlexIO on-chip peripheral.
- dvp_20pin_ov7670 - supports the SmartDMA video interface.
