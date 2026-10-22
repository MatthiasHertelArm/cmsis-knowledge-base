---
id: "zepb-stm32n6570-dk-hardware"
type: "concept"
domain: "bring-up"
title: "stm32n6570_dk: Hardware"
summary: "STM32N6570-DK features a CSI camera module with a high-resolution 5‑Mpx CMOS RGB image sensor. This camera outputs images in RAW Bayer format which require signal processing to be displayed with real life colors."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/st/stm32n6570_dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/stm32n6570_dk/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

- STM32N657X0H3Q Arm® Cortex®‑M55‑based microcontroller featuring ST Neural-ART Accelerator™,
  H264 encoder, NeoChrom 2.5D GPU, and 4.2 Mbytes of contiguous SRAM, in a VFBGA264 package
- 5" LCD module with capacitive touch panel
- USB Type-C® with USB 2.0 HS interface, dual‑role‑power (DRP)
- USB Type-A with USB 2.0 HS interface, host, 0.5 A max
- 1‑Gbit Ethernet with TSN (time-sensitive networking) compliant with IEEE‑802.3‑2002
- SAI audio codec
- One MEMS digital microphone
- 1‑Gbit Octo‑SPI flash memory
- 256-Mbit Hexadeca‑SPI PSRAM
- Two user LEDs
- User, tamper, and reset push-buttons
- Board connectors:

  - USB Type-C®
  - USB Type-A
  - Ethernet RJ45
  - Camera module
  - microSD™ card
  - LCD
  - Stereo headset jack including analog microphone input
  - Audio MEMS daughterboard expansion connector
  - ARDUINO® Uno R3 expansion connector
  - STMod+ expansion connector

- On-board STLINK-V3EC debugger/programmer with USB re-enumeration capability:
  Virtual COM port, and debug port

For more details, please refer to:

* STM32N6570_DK website
* STM32N657X0 on www.st.com
* STM32N657 reference manual


### Supported Features



### Video


STM32N6570-DK features a CSI camera module with a high-resolution 5‑Mpx CMOS RGB image sensor.
This camera outputs images in RAW Bayer format which require signal processing to be displayed with
real life colors. This Image Signal Processing could be done with a dedicated STM32 ISP module.


### NPU


STM32N6570-DK also embeds the ST Neural-ART Accelerator™ as NPU engineered for power-efficient edge
AI applications, such as the Zephyr computer vision application which is available as a separate
Zephyr application.


### Ethernet


STM32N6570-DK features a 1-Gbit Ethernet interface connected to an external PHY via RGMII.

An area of the on-chip OTP (One-Time Programmable) memory is dedicated to holding
Ethernet MAC addresses. This area is not programmed during manufacturing and reads
as all zeroes; it must be programmed in the field using STM32CubeProgrammer.

To use the OTP MAC address `MAC_ADDR1` in your application, add the following overlay:

```dts

&mac {
    nvmem-cells = <&mac_address0>;
    nvmem-cell-names = "mac-address";
};
```

**Warning:** Ethernet will not work with this overlay if the on-chip OTP has not been programmed, because the unprogrammed OTP value (all zeroes) would be read and used as MAC address, but 00:00:00:00:00:00 is not a valid MAC address.

However, to allow running Zephyr net related samples without programming
irreversibly your device, by default, the STM32 Ethernet driver creates a
locally administered MAC address from the device unique ID.


### STM32 OEMuROT integration


STM32CubeN6 provides an external secure bootloader called STM32 OEMuROT
that takes advantage of the secure features of the STM32N657X0H3Q
microcontroller. Refer to the OEMuRoT for STM32N6 wiki article for details
on this bootloader.

Integration of this bootloader in the Zephyr build environment is available
in the external STM32 OEMxROT module.


### USB


The USB pin assignments on the STM32N657XX microcontroller are immutable. This means that the specific
pins designated for USB functionality are fixed and cannot be changed or reassigned to other functions,
ensuring consistent and reliable USB communication.


### USB PIN (IOs)


+------------------+--------------------------------------+
| Name             | Description                          |
+==================+======================================+
| OTG1_HSDM        | USB OTG1 High-Speed Data- (negative) |
+------------------+--------------------------------------+
| OTG1_HSDP        | USB OTG1 High-Speed Data+ (positive) |
+------------------+--------------------------------------+
| OTG1_ID          | USB OTG1 ID Pin                      |
+------------------+--------------------------------------+
| OTG1_TXRTUNE     | USB OTG1 Transmit Retune             |
+------------------+--------------------------------------+
| OTG2_HSDM        | USB OTG2 High-Speed Data- (negative) |
+------------------+--------------------------------------+
| OTG2_HSDP        | USB OTG2 High-Speed Data+ (positive) |
+------------------+--------------------------------------+
| OTG2_ID          | USB OTG2 ID Pin                      |
+------------------+--------------------------------------+
| OTG2_TXRTUNE     | USB OTG2 Transmit Retune             |
+------------------+--------------------------------------+


### Connections and IOs


STM32N6570_DK Board has 12 GPIO controllers. These controllers are responsible
for pin muxing, input/output, pull-up, etc.

For more details please refer to STM32N6570_DK User Manual.


#### Default Zephyr Peripheral Mapping:


- ADC1_INP10 : PA9
- ADC1_INP11 : PA10
- FDCAN1_TX : PH2
- FDCAN1_RX : PD0
- I2C1_SCL : PH9
- I2C1_SDA : PC1
- I2C4_SCL : PE13
- I2C4_SDA : PE14
- LD1 : PO1
- LD2 : PG10
- SDMMC2_CK : PC2
- SDMMC2_CMD : PC3
- SDMMC2_D0 : PC4
- SDMMC2_D1 : PC5
- SDMMC2_D2 : PC0
- SDMMC2_D3 : PE4
- SPI5_SCK : PE15
- SPI5_MOSI : PG2
- SPI5_MISO : PH8
- SPI5_NSS : PA3
- USART_1_TX : PE5
- USART_1_RX : PE6
- USART_2_TX : PD5
- USART_2_RX : PF6
- XSPI1_NCS1 : PO0
- XSPI1_DQS0 : PO2
- XSPI1_DQS1 : PO3
- XSPI1_CLK : PO4
- XSPI1_IO0 : PP0
- XSPI1_IO1 : PP1
- XSPI1_IO2 : PP2
- XSPI1_IO3 : PP3
- XSPI1_IO4 : PP4
- XSPI1_IO5 : PP5
- XSPI1_IO6 : PP6
- XSPI1_IO7 : PP7
- XSPI1_IO8 : PP8
- XSPI1_IO9 : PP9
- XSPI1_IO10 : PP10
- XSPI1_IO11 : PP11
- XSPI1_IO12 : PP12
- XSPI1_IO13 : PP13
- XSPI1_IO14 : PP14
- XSPI1_IO15 : PP15
- XSPI2_NCS1 : PN1
- XSPI2_DQS0 : PN0
- XSPI2_CLK : PN6
- XSPI2_IO0 : PN2
- XSPI2_IO1 : PN3
- XSPI2_IO2 : PN4
- XSPI2_IO3 : PN5
- XSPI2_IO4 : PN8
- XSPI2_IO5 : PN9
- XSPI2_IO6 : PN10
- XSPI2_IO7 : PN11


#### System Clock


STM32N6570_DK System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
400MHz, driven by 64MHz high speed internal oscillator.


#### Serial Port


STM32N6570_DK board has 10 U(S)ARTs. The Zephyr console output is assigned to
USART1. Default settings are 115200 8N1.
