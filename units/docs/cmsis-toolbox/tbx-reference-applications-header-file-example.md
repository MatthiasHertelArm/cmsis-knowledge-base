---
id: "tbx-reference-applications-header-file-example"
type: "concept"
domain: "project"
title: "Reference Applications: Header File Example"
summary: "Two header files contain I/O configuration settings for the application program:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/ReferenceApplications.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/#header-file-example"
license: "Apache-2.0"
mode: "V"
---

Two header files contain I/O configuration settings for the application program:

- `CMSIS_target_header` defines the resources available by the evaluation board.
- `CMSIS_shield_header` extends this `CMSIS_target_header` with resources of a shield that is applied to an evaluation board.

Refer to [Header File Structure](#header-file-structure) for more information.

**`CMSIS_target_header`**

```c
#ifndef B_U585I_IOT02A_H_
#define B_U585I_IOT02A_H_

#include "stm32u5xx_hal.h"
#include "GPIO_STM32U5xx.h"
#include "Driver_I2C.h"
#include "Driver_SPI.h"
#include "Driver_USART.h"

// B-U585I-IOT02A Arduino Connector Pin Definitions
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

// CMSIS Driver instances on Arduino connector
#define ARDUINO_UNO_I2C     1
#define ARDUINO_UNO_SPI     1
#define ARDUINO_UNO_UART    3

// CMSIS Driver instances of Board peripherals
#define CMSIS_DRIVER_USBD   0  // instance of CMSIS-Driver USB Device

// CMSIS Drivers
extern ARM_DRIVER_I2C   Driver_I2C1;
extern ARM_DRIVER_SPI   Driver_SPI1;
extern ARM_DRIVER_USART Driver_USART1;
extern ARM_DRIVER_USART Driver_USART3;

#ifdef CMSIS_shield_header
#include CMSIS_shield_header
#endif

#endif /* B_U585I_IOT02A_H_ */
```

**`CMSIS_shield_header`**

```c
#ifndef _FRDM_STBC_AGM01_SHIELD_H_
#define _FRDM_STBC_AGM01_SHIELD_H_

// FRDM-STBC-AGM01 Shield Reset
#define RESET_GPIO              ARDUINO_UNO_D17

#define SHIELD_MULTIB   0
#define SHIELD_NONE     1
#define SHIELD_AGM01    2
#define SHIELD_AGM02    3
#define SHIELD_AGMP03   4
#define SHIELD_AGM04    5
#define THIS_SHIELD     SHIELD_AGM01

// Shield Setup (default configuration)
extern int32_t shield_setup (void);

#endif /* _FRDM_STBC_AGM01_SHIELD_H_ */
```
