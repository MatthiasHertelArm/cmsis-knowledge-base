---
id: "dv-setup-step-8-setup-the-required-hardware"
type: "concept"
domain: "drivers"
title: "Setup: Step 8: Setup the required hardware"
summary: "For the interfaces that support loopback testing: Ethernet, USART and SPI, connect the following pins on your target hardware together (refer to the hardware schematics):"
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DriverValidation.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/setup.html"
license: "Apache-2.0"
mode: "V"
---

For the interfaces that support loopback testing: Ethernet, USART and SPI,
connect the following pins on your target hardware together (refer to the hardware schematics):

- **Ethernet**: **RX+** and **TX+**, **RX-** and **TX-**
- **USART**:    **RX** and **TX**
- **SPI**:      **MOSI** and **MISO**

For the interfaces that support testing with dedicated server: WiFi, SPI and USART
connect the related hardware as required by the related server:

- **USART**: **Tx**, **Rx**, **GND** and optionally CLK, CTS, RTS, DCD and RI lines as described in usart_server
- **SPI**:   **MOSI**, **MISO**, **SCLK**, **SS**, **GND** to the same lines on the spi_server
- **WiFi**:  WiFi module has to be in close proximity to the Access Point which is in the same network as the required wifi_sock_setup
