---
id: "drv-usart-interface"
type: "concept"
domain: "drivers"
title: "USART Interface"
summary: "Driver API for Universal Synchronous Asynchronous Receiver/Transmitter (%Driver_USART.h)"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
license: "Apache-2.0"
mode: "V"
---

Driver API for Universal Synchronous Asynchronous Receiver/Transmitter (%Driver_USART.h)
 
The **Universal Synchronous Asynchronous Receiver/Transmitter** (USART) implements a synchronous and asynchronous serial bus for exchanging data. 
When only asynchronous mode is supported it is called Universal Asynchronous Receiver/Transmitter (UART).  
Almost all microcontrollers have a serial interface (UART/USART peripheral). A UART is a simple device to send data to a PC
via a terminal emulation program (Hyperterm, TeraTerm) or to another microcontroller.
A UART takes bytes of data and transmits the individual bits in a sequential mode. At the destination, 
a second UART reassembles the bits into complete bytes. Each UART contains a shift register for converting between serial and parallel transmission forms. 
Wikipedia offers more information about  
the **Universal asynchronous receiver/transmitter**.


**USART API**

The following header files define the Application Programming Interface (API) for the USART interface:
  - **%Driver_USART.h** : Driver API for Universal Synchronous Asynchronous Receiver/Transmitter

The driver implementation is a typical part of the Device Family Pack (DFP) that supports the 
peripherals of the microcontroller family.


**Driver Functions**

The driver functions are published in the access struct as explained in DriverFunctions
  - ARM_DRIVER_USART : access struct for USART driver functions

  
**Example Code**

The following example code shows the usage of the USART interface for asynchronous communication.

\include USART_Demo.c
