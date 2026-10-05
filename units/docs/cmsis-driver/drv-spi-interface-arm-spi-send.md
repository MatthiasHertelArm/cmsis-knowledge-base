---
id: "drv-spi-interface-arm-spi-send"
type: "concept"
domain: "drivers"
title: "SPI Interface: ARM_SPI_Send"
summary: "This function ARM_SPI_Send is used to send data to the SPI transmitter (received data is ignored)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_SPI_Send (const void *data, uint32_t num)
```

 
This function **ARM_SPI_Send** is used to send data to the SPI transmitter (received data is ignored).

The parameter **data** specifies the data buffer. \n
The parameter **num** specifies the number of items to send. \n
The item size is defined by the data type, which depends on the configured number of data bits.

Data type is:
 - **uint8_t** when configured for 1..8 data bits
 - **uint16_t** when configured for 9..16 data bits
 - **uint32_t** when configured for 17..32 data bits
 
Calling the function **ARM_SPI_Send** only starts the send operation.
When in slave mode, the operation is only registered and started when the master starts the transfer.
The function is non-blocking and returns as soon as the driver has started the operation 
(driver typically configures DMA or the interrupt system for continuous transfer).
During the operation it is not allowed to call this function or any other data transfer function again. 
Also the data buffer must stay allocated and the contents of unsent data must not be modified.
When send operation is completed (requested number of items sent), the ARM_SPI_EVENT_TRANSFER_COMPLETE event is generated.
Progress of send operation can also be monitored by reading the number of items already sent by calling ARM_SPI_GetDataCount. 

Status of the transmitter can also be monitored by calling the ARM_SPI_GetStatus and checking the **busy** data field,
which indicates if transmission is still in progress or pending. 

When in master mode and configured to monitor slave select and the slave select gets deactivated during transfer,
then the SPI mode changes to inactive and the ARM_SPI_EVENT_MODE_FAULT event is generated (instead of ARM_SPI_EVENT_TRANSFER_COMPLETE).

When in slave mode but send/receive/transfer operation is not started and data is sent/requested by the master, 
then the ARM_SPI_EVENT_DATA_LOST event is generated. 

Send operation can be aborted by calling ARM_SPI_Control with ARM_SPI_ABORT_TRANSFER as the control parameter.
*************************************************************************************************************************
