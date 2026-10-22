---
id: "zepb-kit-xmc72-evk-hardware"
type: "concept"
domain: "bring-up"
title: "kit_xmc72_evk: Hardware"
summary: "For more information about the XMC 7200 and KIT_XMC72_EVK:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/infineon/kit_xmc72_evk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/infineon/kit_xmc72_evk/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

- **SoC:** XMC 7200 (XMC7200D_E272K8384)
- **CPU:** Arm® Cortex®-M7 (×2) at 350 MHz + Arm® Cortex®-M0+ at 100 MHz
- **Package:** 272-pin BGA
- **Flash:** 8 MB
- **SRAM:** 1 MB
- **Connectivity:** Gigabit Ethernet, CAN FD, M.2 WiFi/BT
- **Peripherals:** 512-Mb QSPI NOR flash, HYPERBUS™ memory interface (not supported)
- **Debug:** Onboard KitProg3 (SWD + USB-UART + USB-I2C)
- **Power:** Selectable 3.3V or 5.0V, USB or 12V DC adapter
- **Connector:** Micro-B USB for programming and power
- **Expansion:** Arduino-compatible headers, Digilent dual PMOD SMIF header
- **User I/O:** Three user LEDs, two user buttons, potentiometer


**Note:** Some boards with serial numbers starting "2339HTX01" use S25HL512T flash instead of S25FL512S. Check the board serial number if you experience flash compatibility issues.

For more information about the XMC 7200 and KIT_XMC72_EVK:

- XMC7200D SoC Website
- KIT_XMC72_EVK Board Website


### Kit Contents


- XMC 7200 Evaluation Kit board
- USB Type-A to Micro-B cable
- 12V/3A DC power adapter
- Six jumper wires
- Quick start guide


### Supported Features



### Connections and IOs



#### LEDs


+---------+--------------------+
| Name    | GPIO Pin           |
+=========+====================+
| LED0    | P16.1 (active low) |
+---------+--------------------+
| LED1    | P16.2 (active low) |
+---------+--------------------+
| LED2    | P16.3 (active low) |
+---------+--------------------+


#### Push Buttons


+---------+----------------------------+
| Name    | GPIO Pin                   |
+=========+============================+
| SW1     | P21.4 (active low, pullup) |
+---------+----------------------------+
| SW2     | P17.3 (active low, pullup) |
+---------+----------------------------+


#### Default Zephyr Peripheral Mapping


+-----------+-----------------+----------------------------+
| Pin       | Function        | Usage                      |
+===========+=================+============================+
| P13.1     | SCB3 UART TX    | Console TX                 |
+-----------+-----------------+----------------------------+
| P13.0     | SCB3 UART RX    | Console RX                 |
+-----------+-----------------+----------------------------+
| P13.2     | SCB3 UART RTS   | Console RTS                |
+-----------+-----------------+----------------------------+
| P13.3     | SCB3 UART CTS   | Console CTS                |
+-----------+-----------------+----------------------------+
| P16.1     | GPIO            | LED0                       |
+-----------+-----------------+----------------------------+
| P16.2     | GPIO            | LED1                       |
+-----------+-----------------+----------------------------+
| P16.3     | GPIO            | LED2                       |
+-----------+-----------------+----------------------------+
| P21.4     | GPIO            | Button SW1                 |
+-----------+-----------------+----------------------------+
| P17.3     | GPIO            | Button SW2                 |
+-----------+-----------------+----------------------------+


### System Clock


The XMC 7200 uses an External Crystal Oscillator (ECO) as the clock source.
The clock path is:

- **FLL**: ECO → 100 MHz
- **PLL**: ECO → 100 MHz
- **CLK_HF0**: 200 MHz (system clock)
- **CLK_HF1**: 350 MHz (high-performance peripherals)


### Serial Port


The XMC 7200 has multiple SCB (Serial Communication Block) interfaces. The
Zephyr console output is assigned to **SCB3** (`uart3`), which is routed
through the KitProg3 USB-UART bridge.

Default communication settings are **115200 8N1**.
