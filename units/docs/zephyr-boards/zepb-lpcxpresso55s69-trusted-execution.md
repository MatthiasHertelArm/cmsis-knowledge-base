---
id: "zepb-lpcxpresso55s69-trusted-execution"
type: "concept"
domain: "bring-up"
title: "lpcxpresso55s69: Trusted Execution"
summary: "+-----------+------------------+--------------------+ | Memory | Address[Size] | Comment | +===========+==================+====================+ | MCUboot | 0x00000000[32K] | Secure bootloader | +-----------+------------------+--------------------+ | TFM_S | 0x00008000[160k] | Secure image | +-----------+------------------+--------------------+ | Zephyr_NS | 0x00030000[96k] | Non-Secure image | +-----------+------------------+--------------------+ | storage …"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/nxp/lpcxpresso55s69/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso55s69/doc/index.html#trusted-execution"
license: "Apache-2.0"
mode: "V"
---

+-----------+------------------+--------------------+
| Memory    | Address[Size]    | Comment            |
+===========+==================+====================+
| MCUboot   | 0x00000000[32K]  | Secure bootloader  |
+-----------+------------------+--------------------+
| TFM_S     | 0x00008000[160k] | Secure image       |
+-----------+------------------+--------------------+
| Zephyr_NS | 0x00030000[96k]  | Non-Secure image   |
+-----------+------------------+--------------------+
| storage   | 0x00088000[50k]  | Persistent storage |
+-----------+------------------+--------------------+

+----------------+------------------+-------------------+
| RAM            | Address[Size]    | Comment           |
+================+==================+===================+
| secure_ram     | 0x20000000[136k] | Secure memory     |
+----------------+------------------+-------------------+
| non_secure_ram | 0x20022000[136k] | Non-Secure memory |
+----------------+------------------+-------------------+
