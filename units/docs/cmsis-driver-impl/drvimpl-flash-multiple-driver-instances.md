---
id: "drvimpl-flash-multiple-driver-instances"
type: "concept"
domain: "drivers"
title: "Flash: Multiple Driver Instances"
summary: "CMSIS-Driver API supports multiple driver instances. The Flash drivers are implemented within a single C module and several driver instances of the same type can be used in a project as follows:"
status: "draft"
collection: "cmsis-driver-impl"
source: "ARM-software/CMSIS-Driver@6301c65:Documentation/Doxygen/src/flash.md"
doc_source: "https://github.com/ARM-software/CMSIS-Driver/blob/6301c65/Documentation/Doxygen/src/flash.md#multiple-driver-instances"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Driver API supports multiple driver instances. The Flash drivers are implemented within a single C module and several driver instances of the same type can be used in a project as follows:

1. Add the first driver instance to the project. In IDEs with CMSIS-pack management support this can be done from the Run-Time Environment (RTE).
2. Create a copy of the driver's .c file with a different file name and add it to the project. This will be the second driver instance. For example, copy `AT45DB641E.c` file as `AT45DB641E_2.c`.
3. Copy the driver's .h file to the project or add the driver's folder to the compiler include search path.
4. Specify the driver parameters for the second instance based on the hardware design. For example, in `AT45DB641E_2.c` the values for the flash driver number and SPI driver number need to be configured as shown below:
    ```c
    #define DRIVER_FLASH_NUM        1
    #define DRIVER_SPI_NUM          1
    ```
5. Now both Flash instances can be accessed from the application. For example:
    ```c
    #include "Driver_Flash.h"

    /* Flash driver instances */
    extern ARM_DRIVER_FLASH Driver_Flash0;
    extern ARM_DRIVER_FLASH Driver_Flash1;

    #define flash0  (&Driver_Flash0)
    #define flash1  (&Driver_Flash1)
    ```
