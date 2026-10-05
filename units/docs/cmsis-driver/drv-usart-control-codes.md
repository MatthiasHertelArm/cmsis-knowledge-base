---
id: "drv-usart-control-codes"
type: "concept"
domain: "drivers"
title: "USART Control Codes"
summary: "Many parameters of the USART driver are configured using the ARM_USART_Control function."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
license: "Apache-2.0"
mode: "V"
---

Many parameters of the USART driver are configured using the ARM_USART_Control function.

The various USART control codes define:
  - usart_mode_control specifies USART mode
  - usart_data_bits defines the number of data bits
  - usart_parity_bit defines the parity bit
  - usart_stop_bits defines the number of stop bits
  - usart_flow_control specifies RTS/CTS flow control
  - usart_clock_polarity defines the clock polarity for the synchronous mode
  - usart_clock_phase defines the clock phase for the synchronous mode
  - usart_misc_control specifies additional miscellaneous controls

Refer to the ARM_USART_Control function for further details.
