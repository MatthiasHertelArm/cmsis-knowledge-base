---
id: "drvimpl-ethernet-multiple-driver-instances"
type: "concept"
domain: "drivers"
title: "Ethernet: Multiple Driver Instances"
summary: "CMSIS-Driver API supports multiple driver instances. The Ethernet drivers are implemented within a single C module and several driver instances of the same type can be used in a project as follows:"
status: "draft"
collection: "cmsis-driver-impl"
source: "ARM-software/CMSIS-Driver@6301c65:Documentation/Doxygen/src/ethernet.md"
doc_source: "https://github.com/ARM-software/CMSIS-Driver/blob/6301c65/Documentation/Doxygen/src/ethernet.md#multiple-driver-instances"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Driver API supports multiple driver instances. The Ethernet drivers are implemented within a single C module and several driver instances of the same type can be used in a project as follows:

1. Add the first driver instance to the project. In IDEs with CMSIS-pack management support this can be done from the Run-Time Environment (RTE).
2. Create a copy of the driver's .c file with a different file name and add it to the project. This will be the second driver instance. For example, copy `ETH_LAN9220.c` file as `ETH2_LAN9220.c`.
3. Copy the driver's .h file to the project or add the driver's folder to the compiler include search path.
4. Specify the driver parameters for the second instance. For example, in `ETH2_LAN9220.c` new values to the following parameters are needed instead of default ones:
    ```c
    #define ETH_MAC_NUM             1
    #define ETH_PHY_NUM             1
    #define LAN9220_BASE            (0x53000000UL)
    ```
5. Now both Ethernet instances can be accessed from the application. For example:
    ```c
    #include "Driver_ETH_MAC.h"
    #include "Driver_ETH_PHY.h"

    extern ARM_DRIVER_ETH_MAC Driver_ETH_MAC0;
    extern ARM_DRIVER_ETH_MAC Driver_ETH_MAC1;

    extern ARM_DRIVER_ETH_PHY Driver_ETH_PHY0;
    extern ARM_DRIVER_ETH_PHY Driver_ETH_PHY1;

    #define eth0    (&Driver_ETH_MAC0)
    #define eth1    (&Driver_ETH_MAC1)

    #define phy0    (&Driver_ETH_PHY0)
    #define phy1    (&Driver_ETH_PHY1)
    ```
