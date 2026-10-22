---
id: "drv-usart-interface-arm-usart-receive"
type: "concept"
domain: "drivers"
title: "USART Interface: ARM_USART_Receive"
summary: "This functions ARM_USART_Receive is used in asynchronous mode to receive data from the USART receiver. It can also be used in synchronous mode when receiving data only (transmits the default value as specified by ARM_USART_Control with ARM_USART_SET_DEFAULT_TX_VALUE as control parameter)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USART_Receive (void *data, uint32_t num)
```


This functions **ARM_USART_Receive** is used in asynchronous mode to receive data from the USART receiver.
It can also be used in synchronous mode when receiving data only (transmits the default value as specified by ARM_USART_Control with ARM_USART_SET_DEFAULT_TX_VALUE as control parameter). 

Receiver needs to be enabled by calling ARM_USART_Control with ARM_USART_CONTROL_RX as the control parameter and `1` as argument. 

The function parameters specify the buffer for data and the number of items to receive.
The item size is defined by the data type which depends on the configured number of data bits.

Data type is:
 - **uint8_t** when configured for 5..8 data bits
 - **uint16_t** when configured for 9 data bits
 
Calling the function **ARM_USART_Receive** only starts the receive operation.
The function is non-blocking and returns as soon as the driver has started the operation (driver typically configures DMA or the interrupt system for continuous transfer).
When in synchronous slave mode the operation is only registered and started when the master starts the transfer.
During the operation it is not allowed to call this function again or any other data transfer function when in synchronous mode. Also the data buffer must stay allocated.
When receive operation is completed (requested number of items received) the ARM_USART_EVENT_RECEIVE_COMPLETE event is generated.
Progress of receive operation can also be monitored by reading the number of items already received by calling ARM_USART_GetRxCount. 

Status of the receiver can be monitored by calling the ARM_USART_GetStatus and checking the **rx_busy** flag
which indicates if reception is still in progress. 

During reception the following events can be generated (in asynchronous mode):
 - ARM_USART_EVENT_RX_TIMEOUT : Receive timeout between consecutive characters detected (optional)
 - ARM_USART_EVENT_RX_BREAK : Break detected (Framing error is not generated for Break condition)
 - ARM_USART_EVENT_RX_FRAMING_ERROR : Framing error detected
 - ARM_USART_EVENT_RX_PARITY_ERROR : Parity error detected
 - ARM_USART_EVENT_RX_OVERFLOW : Data overflow detected (also in synchronous slave mode)

ARM_USART_EVENT_RX_OVERFLOW event is also generated when receiver is enabled but data is lost because 
receive operation in asynchronous mode or receive/send/transfer operation in synchronous slave mode has not been started.

Receive operation can be aborted by calling ARM_USART_Control with ARM_USART_ABORT_RECEIVE as the control parameter.
****************************************************************************************************************
