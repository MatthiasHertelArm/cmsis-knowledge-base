---
id: "drv-nand-interface-arm-nand-control"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_Control"
summary: "The function ARM_NAND_Control controls the NAND interface and executes operations."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_NAND_Control (uint32_t dev_num, uint32_t control, uint32_t arg)
```


The function **ARM_NAND_Control** controls the NAND interface and executes operations.

The parameter **dev_num** is the device number. \n
The parameter **control** specifies the operation. \n
The parameter **arg** provides (depending on the **control)** additional information or sets values.

The table lists the operations for the parameter **control.**

Parameter **control**            | Operation
:--------------------------------|:--------------------------------------------
ARM_NAND_BUS_MODE           | Set the bus mode. The parameter **arg** sets the **Bus** Mode.
ARM_NAND_BUS_DATA_WIDTH     | Set the data bus width. The parameter **arg** sets the **Bus** Data Width.
ARM_NAND_DRIVER_STRENGTH    | Set the driver strength. The parameter **arg** sets the **Driver** Strength.
ARM_NAND_DRIVER_READY_EVENT | Control generation of callback event ARM_NAND_EVENT_DRIVER_READY. Enable: **arg** = `1`. Disable: **arg** = `0`.
ARM_NAND_DEVICE_READY_EVENT | Control generation of callback event ARM_NAND_EVENT_DEVICE_READY; Enable: **arg** = `1`. Disable: **arg** = `0`.

**See Also**
- ARM_NAND_GetCapabilities returns information about supported operations, which are stored in the structure ARM_NAND_CAPABILITIES.
- ARM_NAND_SignalEvent provides information about the callback events ARM_NAND_EVENT_DRIVER_READY and ARM_NAND_EVENT_DEVICE_READY

The table lists values for the parameter **arg** used with the **control** operation ARM_NAND_BUS_MODE, ARM_NAND_BUS_DATA_WIDTH, and
ARM_NAND_DRIVER_STRENGTH. Values from different categories can be ORed.




| Parameter **arg** for control = ARM_NAND_BUS_MODE | Bit | Category | Description | Supported when ARM_NAND_CAPABILITIES |
|---|---|---|---|---|
| ARM_NAND_BUS_TIMING_MODE_0 (default) | 0..3 | Bus Timing Mode | `0` | The maximum timing mode that can be applied to a specific **Bus** Data Interface is stored in the data fields: sdr_timing_mode - for SDR ddr_timing_mode - for NV-DDR ddr2_timing_mode - for NV_DDR2 |
| ARM_NAND_BUS_TIMING_MODE_1 | `1` |  |  |  |
| ARM_NAND_BUS_TIMING_MODE_2 | `2` |  |  |  |
| ARM_NAND_BUS_TIMING_MODE_3 | `3` |  |  |  |
| ARM_NAND_BUS_TIMING_MODE_4 | `4` (SDR EDO capable) |  |  |  |
| ARM_NAND_BUS_TIMING_MODE_5 | `5` (SDR EDO capable) |  |  |  |
| ARM_NAND_BUS_TIMING_MODE_6 | `6` (NV-DDR2 only) |  |  |  |
| ARM_NAND_BUS_TIMING_MODE_7 | `7` (NV-DDR2 only) |  |  |  |
| ARM_NAND_BUS_SDR (default) | 4..7 | Bus Data Interface | SDR (Single Data Rate) - Traditional interface | always supported |
| ARM_NAND_BUS_DDR | NV-DDR (Double Data Rate) | data field ddr = `1` |  |  |
| ARM_NAND_BUS_DDR2 | NV-DDR2 (Double Data Rate) | data field ddr2 = `1` |  |  |
| ARM_NAND_BUS_DDR2_DO_WCYC_0 (default) | 8..11 | Data Output Warm-up | Set the DDR2 Data Output Warm-up to `0` cycles | **Data Output Warm-up** cycles are dummy cycles for interface calibration with no incremental data transfer and apply to NV-DDR2 of the **Bus** Data Interface. |
| ARM_NAND_BUS_DDR2_DO_WCYC_1 | Set the DDR2 Data Output Warm-up to `1` cycles |  |  |  |
| ARM_NAND_BUS_DDR2_DO_WCYC_2 | Set the DDR2 Data Output Warm-up to `2` cycles |  |  |  |
| ARM_NAND_BUS_DDR2_DO_WCYC_4 | Set the DDR2 Data Output Warm-up to `4` cycles |  |  |  |
| ARM_NAND_BUS_DDR2_DI_WCYC_0 (default) >  12..15 | Data Input Warm-up | Set the DDR2 Data Input Warm-up to `0` cycles | **Data Input Warm-up** cycles are dummy cycles for interface calibration with no incremental data transfer and apply to NV-DDR2 of the **Bus** Data Interface. |  |
| ARM_NAND_BUS_DDR2_DI_WCYC_1 | Set the DDR2 Data Input Warm-up to `1` cycles |  |  |  |
| ARM_NAND_BUS_DDR2_DI_WCYC_2 | Set the DDR2 Data Input Warm-up to `2` cycles |  |  |  |
| ARM_NAND_BUS_DDR2_DI_WCYC_4 | Set the DDR2 Data Input Warm-up to `4` cycles |  |  |  |
| ARM_NAND_BUS_DDR2_VEN   | 16 | Miscellaneous | Set the DDR2 Enable external VREFQ as reference |   |
| ARM_NAND_BUS_DDR2_CMPD | 17 | Set the DDR2 Enable complementary DQS (DQS_c) signal |  |  |
| ARM_NAND_BUS_DDR2_CMPR | 18 | Set the DDR2 Enable complementary RE_n (RE_c) signal |  |  |
| Parameter **arg** for control = ARM_NAND_BUS_DATA_WIDTH | Bit | Category | Description | Supported when ARM_NAND_CAPABILITIES |
| ARM_NAND_BUS_DATA_WIDTH_8 (default) | 0..1 | Bus Data Width | Set to `8 bit` | always supported |
| ARM_NAND_BUS_DATA_WIDTH_16 | Set to `16 bit` | data field data_width_16 = `1` |  |  |
| Parameter **arg** for control = ARM_NAND_DRIVER_STRENGTH | Bit | Category | Description | Supported when ARM_NAND_CAPABILITIES |
| ARM_NAND_DRIVER_STRENGTH_18 | 0..3 | Driver Strength | Set the Driver Strength 2.0x = 18 Ohms | data field driver_strength_18 = `1` |
| ARM_NAND_DRIVER_STRENGTH_25 | Set the Driver Strength 1.4x = 25 Ohms | data field driver_strength_25 = `1` |  |  |
| ARM_NAND_DRIVER_STRENGTH_35 (default) | Set the Driver Strength 1.0x = 35 Ohms | always supported |  |  |
| ARM_NAND_DRIVER_STRENGTH_50 | Set the Driver Strength 0.7x = 50 Ohms | data field driver_strength_50 = `1` |  |  |



**Example**
```
extern ARM_DRIVER_NAND Driver_NAND0;
 
status = Driver_NAND0.Control (0, ARM_NAND_BUS_MODE, ARM_NAND_BUS_TIMING_MODE_5 | 
                                                     ARM_NAND_BUS_DDR2          | 
                                                     ARM_NAND_BUS_DDR2_VEN);
											    
status = Driver_NAND0.Control (0, ARM_NAND_BUS_DATA_WIDTH,  ARM_NAND_BUS_DATA_WIDTH_16); 
 
status = Driver_NAND0.Control (0, ARM_NAND_DRIVER_STRENGTH, ARM_NAND_DRIVER_STRENGTH_50);
```

******************************************************************************************************************
