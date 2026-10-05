---
id: "drv-mci-driver-strength"
type: "concept"
domain: "drivers"
title: "MCI Driver Strength"
summary: "The function ARMMCIControl with control = ARMMCIDRIVERSTRENGTH specifies with arg the driver type of the SD interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

Specify the driver strength.

The function ARM_MCI_Control with **control** = ARM_MCI_DRIVER_STRENGTH specifies with **arg** the driver type of the SD interface.

\sa
  - mci_bus_speed_ctrls

The following codes are defined:


### ARM_MCI_DRIVER_TYPE_A

```c
ARM_MCI_DRIVER_TYPE_A
```


### ARM_MCI_DRIVER_TYPE_B

```c
ARM_MCI_DRIVER_TYPE_B
```


### ARM_MCI_DRIVER_TYPE_C

```c
ARM_MCI_DRIVER_TYPE_C
```


### ARM_MCI_DRIVER_TYPE_D

```c
ARM_MCI_DRIVER_TYPE_D
```

******************************************************************************************************************
