---
id: "zep-board-porting-guide-hardware-support-hierarchy"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: Hardware support hierarchy"
summary: "Zephyr's hardware support is based on a series of hierarchical abstractions. Primarily, each board has one or more SoC. Each SoC can be optionally classed into an SoC series, which in turn may optionally belong to an SoC family."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr's hardware support is based on a series of hierarchical abstractions.
Primarily, each `board` has one or more `SoC`.
Each SoC can be optionally classed into an `SoC series`, which in turn may optionally belong to an `SoC family`.
Each SoC has one or more `CPU cluster`, each containing one or more `CPU core` of a particular `architecture`.

You can visualize the hierarchy in the diagram below:

Below are some examples of the hierarchy described in this section, in the form
of a `board` per row with its corresponding hierarchy entries. Notice how
the `SoC series` and `SoC family` levels are not always used.


+--------------------------------------------+--------------------------+-------------+--------------------+--------------------+----------------+----------------------+
| `board name`                         | `board qualifiers` | `SoC` | `SoC Series` | `SoC family` | CPU core       | `architecture` |
+============================================+==========================+=============+====================+====================+================+======================+
| nrf52dk                    | nrf52832                 | nRF52832    | nRF52              | Nordic nRF         | Arm Cortex-M4  | ARMv7-M              |
+--------------------------------------------+--------------------------+-------------+--------------------+--------------------+----------------+----------------------+
| frdm_k64f      | mk64f12                  | MK64F12     | Kinetis K6x        | NXP Kinetis        | Arm Cortex-M4  | ARMv7-M              |
+--------------------------------------------+--------------------------+-------------+--------------------+--------------------+----------------+----------------------+
| rv32m1_vega  | openisa_rv32m1/ri5cy     | RV32M1      | (Not used)         | (Not used)         | RI5CY          | RISC-V RV32          |
+--------------------------------------------+--------------------------+-------------+--------------------+--------------------+----------------+----------------------+
| nrf5340dk                  | nrf5340/cpuapp           | nRF5340     | nRF53              | Nordic nRF         | Arm Cortex-M33 | ARMv8-M              |
|                                            +--------------------------+-------------+--------------------+--------------------+----------------+----------------------+
|                                            | nrf5340/cpunet           | nRF5340     | nRF53              | Nordic nRF         | Arm Cortex-M33 | ARMv8-M              |
+--------------------------------------------+--------------------------+-------------+--------------------+--------------------+----------------+----------------------+
| mimx8mp_evk   | mimx8ml8/a53             | i.MX8M Plus | i.MX8M             | NXP i.MX           | Arm Cortex-A53 | ARMv8-A              |
|                                            +--------------------------+-------------+--------------------+--------------------+----------------+----------------------+
|                                            | mimx8ml8/m7              | i.MX8M Plus | i.MX8M             | NXP i.MX           | Arm Cortex-M7  | ARMv7-M              |
|                                            +--------------------------+-------------+--------------------+--------------------+----------------+----------------------+
|                                            | mimx8ml8/adsp            | i.MX8M Plus | i.MX8M             | NXP i.MX           | Cadence HIFI4  | Xtensa LX6           |
+--------------------------------------------+--------------------------+-------------+--------------------+--------------------+----------------+----------------------+
Additional details about terminology can be found in the next section.
