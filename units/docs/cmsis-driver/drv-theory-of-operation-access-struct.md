---
id: "drv-theory-of-operation-access-struct"
type: "concept"
domain: "drivers"
title: "Theory of Operation: Access Struct"
summary: "A CMSIS-Driver publishes an AccessStruct with the data type name ARMDRIVERxxxx that gives to access the driver functions."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/operation.md#access-struct"
license: "Apache-2.0"
mode: "V"
---

A CMSIS-Driver publishes an AccessStruct with the data type name `ARM_DRIVER_xxxx` that gives to access the driver functions.

**Code Example:** Function Access of the SPI driver

```c
typedef struct _ARM_DRIVER_SPI {
  ARM_DRIVER_VERSION   (*GetVersion)      (void);
  ARM_SPI_CAPABILITIES (*GetCapabilities) (void);
  int32_t              (*Initialize)      (ARM_SPI_SignalEvent_t cb_event);
  int32_t              (*Uninitialize)    (void);
  int32_t              (*PowerControl)    (ARM_POWER_STATE state);
  int32_t              (*Send)            (const void *data, uint32_t num);
  int32_t              (*Receive)         (      void *data, uint32_t num);
  int32_t              (*Transfer)        (const void *data_out, void *data_in, uint32_t num);
  uint32_t             (*GetDataCount)    (void);
  int32_t              (*Control)         (uint32_t control, uint32_t arg);
  ARM_SPI_STATUS       (*GetStatus)       (void);
} const ARM_DRIVER_SPI;
```

### Driver Instances

A device may offer several peripherals of the same type. For such devices, the CMSIS-Driver publishes multiple instances of the AccessStruct. The name of each driver instance reflects the names of the peripheral available in the device.

**Code Example:** AccessStruct for three SPIs in a microcontroller device.

```c
ARM_DRIVER_SPI Driver_SPI1;     // access functions for SPI1 interface
ARM_DRIVER_SPI Driver_SPI2;     // access functions for SPI2 interface
ARM_DRIVER_SPI Driver_SPI3;     // access functions for SPI3 interface
```

The access functions can be passed to middleware to specify the driver instance that the middleware should use for communication.

**Naming Convention**

The access structs need to follow this naming convention: the keyword `Driver` followed by an underscore `_`, the interface name `IFNAME` (usually in upper case letters), and the instance number `n`. Here's the full list of access struct names for all drivers (n to be replaced with the actual instance number):

```c
Driver_CANn
Driver_ETH_MACn
Driver_ETH_PHYn
Driver_Flashn
Driver_GPIOn
Driver_I2Cn
Driver_MCIn
Driver_NANDn
Driver_SAIn
Driver_SPIn
Driver_Storagen
Driver_USARTn
Driver_USBDn
Driver_USBHn
Driver_WiFin
```


**Example:**

```c
void init_middleware (ARM_DRIVER_SPI *Drv_spi) ...
\\ inside the middleware the SPI driver functions are called with:
\\   Drv_spi->function (...);
```

```c
\\ setup middleware
init_middleware (&Driver_SPI1);      // connect middleware to SPI1 interface
  :
init_middleware (&Driver_SPI2);      // connect middleware to SPI2 interface
```
