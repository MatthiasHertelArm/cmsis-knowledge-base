---
id: "core-peripheral-access"
type: "concept"
domain: "core"
title: "Peripheral Access"
summary: "Naming conventions and optional features for accessing peripherals."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_peripheral.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_peripheral.txt"
license: "Apache-2.0"
mode: "V"
---

Naming conventions and optional features for accessing peripherals.

	
The section below describes the naming conventions, requirements, and optional features for accessing device specific peripherals.
Most of the rules also apply to the core peripherals.  The device_h_pg contains typically these definition and also includes
the core specific header files.

\ifnot FuSaRTS
The definitions for peripheral_gr can be generated using the **CMSIS-SVD** System View Description for Peripherals.
Refer to **SVDConv.exe** for more information.
\endif
	
Each peripheral provides a data type definition with a name that is composed of:
  - an optional prefix **<_device abbreviation>__**
  - **<_peripheral name_>**
  - postfix **_Type** or **_TypeDef** to identify a type definition.

Examples:
  - **UART_TypeDef** for the peripheral **UART.**
  - **LPC_UART_TypeDef** for the device family **LPC** and the peripheral **UART.**

The data type definition uses standard C data types defined by the ANSI C header file `<stdint.h>`.
 
 - IO Type Qualifiers are used to specify the access to peripheral variables.
   IO Type Qualifier  | Type            | Description
   :------------------|:----------------|:------------
   **__IM**            | Struct member   | Defines 'read only' permissions
   **__OM**            | Struct member   | Defines 'write only' permissions
   **__IOM**           | Struct member   | Defines 'read / write' permissions
   **__I**             | Scalar variable | Defines 'read only' permissions
   **__O**             | Scalar variable | Defines 'write only' permissions
   **__IO**            | Scalar variable | Defines 'read / write' permissions
   
**Note:** 
**__IM,** **__OM,** **__IOM** are added in CMSIS-Core V4.20 to enhance support for C++. Prior version used **__I,** **__O,** **__IO** also for struct member definitions.

The typedef **\<_device abbreviation_\>_UART_TypeDef** shown below defines the generic register layout for all UART channels in a device.

```
typedef struct
{
  union {
  __IM  uint8_t  RBR;                 /* Offset: 0x000 (R/ )  Receiver Buffer Register            */
  __OM  uint8_t  THR;                 /* Offset: 0x000 ( /W)  Transmit Holding Register           */
  __IOM uint8_t  DLL;                 /* Offset: 0x000 (R/W)  Divisor Latch LSB                   */
        uint32_t RESERVED0;
  };
  union {
  __IOM uint8_t  DLM;                 /* Offset: 0x004 (R/W)  Divisor Latch MSB                   */
  __IOM uint32_t IER;                 /* Offset: 0x004 (R/W)  Interrupt Enable Register           */
  };
  union {
  __IM  uint32_t IIR;                 /* Offset: 0x008 (R/ )  Interrupt ID Register               */
  __OM  uint8_t  FCR;                 /* Offset: 0x008 ( /W)  FIFO Control Register               */
  };
  __IOM uint8_t  LCR;                 /* Offset: 0x00C (R/W)  Line Control Register               */
        uint8_t  RESERVED1[7];
  __IM  uint8_t  LSR;                 /* Offset: 0x014 (R/ )  Line Status Register                */
        uint8_t  RESERVED2[7];
  __IOM uint8_t  SCR;                 /* Offset: 0x01C (R/W)  Scratch Pad Register                */
        uint8_t  RESERVED3[3];
  __IOM uint32_t ACR;                 /* Offset: 0x020 (R/W)  Autobaud Control Register           */
  __IOM uint8_t  ICR;                 /* Offset: 0x024 (R/W)  IrDA Control Register               */
        uint8_t  RESERVED4[3];
  __IOM uint8_t  FDR;                 /* Offset: 0x028 (R/W)  Fractional Divider Register         */
        uint8_t  RESERVED5[7];
  __IOM uint8_t  TER;                 /* Offset: 0x030 (R/W)  Transmit Enable Register            */
        uint8_t  RESERVED6[39];
  __IM  uint8_t  FIFOLVL;             /* Offset: 0x058 (R/ )  FIFO Level Register                 */
} LPC_UART_TypeDef;
```

To access the registers of the UART defined above, pointers to this register structure are defined.
If more instances of a peripheral exist, the variables have a postfix (digit or letter) that identifies the peripheral.

**Example:**
In this example **LPC_UART2** and **LPC_UART3** are two pointers to UARTs defined with above register structure.
\n
```
#define LPC_UART2             ((LPC_UART_TypeDef      *) LPC_UART2_BASE    )
#define LPC_UART3             ((LPC_UART_TypeDef      *) LPC_UART3_BASE    )
```

**Note:** 
 - The prefix **LPC** is optional.
 
The registers in the various UARTs can now be referred in the user code as shown below:\n
```
 val = LPC_UART2->DR   // is the data register of UART1.
```
