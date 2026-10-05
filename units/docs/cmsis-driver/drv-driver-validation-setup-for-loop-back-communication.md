---
id: "drv-driver-validation-setup-for-loop-back-communication"
type: "concept"
domain: "drivers"
title: "Driver Validation: Setup for Loop Back Communication"
summary: "To perform loop back communication tests it is required to connect the input and the output of the peripherals as shown in this table:"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/validation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/validation.md#setup-for-loop-back-communication"
license: "Apache-2.0"
mode: "V"
---

To perform loop back communication tests it is required to connect the input and the output of the peripherals as shown in this table:

Peripheral       | Loop Back Configuration
:----------------|:----------------------------
Ethernet         | Connect TX+ (Pin 1) with RX+ (Pin 3), TX- (Pin 2) with RX- (Pin 6)
SPI              | Connect MISO to MOSI
USART            | Connect TX with RX

The following picture shows the necessary external loop back connections for the Keil MCBSTM32F400 evaluation board:

 - SPI: PB14 (SPI2_MISO) and PB15 (SPI2_MOSI)
 - USART: PB6 (USART1_TX) and PB7 (USART1_RX)
 - Ethernet: Pin 1 (TX+) and Pin 3 (RX+), Pin 2 (TX-) and Pin 6 (RX-)

(figure: Connections for Loop Back Communication Tests on Keil MCBSTM32F400)
