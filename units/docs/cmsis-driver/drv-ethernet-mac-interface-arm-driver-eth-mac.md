---
id: "drv-ethernet-mac-interface-arm-driver-eth-mac"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_DRIVER_ETH_MAC"
summary: "The functions of the Ethernet MAC are accessed by function pointers. Refer to DriverFunctions for overview information."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_ETH_MAC
```


The functions of the Ethernet MAC are accessed by function pointers. Refer to DriverFunctions for 
overview information.

Each instance of an Ethernet MAC provides such an access struct. The instance is indicated by
a postfix in the symbol name of the access struct, for example:
 - **Driver_ETH_MAC0** is the name of the access struct of the first instance (no. 0).
 - **Driver_ETH_MAC1** is the name of the access struct of the second instance (no. 1).

A configuration setting in the middleware allows connecting the middleware to a specific driver instance **Driver_ETH_MAC_n_**.
The default is `0`, which connects a middleware to the first instance of a driver.
