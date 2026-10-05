---
id: "dv-usart-server"
type: "concept"
domain: "drivers"
title: "USART Server"
summary: "The USART Server is an application used by the CMSIS-Driver Validation suite to test the physical operation of the USART driver."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_USART.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/usart_server.html"
license: "Apache-2.0"
mode: "V"
---

The **USART Server** is an application used by the CMSIS-Driver Validation suite to test the *physical* operation of
the USART driver.

It is available for the STMicroelectronics **STM32F429I-DISC1** board and as a template for **any board**
with available **Board Layer** and configured **CMSIS compliant USART driver**.

**Note:** STM32F429I-DISC1 was selected because its USART driver is stable and supports all required features.
**Note:** For running on the STM32F429I-DISC1 board, see usart_server_disc1.
**Note:** For running on other hardware, see usart_server_template.
