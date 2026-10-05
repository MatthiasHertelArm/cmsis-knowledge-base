---
id: "tfm-max32657-introduction"
type: "concept"
domain: "security"
title: "MAX32657: Introduction"
summary: "The MAX32657 microcontroller (MCU) is an advanced system-on-chip (SoC) featuring an Arm® Cortex®-M33 core with single-precision floating point unit (FPU) with digital signal processing (DSP) instructions, large flash and SRAM memories, and the latest generation Bluetooth® 5.4 Low …"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/adi/max32657/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/adi/max32657/.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

The MAX32657 microcontroller (MCU) is an advanced system-on-chip (SoC)
featuring an Arm® Cortex®-M33 core with single-precision floating point unit (FPU)
with digital signal processing (DSP) instructions, large flash and SRAM memories,
and the latest generation Bluetooth® 5.4 Low Energy (LE) radio.
The nano-power modes increase battery life substantially.

MAX32657 1MB flash and 256KB RAM split to define section for MCUBoot,
TF-M (S), Zephyr (NS) and storage that used for secure services and configurations.
Default layout of MAX32657 is listed in below table.

+----------+------------------+---------------------------------+
| Name     | Address[Size]    | Comment                         |
+==========+==================+=================================+
| boot     | 0x1000000[64K]   | MCU Bootloader                  |
+----------+------------------+---------------------------------+
| slot0    | 0x1010000[320k]  | Secure image slot0 (TF-M)       |
+----------+------------------+---------------------------------+
| slot0_ns | 0x1060000[576k]  | Non-secure image slot0          |
+----------+------------------+---------------------------------+
| slot1    | 0x10F0000[0k]    | Updates slot0 image             |
+----------+------------------+---------------------------------+
| slot1_ns | 0x10F0000[0k]    | Updates slot0_ns image          |
+----------+------------------+---------------------------------+
| storage  | 0x10f0000[64k]   | File system, persistent storage |
+----------+------------------+---------------------------------+


+----------------+------------------+-------------------+
| RAM            | Address[Size]    | Comment           |
+================+==================+===================+
| secure_ram     | 0x30000000[64k]  | Secure memory     |
+----------------+------------------+-------------------+
| non_secure_ram | 0x20010000[192k] | Non-Secure memory |
+----------------+------------------+-------------------+
