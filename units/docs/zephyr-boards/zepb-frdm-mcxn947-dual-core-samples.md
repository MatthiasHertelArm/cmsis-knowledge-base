---
id: "zepb-frdm-mcxn947-dual-core-samples"
type: "concept"
domain: "bring-up"
title: "frdm_mcxn947: Dual Core samples"
summary: "+-----------+----------------------+-------------------------------+ | Core | Flash Region | Comment | +===========+======================+===============================+ | CPU0 | Full flash memory | Primary core with bootloader | | | (including partition | access and application in | | | slot0_partition) | slot0_partition | …"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nxp/frdm_mcxn947/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxn947/doc/index.html#dual-core-samples"
license: "Apache-2.0"
mode: "V"
---

+-----------+----------------------+-------------------------------+
| Core      | Flash Region         | Comment                       |
+===========+======================+===============================+
| CPU0      | Full flash memory    | Primary core with bootloader  |
|           | (including partition | access and application in     |
|           | slot0_partition)     | slot0_partition               |
+-----------+----------------------+-------------------------------+
| CPU1      | slot1_partition only | Secondary core restricted to  |
|           |                      | its dedicated partition       |
+-----------+----------------------+-------------------------------+

+----------+------------------+-----------------------+
| Memory   | Region           | Comment               |
+==========+==================+=======================+
| srama    | RAM (320KB)      | CPU0 ram              |
+----------+------------------+-----------------------+
| sramg    | RAM (64KB)       | CPU1 ram              |
+----------+------------------+-----------------------+
| sramh    | RAM (32KB)       | Shared memory         |
+----------+------------------+-----------------------+


**Note:** The actual memory addresses are defined in the device tree and can be viewed in the generated map files after building. CPU0 accesses the full flash memory starting from its base address, while CPU1 is restricted to the slot1_partition region.


### Targets available


The default configuration file
`boards/nxp/frdm_mcxn947/frdm_mcxn947_mcxn947_cpu0_defconfig`
only enables the first core. CPU0 is the only target that can run standalone.

CPU1 does not work without CPU0 enabling it.

To enable CPU1, create System Build application project and enable the
second core with config `CONFIG_SECOND_CORE_MCUX`.

Please have a look at some already enabled samples:

- `samples/subsys/ipc/ipc_service/static_vrings`
- `samples/subsys/ipc/openamp`
- `samples/drivers/mbox`
- `samples/drivers/mbox_data`


### Connections and IOs


The MCX-N947 SoC has 6 gpio controllers and has pinmux registers which
can be used to configure the functionality of a pin.

+------------+-----------------+----------------------------+
| Name       | Function        | Usage                      |
+============+=================+============================+
| P0_PIO1_8  | UART            | UART RX cpu0               |
+------------+-----------------+----------------------------+
| P1_PIO1_9  | UART            | UART TX cpu0               |
+------------+-----------------+----------------------------+
| P4_PIO4_3  | UART            | UART RX cpu1               |
+------------+-----------------+----------------------------+
| P4_PIO4_2  | UART            | UART TX cpu1               |
+------------+-----------------+----------------------------+


### System Clock


The MCX-N947 SoC is configured to use PLL0 running at 150MHz as a source for
the system clock.


### Serial Port


The FRDM-MCXN947 SoC has 10 FLEXCOMM interfaces for serial communication.
Flexcomm 4 is configured as UART for the console.
