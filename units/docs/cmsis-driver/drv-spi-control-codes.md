---
id: "drv-spi-control-codes"
type: "concept"
domain: "drivers"
title: "SPI Control Codes"
summary: "Many parameters of the SPI driver are configured using the ARM_SPI_Control function."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
license: "Apache-2.0"
mode: "V"
---

Many parameters of the SPI driver are configured using the ARM_SPI_Control function.
 
The various SPI control codes define:
  
  - spi_mode_ctrls               specifies SPI mode
  - spi_frame_format_ctrls       defines the frame format
  - spi_data_bits_ctrls          defines the number of data bits
  - spi_bit_order_ctrls          defines the bit order
  - spi_slave_select_mode_ctrls  specifies slave select mode
  - spi_misc_ctrls               specifies additional miscellaneous controls

Refer to the ARM_SPI_Control function for further details.
