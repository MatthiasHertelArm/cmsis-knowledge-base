---
id: "drv-mci-bus-data-width"
type: "concept"
domain: "drivers"
title: "MCI Bus Data Width"
summary: "The function ARMMCIControl with control = ARMMCIBUSDATAWIDTH specifies with arg the number of data I/O pins on the SD/MMC interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

Specify the data bus width.

The function ARM_MCI_Control with **control** = ARM_MCI_BUS_DATA_WIDTH specifies with **arg** the number of data I/O pins on the SD/MMC interface.

For high-speed memory cards, a 4-bit bus data width should be used (or 8-bit for eMMC). The data fields **data_width_4** and **data_width_8** 
of the structure ARM_MCI_CAPABILITIES encode whether the driver supports a specific bus data with.

The following codes are defined:


### ARM_MCI_BUS_DATA_WIDTH_1

```c
ARM_MCI_BUS_DATA_WIDTH_1
```


### ARM_MCI_BUS_DATA_WIDTH_4

```c
ARM_MCI_BUS_DATA_WIDTH_4
```


### ARM_MCI_BUS_DATA_WIDTH_8

```c
ARM_MCI_BUS_DATA_WIDTH_8
```


### ARM_MCI_BUS_DATA_WIDTH_4_DDR

```c
ARM_MCI_BUS_DATA_WIDTH_4_DDR
```


### ARM_MCI_BUS_DATA_WIDTH_8_DDR

```c
ARM_MCI_BUS_DATA_WIDTH_8_DDR
```

******************************************************************************************************************
