---
id: "drv-mci-interface-arm-mci-control"
type: "concept"
domain: "drivers"
title: "MCI Interface: ARM_MCI_Control"
summary: "Th function ARM_MCI_Control controls the MCI interface and executes various operations."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_MCI_Control (uint32_t control, uint32_t arg)
```


Th function **ARM_MCI_Control** controls the MCI interface and executes various operations.

The parameter **control** specifies the operation.  
Values for **control** cannot be ORed, but must be called separately in the code. \n
The parameter **arg** provides, depending on the operation, additional information or sets values.

**Note:**
For parameters, the values marked with (default) are the setting after the driver initialization.

The table lists values for the parameter **control.**

Parameter **control**                 | Operation
:-------------------------------------|:------------
ARM_MCI_BUS_SPEED                | Set the Bus Speed. The parameter **arg** specifies the speed in bits/s; The function returns the bus speed configured in bits/s.
ARM_MCI_BUS_SPEED_MODE           | Set the Bus Speed Mode. Predefined values for **arg** are listed in the table **Bus Speed Mode**.
ARM_MCI_BUS_CMD_MODE             | Set the CMD Line Mode. Predefined values for **arg** are listed in the table **Bus CMD Line Mode**.
ARM_MCI_BUS_DATA_WIDTH           | Set data bus width. Predefined values for **arg** are encoded in **Bus Data Width**.
ARM_MCI_DRIVER_STRENGTH          | Set driver strength. Predefined values for **arg** are listed in the table **Driver Type**
ARM_MCI_CONTROL_RESET            | Control optional RST_n Pin (eMMC). The parameter **arg** can have the values `[0:inactive(default); 1:active]`
ARM_MCI_CONTROL_CLOCK_IDLE       | Control clock generation on CLK Pin when idle. The parameter **arg**  can have the values `[0:disabled; 1:enabled]`
ARM_MCI_UHS_TUNING_OPERATION     | Sampling clock Tuning operation (SD UHS-I). The parameter **arg**  can have the values  `[0:reset; 1:execute]`
ARM_MCI_UHS_TUNING_RESULT        | Sampling clock Tuning result (SD UHS-I). Returns `[0:done; 1:in progress; -1:error]`
ARM_MCI_DATA_TIMEOUT             | Set Data timeout;  The parameter **arg** sets the timeout in bus cycles.
ARM_MCI_CSS_TIMEOUT              | Set Command Completion Signal (CCS) timeout. The parameter **arg** sets timeout in bus cycles.
ARM_MCI_MONITOR_SDIO_INTERRUPT   | Monitor SD I/O interrupt. The parameter **arg**  can have the values `[0:disabled(default); 1:enabled]`. Monitoring is automatically disabled when an interrupt is recognized.
ARM_MCI_CONTROL_READ_WAIT        | Control Read/Wait states for SD I/O. The parameter **arg**  can have the values `[0:disabled(default); 1:enabled]`.
ARM_MCI_SUSPEND_TRANSFER         | Suspend Data transfer (SD I/O). Returns the number of remaining bytes to transfer.
ARM_MCI_RESUME_TRANSFER          | Resume Data transfer (SD I/O).
 
 
**Bus Speed Mode**
 
The function ARM_MCI_GetCapabilities lists the supported bus speed modes. Initially, all SD cards use a 3.3 volt electrical interface. 
Some SD cards can switch to 1.8 volt operation. For example, the use of ultra-high-speed (UHS) 
SD cards requires 1.8 volt operation and a 4-bit bus data width. The bit field ARM_MCI_CAPABILITIES.uhs_signaling encodes 
whether the driver supports 1.8 volt UHS signaling.

The **control** operation **ARM_MCI_BUS_SPEED_MODE**  sets the bus speed mode using the parameter **arg.**

Parameter **arg**                                             | Bus Speed Mode
:-------------------------------------------------------------|:------------------------------------------
ARM_MCI_BUS_DEFAULT_SPEED (default)                     | Set the bus speed for SD/MMC cards: Default Speed mode up to `[25;26]MHz` 
ARM_MCI_BUS_HIGH_SPEED                                  | Set the bus speed for SD/MMC: High    Speed mode up to `[50;52]MHz`
ARM_MCI_BUS_UHS_SDR12                                   | Set the bus speed for SD: SDR12  (Single Data Rate) up to  `25MHz,  12.5MB/s: UHS-I (Ultra High Speed) 1.8V signalling`
ARM_MCI_BUS_UHS_SDR25                                   | Set the bus speed for SD: SDR25  (Single Data Rate) up to  `50MHz,  25  MB/s: UHS-I (Ultra High Speed) 1.8V signalling`
ARM_MCI_BUS_UHS_SDR50                                   | Set the bus speed for SD: SDR50  (Single Data Rate) up to `100MHz,  50  MB/s: UHS-I (Ultra High Speed) 1.8V signalling`
ARM_MCI_BUS_UHS_SDR104                                  | Set the bus speed for SD: SDR104 (Single Data Rate) up to `208MHz, 104  MB/s: UHS-I (Ultra High Speed) 1.8V signalling`
ARM_MCI_BUS_UHS_DDR50                                   | Set the bus speed for SD: DDR50  (Dual Data Rate)   up to  `50MHz,  50  MB/s: UHS-I (Ultra High Speed) 1.8V signalling`
 
 
**Bus CMD Line Mode** 
 
The **control** operation **ARM_MCI_BUS_CMD_MODE** sets the bus command line mode using the parameter **arg.**

Parameter **arg**                                             | Bus CMD Line Mode  
:-------------------------------------------------------------|:------------------------------------------
ARM_MCI_BUS_CMD_PUSH_PULL  (default)                     | Set the Push-Pull CMD line
ARM_MCI_BUS_CMD_OPEN_DRAIN                               | Set the Open Drain CMD line (MMC only)
 
 
**Bus Data Width** 
 
Specifies the bus data width (the number of data I/O pins on the SD/MMC interface).
 
For high speed memory cards, a 4-bit bus data width should be used (or 8-bit for eMMC). The bit fields ARM_MCI_CAPABILITIES.data_width_4 and
ARM_MCI_CAPABILITIES.data_width_8 encode whether the driver supports a specific bus data with.

The **control** operation **ARM_MCI_BUS_DATA_WIDTH**  sets the bus data width using the parameter **arg.**

Parameter **arg**                                             | Bus Data Width
:-------------------------------------------------------------|:------------------------------------------
ARM_MCI_BUS_DATA_WIDTH_1 (default)                       | Set the Bus data width to `1 bit` 
ARM_MCI_BUS_DATA_WIDTH_4                                 | Set the Bus data width to `4 bits`
ARM_MCI_BUS_DATA_WIDTH_8                                 | Set the Bus data width to `8 bits`
ARM_MCI_BUS_DATA_WIDTH_4_DDR                             | Set the Bus data width to `4 bits`, DDR (Dual Data Rate) - MMC only
ARM_MCI_BUS_DATA_WIDTH_8_DDR                             | Set the Bus data width to `8 bits`, DDR (Dual Data Rate) - MMC only
 
 
**Driver Type** 
 
Specifies the interface driver type.

The **control** operation **ARM_MCI_DRIVER_STRENGTH**  sets the interface driver type using the parameter **arg.**

Parameter **arg**                                             | Driver Type 
:-------------------------------------------------------------|:------------------------------------------
ARM_MCI_DRIVER_TYPE_A                                    | Set the interface to SD UHS-I Driver Type A
ARM_MCI_DRIVER_TYPE_B  (default)                         | Set the interface to SD UHS-I Driver Type B 
ARM_MCI_DRIVER_TYPE_C                                    | Set the interface to SD UHS-I Driver Type C
ARM_MCI_DRIVER_TYPE_D                                    | Set the interface to SD UHS-I Driver Type D

**Examples:**
```
// Set Bus Speed to 25MHz
MCIdrv->Control(ARM_MCI_BUS_SPEED, 25000000);
 
// Set High Speed mode
MCIdrv->Control(ARM_MCI_BUS_SPEED_MODE, ARM_MCI_BUS_HIGH_SPEED);
 
// Configure CMD line as Open Drain (MMC only)
MCIdrv->Control(ARM_MCI_BUS_CMD_MODE, ARM_MCI_BUS_CMD_OPEN_DRAIN);
 
// Set Bus Data Width = 4bits
MCIdrv->Control(ARM_MCI_BUS_DATA_WIDTH, ARM_MCI_BUS_DATA_WIDTH_4);
 
// Set SD UHS-I Driver Type B
MCIdrv->Control(ARM_MCI_DRIVER_STRENGTH, ARM_MCI_DRIVER_TYPE_B);
 
// RTS_n Pin is not active by default
// Assert RTS_n Pin (eMMC)
MCIdrv->Control(ARM_MCI_CONTROL_RESET, 1);
// De-assert RTS_n Pin (eMMC)
MCIdrv->Control(ARM_MCI_CONTROL_RESET, 0);
 
// Clock generation on CLK when Idle: hardware specific default behavior
// Enable Clock generation on CLK when Idle
MCIdrv->Control(ARM_MCI_CONTROL_CLOCK_IDLE, 1);
// Disable Clock generation on CLK when Idle
MCIdrv->Control(ARM_MCI_CONTROL_CLOCK_IDLE, 0);
 
// UHS Tuning
MCIdrv->Control(ARM_MCI_UHS_TUNING_OPERATION, 1);  // start tuning
do {
  status = MCIdrv->Control(ARM_MCI_UHS_TUNING_RESULT, 0/*argument not used*/);
  if (status == -1) { break; /* tuning failed */ }
} while (status == 1);
 
// Set Data Timeout to 12500000 bus cycles (0.5s @25MHz Bus Speed)
// Default value is hardware specific (typically 2^32-1)
MCIdrv->Control(ARM_MCI_DATA_TIMEOUT, 12500000);
  
// Set CSS Timeout to 1000000 bus cycles
// Default value is hardware specific
MCIdrv->Control(ARM_MCI_CSS_TIMEOUT, 1000000);
 
// SD I/O Interrupt Monitoring is disabled by default
// Enable SD I/O Interrupt Monitoring
MCIdrv->Control(ARM_MCI_MONITOR_SDIO_INTERRUPT, 1);
// Disable SD I/O Interrupt Monitoring
MCIdrv->Control(ARM_MCI_MONITOR_SDIO_INTERRUPT, 0);
 
// Read/Wait for SD I/O is disabled by default
// Enable Read/Wait for SD I/O
MCIdrv->Control(ARM_MCI_CONTROL_READ_WAIT, 1);
// Disable Read/Wait for SD I/O
MCIdrv->Control(ARM_MCI_CONTROL_READ_WAIT, 0);
 
// Suspend Data transfer (SD I/O)
MCIdrv->Control(ARM_MCI_SUSPEND_TRANSFER, 0/*argument not used*/);
 
// Resume Data transfer (SD I/O)
MCIdrv->Control(ARM_MCI_RESUME_TRANSFER, 0/*argument not used*/);
```
******************************************************************************************************************
