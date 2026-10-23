---
id: "drv-usart-interface-arm-usart-send"
type: "concept"
domain: "drivers"
title: "USART Interface: ARM_USART_Send"
summary: "This functions ARM_USART_Send is used in asynchronous mode to send data to the USART transmitter. It can also be used in synchronous mode when sending data only (received data is ignored)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USART_Send (const void *data, uint32_t num)
```


This functions **ARM_USART_Send** is used in asynchronous mode to send data to the USART transmitter.
It can also be used in synchronous mode when sending data only (received data is ignored). 

Transmitter needs to be enabled by calling ARM_USART_Control with ARM_USART_CONTROL_TX as the control parameter and `1` as argument. 

The function parameters specify the buffer with data and the number of items to send.
The item size is defined by the data type which depends on the configured number of data bits.

Data type is:
 - **uint8_t** when configured for 5..8 data bits
 - **uint16_t** when configured for 9 data bits
 
Calling the function **ARM_USART_Send** only starts the send operation.
The function is non-blocking and returns as soon as the driver has started the operation (driver typically configures DMA or the interrupt system for continuous transfer).
When in synchronous slave mode the operation is only registered and started when the master starts the transfer.
During the operation it is not allowed to call this function again or any other data transfer function when in synchronous mode. Also the data buffer must stay allocated and the contents of unsent data must not be modified.
When send operation is completed (requested number of items sent) the ARM_USART_EVENT_SEND_COMPLETE event is generated.
Progress of send operation can also be monitored by reading the number of items already sent by calling ARM_USART_GetTxCount. 

After send operation has completed there might still be some data left in the driver's hardware buffer which is still being transmitted.
When all data has been physically transmitted the ARM_USART_EVENT_TX_COMPLETE event is generated (if supported and reported by **event_tx_complete** in ARM_USART_CAPABILITIES).
At that point also the **tx_busy** data field in ARM_USART_STATUS is cleared.

Status of the transmitter can be monitored by calling the ARM_USART_GetStatus and checking the **tx_busy** flag
which indicates if transmission is still in progress. 

When in synchronous slave mode and transmitter is enabled but send/receive/transfer operation is not started and data is requested by the master then the ARM_USART_EVENT_TX_UNDERFLOW event is generated. 

Send operation can be aborted by calling ARM_USART_Control with ARM_USART_ABORT_SEND as the control parameter.
****************************************************************************************************************
