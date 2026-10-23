---
id: "drv-usart-events"
type: "concept"
domain: "drivers"
title: "USART Events"
summary: "The USART driver generates call back events that are notified via the function ARM_USART_SignalEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
license: "Apache-2.0"
mode: "V"
---

The USART driver generates call back events that are notified via the function ARM_USART_SignalEvent.
 
This section provides the event values for the ARM_USART_SignalEvent callback function.

The following call back notification events are generated:

### ARM_USART_EVENT_SEND_COMPLETE

```c
ARM_USART_EVENT_SEND_COMPLETE
```


### ARM_USART_EVENT_RECEIVE_COMPLETE

```c
ARM_USART_EVENT_RECEIVE_COMPLETE
```


### ARM_USART_EVENT_TRANSFER_COMPLETE

```c
ARM_USART_EVENT_TRANSFER_COMPLETE
```


### ARM_USART_EVENT_TX_COMPLETE

```c
ARM_USART_EVENT_TX_COMPLETE
```


### ARM_USART_EVENT_TX_UNDERFLOW

```c
ARM_USART_EVENT_TX_UNDERFLOW
```


### ARM_USART_EVENT_RX_OVERFLOW

```c
ARM_USART_EVENT_RX_OVERFLOW
```


### ARM_USART_EVENT_RX_TIMEOUT

```c
ARM_USART_EVENT_RX_TIMEOUT
```


### ARM_USART_EVENT_RX_BREAK

```c
ARM_USART_EVENT_RX_BREAK
```


### ARM_USART_EVENT_RX_FRAMING_ERROR

```c
ARM_USART_EVENT_RX_FRAMING_ERROR
```


### ARM_USART_EVENT_RX_PARITY_ERROR

```c
ARM_USART_EVENT_RX_PARITY_ERROR
```


### ARM_USART_EVENT_CTS

```c
ARM_USART_EVENT_CTS
```


### ARM_USART_EVENT_DSR

```c
ARM_USART_EVENT_DSR
```


### ARM_USART_EVENT_DCD

```c
ARM_USART_EVENT_DCD
```


### ARM_USART_EVENT_RI

```c
ARM_USART_EVENT_RI
```
