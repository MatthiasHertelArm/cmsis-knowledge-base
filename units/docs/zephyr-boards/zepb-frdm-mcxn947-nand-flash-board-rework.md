---
id: "zepb-frdm-mcxn947-nand-flash-board-rework"
type: "concept"
domain: "bring-up"
title: "frdm_mcxn947: NAND Flash (Board Rework)"
summary: "The FlexSPI PortA on FRDM-MCXN947 is pin-compatible with SPI NAND flash. A Macronix MX35LF1GE4AB (1 Gbit) can replace the W25Q64 NOR at U32 by board rework, providing 128 MB of NAND storage accessible via the FlexSPI controller."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nxp/frdm_mcxn947/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxn947/doc/index.html#nand-flash-board-rework"
license: "Apache-2.0"
mode: "V"
---

The FlexSPI PortA on FRDM-MCXN947 is pin-compatible with SPI NAND flash.
A Macronix MX35LF1GE4AB (1 Gbit) can replace the W25Q64 NOR at U32 by
board rework, providing 128 MB of NAND storage accessible via the FlexSPI
controller.

The `mx35lf1ge4ab` device tree node is present in the board DTS but disabled
by default. Enable it with a devicetree overlay, and disable the NOR node
since the two are mutually exclusive:

```devicetree

&ext_flash_ctrl {
    status = "disabled";
};

&mx35lf1ge4ab {
    status = "okay";
};
```
The littlefs sample provides ready-made board files
(`boards/frdm_mcxn947_nand.*`) that run LittleFS over Dhara FTL on this NAND.


### Troubleshooting


.. _bootfromflash.bin:
   https://github.com/nxp-mcuxpresso/mcuxsdk-examples/blob/main/_boards/frdmmcxn947/demo_apps/hello_world_qspi_xip/cm33_core0/bootfromflash.bin

.. _bootfromflexspi.bin:
   https://github.com/nxp-mcuxpresso/mcuxsdk-examples/blob/main/_boards/frdmmcxn947/demo_apps/hello_world_qspi_xip/cm33_core0/bootfromflexspi.bin
