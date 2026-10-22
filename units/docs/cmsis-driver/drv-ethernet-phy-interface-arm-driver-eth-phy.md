---
id: "drv-ethernet-phy-interface-arm-driver-eth-phy"
type: "concept"
domain: "drivers"
title: "Ethernet PHY Interface: ARM_DRIVER_ETH_PHY"
summary: "The functions of the Ethernet PHY are accessed by function pointers exposed by this structure. Refer to DriverFunctions for overview information."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_PHY.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_PHY.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_ETH_PHY
```


The functions of the Ethernet PHY are accessed by function pointers exposed by this structure. Refer to DriverFunctions for 
overview information.

Each instance of an Ethernet PHY provides such an access struct. The instance is identified by
a postfix number in the symbol name of the access struct, for example:
 - **Driver_ETH_PHY0** is the name of the access struct of the first instance (no. 0).
 - **Driver_ETH_PHY1** is the name of the access struct of the second instance (no. 1).


A configuration setting in the middleware allows connecting the middleware to a specific driver instance **Driver_ETH_PHY_n_**.
The default is `0`, which connects a middleware to the first instance of a driver.
****************************************************************************************************************
