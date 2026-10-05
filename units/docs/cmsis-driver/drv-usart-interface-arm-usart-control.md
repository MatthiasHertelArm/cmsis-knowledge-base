---
id: "drv-usart-interface-arm-usart-control"
type: "concept"
domain: "drivers"
title: "USART Interface: ARM_USART_Control"
summary: "The function ARMUSARTControl control the USART interface settings and execute various operations."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USART_Control (uint32_t control, uint32_t arg)
```


The function **ARM_USART_Control** control the USART interface settings and execute various operations.

The parameter **control** sets the operation and is explained in the table below.
Values from different categories can be ORed with the exception of Miscellaneous Operations.

The parameter **arg** provides, depending on the operation, additional information, for example the baudrate.

The table lists the available **control** operations.



| Parameter **control**            |    Bit                  |       Category  |  Description  | 

| ARM_USART_MODE_ASYNCHRONOUS |           0..7     |       Operation Mode   | Set to asynchronous UART mode. **arg** specifies baudrate. | 

| ARM_USART_MODE_SYNCHRONOUS_MASTER |    Set to synchronous master mode with clock signal generation. **arg** specifies baudrate. | 

| ARM_USART_MODE_SYNCHRONOUS_SLAVE |     Set to synchronous slave mode with external clock signal. | 

| ARM_USART_MODE_SINGLE_WIRE |           Set to single-wire (half-duplex) mode. **arg** specifies baudrate. | 

| ARM_USART_MODE_IRDA |                  Set to Infra-red data mode. **arg** specifies baudrate. | 

| ARM_USART_MODE_SMART_CARD |            Set to Smart Card mode. **arg** specifies baudrate. | 

| ARM_USART_DATA_BITS_5 |          8..11     |       Data Bits   | Set to `5` data bits | 

| ARM_USART_DATA_BITS_6 |            Set to `6` data bits | 

| ARM_USART_DATA_BITS_7 |            Set to `7` data bits | 

| ARM_USART_DATA_BITS_8 |            Set to `8` data bits (default) | 

| ARM_USART_DATA_BITS_9 |            Set to `9` data bits | 

| ARM_USART_PARITY_EVEN |          12..13  |    Parity Bit   | Set to Even Parity | 

| ARM_USART_PARITY_NONE |            Set to No Parity (default) | 

| ARM_USART_PARITY_ODD |             Set to Odd Parity | 

| ARM_USART_STOP_BITS_1 |          14..15  |    Stop Bit   | Set to `1` Stop bit (default) | 

| ARM_USART_STOP_BITS_2 |            Set to `2` Stop bits | 

| ARM_USART_STOP_BITS_1_5 |          Set to `1.5` Stop bits | 

| ARM_USART_STOP_BITS_0_5 |          Set to `0.5` Stop bits | 

| ARM_USART_FLOW_CONTROL_NONE |    16..17  |    Flow Control   | No flow control signal (default) | 

| ARM_USART_FLOW_CONTROL_CTS |       Set to use the CTS flow control signal | 
 
| ARM_USART_FLOW_CONTROL_RTS |       Set to use the RTS flow control signal | 

| ARM_USART_FLOW_CONTROL_RTS_CTS |   Set to use the RTS and CTS flow control signal | 
 
| ARM_USART_CPOL0 |                18      |    Clock Polarity   | CPOL=`0` (default) : data are captured on rising edge (low->high transition) | 
 
| ARM_USART_CPOL1 |                  CPOL=`1` : data are captured on falling edge (high->low transition) | 
 
| ARM_USART_CPHA0 |                19      |    Clock Phase   | CPHA=`0` (default) : sample on first (leading) edge | 

| ARM_USART_CPHA1 |                  CPHA=`1` : sample on second (trailing) edge | 

| ARM_USART_ABORT_RECEIVE |        0..19   |     Miscellaneous Operations 
(cannot be ORed)   | Abort receive operation (see also: ARM_USART_Receive) | 

|  ARM_USART_ABORT_SEND |                  Abort  send operation   (see also: ARM_USART_Send) | 

|  ARM_USART_ABORT_TRANSFER |              Abort transfer operation  (see also: ARM_USART_Transfer) | 

|  ARM_USART_CONTROL_BREAK |               Enable or disable continuous Break transmission; **arg** : `0=disabled; 1=enabled` | 
 
|  ARM_USART_CONTROL_RX |                  Enable or disable receiver; **arg** : `0=disabled; 1=enabled` (see also: ARM_USART_Receive; ARM_USART_Transfer) | 

|  ARM_USART_CONTROL_SMART_CARD_NACK |     Enable or disable Smart Card NACK generation; **arg** : `0=disabled; 1=enabled` | 
 
|  ARM_USART_CONTROL_TX |                  Enable or disable transmitter; **arg** : `0=disabled; 1=enabled` (see also: ARM_USART_Send; ARM_USART_Transfer) | 

|  ARM_USART_SET_DEFAULT_TX_VALUE |        Set the default transmit value (synchronous receive only); **arg** specifies the value. (see also: ARM_USART_Receive) | 

|  ARM_USART_SET_IRDA_PULSE |              Set the IrDA pulse value in `ns`; **arg** : `0=3/16 of bit period` | 

|  ARM_USART_SET_SMART_CARD_CLOCK |        Set the Smart Card Clock in `Hz`; **arg** : `0=Clock not set` | 

|  ARM_USART_SET_SMART_CARD_GUARD_TIME |   Set the Smart Card guard time; **arg** = number of bit periods | 



**Example**

```
  extern ARM_DRIVER_USART Driver_USART0;
  
  // configure to UART mode: 8 bits, no parity, 1 stop bit, no flow control, 9600 bps
  status = Driver_USART0.Control(ARM_USART_MODE_ASYNCHRONOUS | 
                                 ARM_USART_DATA_BITS_8 | 
                                 ARM_USART_PARITY_NONE | 
                                 ARM_USART_STOP_BITS_1 | 
                                 ARM_USART_FLOW_CONTROL_NONE, 9600);
 
  // identical with above settings (default settings removed)
  // configure to UART mode: 8 bits, no parity, 1 stop bit, flow control, 9600 bps
  status = Driver_USART0.Control(ARM_USART_MODE_ASYNCHRONOUS, 9600);
 
  // enable TX output
  status = Driver_USART0.Control(ARM_USART_CONTROL_TX, 1);
 
  // disable RX output
  status = Driver_USART0.Control(ARM_USART_CONTROL_RX, 0);
```
****************************************************************************************************************
