---
id: "zep-arm-cortex-m-developer-guide-qemu"
type: "concept"
domain: "rtos"
title: "Arm Cortex-M Developer Guide: QEMU"
summary: "We use QEMU to verify the implemented features of the Cortex-M architecture port in Zephyr. Adequate coverage is achieved by defining and utilizing a list of QEMU targets, each with a specific architecture variant and Arm peripheral support list."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/arch/arm_cortex_m.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/arch/arm_cortex_m.rst"
license: "Apache-2.0"
mode: "V"
---

We use QEMU to verify the implemented features of the Cortex-M architecture port in Zephyr.
Adequate coverage is achieved by defining and utilizing a list of QEMU targets,
each with a specific architecture variant and Arm peripheral support list.

The table below lists the QEMU platform targets defined in Zephyr
along with the corresponding Cortex-M implementation variant and the peripherals
these targets emulate.

+---------------------------------+--------------------+--------------------+----------------+----------------------+----------------------------+
|                                 | **QEMU target**                                                                                              |
+---------------------------------+--------------------+--------------------+----------------+----------------------+----------------------------+
| Architecture variant            | Arm v6-M           | Arm v7-M                            | Arm v8-M             | Arm v8.1-M                 |
+---------------------------------+--------------------+--------------------+----------------+----------------------+----------------------------+
|                                 | **qemu_cortex_m0** | **qemu_cortex_m3** | **mps2/an385** | **mps2/an521/cpu0**  | **mps3/corstone300/an547** |
+---------------------------------+--------------------+--------------------+----------------+----------------------+----------------------------+
| **Emulated features**           |                                                                                                              |
+---------------------------------+--------------------+--------------------+----------------+----------------------+----------------------------+
| NVIC                            | Y                  | Y                  | Y              | Y                    | Y                          |
+---------------------------------+--------------------+--------------------+----------------+----------------------+----------------------------+
| BASEPRI                         | N                  | Y                  | Y              | Y                    | Y                          |
+---------------------------------+--------------------+--------------------+----------------+----------------------+----------------------------+
| SysTick                         | N                  | Y                  | Y              | Y                    | Y                          |
+---------------------------------+--------------------+--------------------+----------------+----------------------+----------------------------+
| MPU                             | N                  | N                  | Y              | Y                    | Y                          |
+---------------------------------+--------------------+--------------------+----------------+----------------------+----------------------------+
| FPU                             | N                  | N                  | N              | Y                    | N                          |
+---------------------------------+--------------------+--------------------+----------------+----------------------+----------------------------+
| SPLIM                           | N                  | N                  | N              | Y                    | Y                          |
+---------------------------------+--------------------+--------------------+----------------+----------------------+----------------------------+
| TrustZone-M                     | N                  | N                  | N              | Y                    | N                          |
+---------------------------------+--------------------+--------------------+----------------+----------------------+----------------------------+
