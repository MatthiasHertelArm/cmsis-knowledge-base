---
id: "tbx-reference-applications-connections"
type: "concept"
domain: "project"
title: "Reference Applications: Connections"
summary: "Connections are only used to identify compatible software layers. Since there are no strict rules for the connect Name, it is possible to extend it with additional namespacing, i.e., prefixing with ST to denote ST-specific interfaces."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/ReferenceApplications.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/#connections"
license: "Apache-2.0"
mode: "V"
---

[Connections](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/YML-Input-Format.md#connections) are only used to identify compatible software layers. Since there are no strict rules for the **`connect` Name**, it is possible to extend it with additional namespacing, i.e., prefixing with *ST_* to denote ST-specific interfaces.

There are also no strict rules on how the different software layers consume or provide the `connect` names.  However, guidelines will be developed once reference applications mature.

Currently, the following **`connect` names** are used.

`connect` name                                               | Value                  | Description
:------------------------------------------------------------|:-----------------------|:--------------------
.                                                            |.                       | **Arduino Shield Interface**
[ARDUINO_UNO_UART](#arduino_uno_uart)                        | -                      | CMSIS-Driver USART connecting to UART on Arduino pins D0..D1
[ARDUINO_UNO_SPI](#arduino_uno_spi)                          | -                      | CMSIS-Driver SPI connecting to SPI on Arduino pins D10..D13
[ARDUINO_UNO_I2C](#arduino_uno_i2c)                          | -                      | CMSIS-Driver I2C connecting to I2C on Arduino pins D20..D21
[ARDUINO_UNO_I2C-Alt](#arduino_uno_i2c)                      | -                      | CMSIS-Driver I2C connecting to I2C on Arduino pins D18..D19
[ARDUINO_UNO_D0 .. D21](#arduino_uno_dx)                     | -                      | CMSIS-Driver GPIO connecting to Arduino pins D0..D21
.                                                            |.                       | **CMSIS Driver and RTOS Interfaces**
[CMSIS_ETH](#cmsis_eth)                                      | -                      | CMSIS-Driver ETH connected to physical board connector
[CMSIS_MCI](#cmsis_mci)                                      | -                      | CMSIS-Driver MCI connected to physical board connector
[CMSIS_USB_Device](#cmsis_usb_device)                        | -                      | CMSIS-Driver USB Device connected to physical board connector
[CMSIS_USB_Host](#cmsis_usb_host)                            | -                      | CMSIS-Driver USB Host connected to physical board connector
[CMSIS_VIO](#cmsis_vio)                                      | -                      | CMSIS-Driver VIO interface for virtual I/O
CMSIS-RTOS2                                                  | -                      | CMSIS-RTOS2 compliant RTOS
.                                                            |.                       | **mikroBUS socket Interface**
[MIKROBUS_AN](#mikrobus_an_int_pwm)                          |-                       | CMSIS-Driver GPIO connecting to mikroBUS AN
[MIKROBUS_INT](#mikrobus_an_int_pwm)                         |-                       | CMSIS-Driver GPIO connecting to mikroBUS INT
[MIKROBUS_PWM](#mikrobus_an_int_pwm)                         |-                       | CMSIS-Driver GPIO connecting to mikroBUS PWM
[MIKROBUS_I2C](#mikrobus_i2c)                                |-                       | CMSIS-Driver I2C connecting to mikroBUS I2C
[MIKROBUS_SPI](#mikrobus_spi)                                |-                       | CMSIS-Driver SPI connecting to mikroBUS SPI
[MIKROBUS_UART](#mikrobus_uart)                              |-                       | CMSIS-Driver USART connecting to mikroBUS UART
.                                                            |.                       | **I/O Retargeting**
[STDERR](#stdio)                                             | -                      | Standard Error output
[STDIN](#stdio)                                              | -                      | Standard Input
[STDOUT](#stdio)                                             | -                      | Standard Output
.                                                            |.                       | **Memory allocation**
Heap                                                         | Heap Size              | Memory heap configuration

ToDo:

- what features of CMSIS-RTOS2 are typically used by board layers?
- more information about Heap. How is it configured? Which existing Reference Applications are using it?  FreeRTOS has its own heap management; is it really required?

### ARDUINO_UNO_UART

Connects to a [CMSIS-Driver USART Interface](https://arm-software.github.io/CMSIS_6/latest/Driver/group__usart__interface__gr.html) configured in asynchronous UART mode with no modem lines.

`CMSIS_target_header` contains the driver instance number with this definition:

```c
#define ARDUINO_UNO_UART    3     // CMSIS-Driver USART instance number
```

### ARDUINO_UNO_I2C

`ARDUINO_UNO_I2C` or `ARDUINO_UNO_I2C-Alt` connects to a [CMSIS-Driver I2C Interface](https://arm-software.github.io/CMSIS_6/latest/Driver/group__i2c__interface__gr.html) configured in controller mode.

`CMSIS_target_header` contains the driver instance number with this definition:

```c
#define ARDUINO_UNO_I2C    0     // CMSIS-Driver I2C instance number
```

### ARDUINO_UNO_SPI

Connects to a [CMSIS-Driver SPI Interface](https://arm-software.github.io/CMSIS_6/latest/Driver/group__spi__interface__gr.html) configured in controller mode and CPOL/CPHA frame format (no TI or Microwire).

The Target Select (SS) pin (typically on ARDUINO_UNO_D10) is not handled by CMSIS-Driver SPI interface; it is driven by the GPIO interface.

`CMSIS_target_header` contains the driver instance number with this definition:

```c
#define ARDUINO_UNO_SPI    1     // CMSIS-Driver SPI instance number
```

### ARDUINO_UNO_Dx

The `ARDUINO_UNO_D0` .. `ARDUINO_UNO_D21` connects to a [CMSIS-Driver GPIO Interface](https://arm-software.github.io/CMSIS_6/latest/Driver/group__gpio__interface__gr.html).

`CMSIS_target_header` contains the pin mapping to the physical driver.

```c
#define ARDUINO_UNO_D0  GPIO_PORTD(9U)  /* USART3: RX */
#define ARDUINO_UNO_D1  GPIO_PORTD(8U)  /* USART3: TX */
#define ARDUINO_UNO_D2  GPIO_PORTD(15U)
#define ARDUINO_UNO_D3  GPIO_PORTB(2U)
#define ARDUINO_UNO_D4  GPIO_PORTE(7U)
#define ARDUINO_UNO_D5  GPIO_PORTE(0U)
#define ARDUINO_UNO_D6  GPIO_PORTB(6U)
#define ARDUINO_UNO_D7  GPIO_PORTF(13U)
#define ARDUINO_UNO_D8  GPIO_PORTC(1U)
#define ARDUINO_UNO_D9  GPIO_PORTA(8U)
#define ARDUINO_UNO_D10 GPIO_PORTE(12U)
#define ARDUINO_UNO_D11 GPIO_PORTE(15U) /* SPI1: MOSI */
#define ARDUINO_UNO_D12 GPIO_PORTE(14U) /* SPI1: MISO */
#define ARDUINO_UNO_D13 GPIO_PORTE(13U) /* SPI1: SCK  */
#define ARDUINO_UNO_D14 GPIO_PORTC(0U)
#define ARDUINO_UNO_D15 GPIO_PORTC(2U)
#define ARDUINO_UNO_D16 GPIO_PORTC(4U)
#define ARDUINO_UNO_D17 GPIO_PORTC(5U)
#define ARDUINO_UNO_D18 GPIO_PORTA(7U)
#define ARDUINO_UNO_D19 GPIO_PORTB(0U)
#define ARDUINO_UNO_D20 GPIO_PORTB(8U)  /* I2C1: SDA  */
#define ARDUINO_UNO_D21 GPIO_PORTB(9U)  /* I2C1: SCL  */
```

### CMSIS_ETH

Connects to a [CMSIS-Driver Ethernet Interface](https://arm-software.github.io/CMSIS_6/latest/Driver/group__eth__interface__gr.html) that offers a physical Ethernet connector on the evaluation board.

`CMSIS_target_header` contains the pin mapping to the physical driver.

```c
#define CMSIS_DRIVER_ETH    0     // CMSIS-Driver Ethernet instance number
```

### CMSIS_MCI

Connects to a [CMSIS-Driver MCI Interface](https://arm-software.github.io/CMSIS_6/latest/Driver/group__mci__interface__gr.html) that offers a physical memory card connector on the evaluation board.

`CMSIS_target_header` contains the pin mapping to the physical driver.

```c
#define CMSIS_DRIVER_MCI    0     // CMSIS-Driver MCI instance number
```

### CMSIS_USB_Device

Connects to a [CMSIS-Driver USB Device Interface](https://arm-software.github.io/CMSIS_6/latest/Driver/group__usbd__interface__gr.html) that offers a physical USB connector on the evaluation board.

`CMSIS_target_header` contains the pin mapping to the physical driver.

```c
#define CMSIS_DRIVER_USBD   0     // CMSIS-Driver USB Device instance number
```

### CMSIS_USB_Host

Connects to a [CMSIS-Driver USB Host Interface](https://arm-software.github.io/CMSIS_6/latest/Driver/group__usbh__interface__gr.html) that offers a physical USB connector on the evaluation board.

`CMSIS_target_header` contains the pin mapping to the physical driver.

```c
#define CMSIS_DRIVER_USBH   0     // CMSIS-Driver USB Host instance number
```

### CMSIS_VIO

Connects to a [CMSIS-Driver VIO Interface](https://arm-software.github.io/CMSIS_6/latest/Driver/group__vio__interface__gr.html), a virtual I/O interface that connects on physical boards to LEDs and switches.

### MIKROBUS_AN/_INT/_PWM

The `MIKROBUS_AN, MIKROBUS_INT and MIKROBUS_PWM` connect to a [CMSIS-Driver GPIO Interface](https://arm-software.github.io/CMSIS_6/latest/Driver/group__gpio__interface__gr.html).

`CMSIS_target_header` contains the pin mapping to the physical driver.

```c
#define MIKROBUS_AN     GPIO_PORTD(0U)
#define MIKROBUS_INT    GPIO_PORTD(1U)
#define MIKROBUS_PWM    GPIO_PORTD(2U)
```

### MIKROBUS_I2C

Connects to a [CMSIS-Driver I2C Interface](https://arm-software.github.io/CMSIS_6/latest/Driver/group__i2c__interface__gr.html) configured in controller mode.

`CMSIS_target_header` contains the driver instance number with this definition:

```c
#define MIKROBUS_I2C        0     // CMSIS-Driver I2C instance number
```

### MIKROBUS_SPI

Connects to a [CMSIS-Driver SPI Interface](https://arm-software.github.io/CMSIS_6/latest/Driver/group__spi__interface__gr.html) configured in controller mode and CPOL/CPHA frame format (no TI or Microwire).

The Chip Select (CS) pin may be handled by CMSIS-Driver SPI interface or driven by the GPIO interface.

`CMSIS_target_header` contains the driver instance number with this definition:

```c
#define MIKROBUS_SPI        0     // CMSIS-Driver SPI instance number
```

### MIKROBUS_UART

Connects to a [CMSIS-Driver USART Interface](https://arm-software.github.io/CMSIS_6/latest/Driver/group__usart__interface__gr.html) configured in asynchronous UART mode with no modem lines.

`CMSIS_target_header` contains the driver instance number with this definition:

```c
#define MIKROBUS_UART       0     // CMSIS-Driver USART instance number
```

### STDIO

The `STDIN`, `STDOUT`, and `STDERR` describe the I/O redirection via the [CMSIS-Compiler](https://arm-software.github.io/CMSIS-Compiler/main/index.html) software component. Typically, the redirect is to a UART dedicated to debugging.
