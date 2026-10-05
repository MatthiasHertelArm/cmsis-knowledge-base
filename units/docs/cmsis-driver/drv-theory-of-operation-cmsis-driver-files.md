---
id: "drv-theory-of-operation-cmsis-driver-files"
type: "concept"
domain: "drivers"
title: "Theory of Operation: CMSIS-Driver Files"
summary: "The API of each CMSIS-Driver peripheral is published in a corresponding header file in the directory .\\CMSIS\\Driver\\Include\\ It is recommended to include such header file in the implementation file of the CMSIS-Driver."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/operation.md#cmsis-driver-files"
license: "Apache-2.0"
mode: "V"
---

The API of each CMSIS-Driver peripheral is published in a corresponding header file in the directory `.\CMSIS\Driver\Include\` It is recommended to include such header file in the implementation file of the CMSIS-Driver.

Template files are available to simplify the development of a CMSIS-Driver. These are code skeletons that provide the structure of a CMSIS-Driver. They are available in the directory`.\CMSIS\Driver\DriverTemplates\`. You can also refer to working CMSIS-Driver Implementations to see how CMSIS-Drivers get implemented on real devices.

The table below summarizes the API header and template files for CMSIS-Driver interfaces, with links to GitHub and API references.


| Header File          | Template File            | API Reference
:----------------------|:-------------------------|:-----------------------
[Driver_Common.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_Common.h)| Not applicable | common_drv_gr
[Driver_CAN.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_CAN.h)      | [Driver_CAN.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_CAN.c) |can_interface_gr
[Driver_ETH.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_ETH.h)      | - |eth_interface_gr
[Driver_ETH_MAC.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_ETH_MAC.h)  | [Driver_ETH_MAC.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_ETH_MAC.c) | eth_mac_interface_gr
[Driver_ETH_PHY.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_ETH_MAC.h)  | [Driver_ETH_PHY.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_ETH_PHY.c) | eth_phy_interface_gr
[Driver_Flash.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_Flash.h)  | [Driver_Flash.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_Flash.c) | flash_interface_gr
[Driver_GPIO.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_GPIO.h)  | [Driver_GPIO.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_GPIO.c) | gpio_interface_gr
[Driver_I2C.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_I2C.h)  | [Driver_I2C.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_I2C.c) | i2c_interface_gr
[Driver_MCI.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_MCI.h)  | [Driver_MCI.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_MCI.c) | mci_interface_gr
[Driver_NAND.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_NAND.h)  | [Driver_NAND.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_NAND.c) | nand_interface_gr
[Driver_SAI.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_SAI.h)  | [Driver_SAI.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_SAI.c) | sai_interface_gr
[Driver_SPI.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_SPI.h)  | [Driver_SPI.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_SPI.c) | spi_interface_gr
[Driver_Storage.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_Storage.h)  | [Driver_Storage.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_Storage.c) | storage_interface_gr
[Driver_USART.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_USART.h)  | [Driver_USART.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_USART.c) | usart_interface_gr
[Driver_USB.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_USB.h)  | - | usb_interface_gr
[Driver_USBD.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_USBD.h)  | [Driver_USBD.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_USBD.c) | usbd_interface_gr
[Driver_USBH.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_USBH.h)  | [Driver_USBH.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_USBH.c) | usbh_interface_gr
[Driver_WiFi.h](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/Include/Driver_WiFi.h)  | [Driver_WiFi.c](https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Driver/DriverTemplates/Driver_WiFi.c) | wifi_interface_gr
