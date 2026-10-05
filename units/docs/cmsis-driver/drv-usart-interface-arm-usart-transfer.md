---
id: "drv-usart-interface-arm-usart-transfer"
type: "concept"
domain: "drivers"
title: "USART Interface: ARM_USART_Transfer"
summary: "This functions ARMUSARTTransfer is used in synchronous mode to transfer data via USART. It synchronously sends data to the USART transmitter and receives data from the USART receiver."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USART_Transfer (const void *data_out, void *data_in, uint32_t num)
```


This functions **ARM_USART_Transfer** is used in synchronous mode to transfer data via USART. It synchronously sends data to the USART transmitter and receives data from the USART receiver. 

Transmitter needs to be enabled by calling ARM_USART_Control with ARM_USART_CONTROL_TX as the control parameter and `1` as argument. 
Receiver needs to be enabled by calling ARM_USART_Control with ARM_USART_CONTROL_RX as the control parameter and `1` as argument. 

The function parameters specify the buffer with data to send, the buffer for data to receive and the number of items to transfer.
The item size is defined by the data type which depends on the configured number of data bits.

Data type is:
 - **uint8_t** when configured for 5..8 data bits
 - **uint16_t** when configured for 9 data bits
 
Calling the function **ARM_USART_Transfer** only starts the transfer operation.
The function is non-blocking and returns as soon as the driver has started the operation (driver typically configures DMA or the interrupt system for continuous transfer).
When in synchronous slave mode the operation is only registered and started when the master starts the transfer.
During the operation it is not allowed to call this function or any other data transfer function again. Also the data buffers must stay allocated and the contents of unsent data must not be modified.
When transfer operation is completed (requested number of items transferred) the ARM_USART_EVENT_TRANSFER_COMPLETE event is generated.
Progress of transfer operation can also be monitored by reading the number of items already transferred by calling ARM_USART_GetTxCount or ARM_USART_GetRxCount. 

Status of the transmitter or receiver can be monitored by calling the ARM_USART_GetStatus and checking the **tx_busy** or **rx_busy** flag. 

When in synchronous slave mode also the following events can be generated:
 - ARM_USART_EVENT_TX_UNDERFLOW : transmitter is enabled but transfer operation is not started and data is requested by the master
 - ARM_USART_EVENT_RX_OVERFLOW : data lost during transfer or because receiver is enabled but transfer operation has not been started

Transfer operation can also be aborted by calling ARM_USART_Control with ARM_USART_ABORT_TRANSFER as the control parameter.
****************************************************************************************************************
