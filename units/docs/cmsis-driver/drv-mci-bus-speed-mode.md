---
id: "drv-mci-bus-speed-mode"
type: "concept"
domain: "drivers"
title: "MCI Bus Speed Mode"
summary: "The function ARM_MCI_Control with control = ARM_MCI_BUS_SPEED configures the bus speed of the MCI to the requested bits/s specified with arg."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

Specify the bus speed mode.

The function ARM_MCI_Control with **control** = ARM_MCI_BUS_SPEED configures the bus speed of the MCI to the
requested bits/s specified with **arg.**

The function ARM_MCI_Control with **control** = ARM_MCI_BUS_SPEED_MODE configures the bus speed mode of the MCI
as specified with **arg** listed bellow.

The function ARM_MCI_GetCapabilities lists the supported bus speed modes. Initially, all SD cards use a 3.3 volt electrical interface. 
Some SD cards can switch to 1.8 volt operation. For example, the use of ultra-high-speed (UHS) 
SD cards requires 1.8 volt operation and a 4-bit bus data width. The data field **uhs_signaling** of the structure ARM_MCI_CAPABILITIES encodes 
whether the driver supports 1.8 volt UHS signaling.

\sa 
 - mci_driver_strength_ctrls

The following codes are defined:


### ARM_MCI_BUS_DEFAULT_SPEED

```c
ARM_MCI_BUS_DEFAULT_SPEED
```


### ARM_MCI_BUS_HIGH_SPEED

```c
ARM_MCI_BUS_HIGH_SPEED
```


### ARM_MCI_BUS_UHS_SDR12

```c
ARM_MCI_BUS_UHS_SDR12
```


### ARM_MCI_BUS_UHS_SDR25

```c
ARM_MCI_BUS_UHS_SDR25
```


### ARM_MCI_BUS_UHS_SDR50

```c
ARM_MCI_BUS_UHS_SDR50
```


### ARM_MCI_BUS_UHS_SDR104

```c
ARM_MCI_BUS_UHS_SDR104
```


### ARM_MCI_BUS_UHS_DDR50

```c
ARM_MCI_BUS_UHS_DDR50
```

******************************************************************************************************************
