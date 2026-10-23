---
id: "zepb-mimxrt1060-evk-shields-for-supported-features"
type: "concept"
domain: "bring-up"
title: "mimxrt1060_evk: Hardware / Shields for Supported Features"
summary: "Some features in the table above are tested with Zephyr shields. These shields are tested on this board:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/nxp/mimxrt1060_evk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1060_evk/doc/index.html#shields-for-supported-features"
license: "Apache-2.0"
mode: "V"
---

_Part of: Hardware_

Some features in the table above are tested with Zephyr shields.  These shields
are tested on this board:

- nxp_m2_wifi_bt - Rev C version is tested with this shield to attach any M.2 module
  with BT HCI UART interface and Wi-Fi SDIO interface. The shield binds the required NXP
  HCI driver or SDIO driver to perform firmware-load and other setup configurations
  for NXP SoC IW416/IW612/IW610.
- rk043fn02h_ct and rk043fn66hs_ctg - support the Display interface.
- dvp_fpc24_mt9m114 - supports the CSI video/camera interface.
