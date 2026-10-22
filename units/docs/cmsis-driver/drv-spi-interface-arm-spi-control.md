---
id: "drv-spi-interface-arm-spi-control"
type: "concept"
domain: "drivers"
title: "SPI Interface: ARM_SPI_Control"
summary: "The function ARM_SPI_Control controls the SPI interface settings and executes various operations."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_SPI_Control (uint32_t control, uint32_t arg)
```


The function **ARM_SPI_Control** controls the SPI interface settings and executes various operations.

The parameter **control** is a bit mask that specifies various operations. 
  - Controls form different categories can be ORed. 
  - If one control is omitted, then the default value of that category is used.
  - Miscellaneous controls cannot be combined.  

The parameter **arg** provides (depending on the parameter **control)** additional information, for example the Bus Speed.




| Parameter **control** | Bit | Category | Description |
|---|---|---|---|
| ARM_SPI_MODE_INACTIVE | 0..7 | Mode Controls | Set SPI to inactive. |
| ARM_SPI_MODE_MASTER | Set the SPI Master (Output on MOSI, and the Input on MISO); **arg** = Bus Speed in `bps` |  |  |
| ARM_SPI_MODE_SLAVE | Set the SPI Slave (Output on MISO, and the Input on MOSI) |  |  |
| ARM_SPI_CPOL0_CPHA0 (default) | 8..11 | Clock Polarity (Frame Format) | CPOL=`0` and CPHA=`0`: Clock Polarity 0, Clock Phase 0 |
| ARM_SPI_CPOL0_CPHA1 | CPOL=`0` and CPHA=`1`: Clock Polarity 0, Clock Phase 1 |  |  |
| ARM_SPI_CPOL1_CPHA0 | CPOL=`1` and CPHA=`0`: Clock Polarity 1, Clock Phase 0 |  |  |
| ARM_SPI_CPOL1_CPHA1 | CPOL=`1` and CPHA=`1`: Clock Polarity 1, Clock Phase 1 |  |  |
| ARM_SPI_TI_SSI | Specifies that the frame format corresponds to the Texas Instruments Frame Format |  |  |
| ARM_SPI_MICROWIRE | Specifies that the frame format corresponds to the National Semiconductor Microwire Frame Format |  |  |
| ARM_SPI_DATA_BITS(n) | 12..17 | Data Bits | Set the number of bits per SPI frame; range for **n** = `1..32`. This is the minimum required parameter. |
| ARM_SPI_MSB_LSB (default) | 18 | Bit Order | Set the bit order from MSB to LSB |
| ARM_SPI_LSB_MSB | Set the bit order from LSB to MSB |  |  |
| ARM_SPI_SS_MASTER_UNUSED (default) | 19..21 | Slave Select when Master   Must be used with the corresponding master or slave controls from category [**Mode Controls**](#spi_mode_tab).   Slave Select when Slave | Set the Slave Select mode for the master to **Not used**. Used with Mode Control ARM_SPI_MODE_MASTER. Master does not drive or monitor the SS line. For example, when connecting to a single slave, which has the SS line connected to a fixed low level. |
| ARM_SPI_SS_MASTER_SW | Set the Slave Select mode for the master to **Software controlled**. Used with Mode Control ARM_SPI_MODE_MASTER. The Slave Select line is configured as output and controlled via the Miscellaneous Control ARM_SPI_CONTROL_SS. By default, the line it is not active (high), and is not affected by transfer-, send-, or receive functions. |  |  |
| ARM_SPI_SS_MASTER_HW_OUTPUT | Set the Slave Select mode for the master to **Hardware controlled Output**. Used with Mode Control ARM_SPI_MODE_MASTER. The Slave Select line is configured as output and controlled by hardware. The line gets activated or deactivated automatically by the hardware for transfers and is not controlled by the Miscellaneous Control ARM_SPI_CONTROL_SS. When exactly the line is activated or deactivated is hardware dependent. Typically, the hardware will activate the line before starting the transfer and deactivate it after the transfer completes. Some hardware will keep the line active as long as the SPI stays master. **Note:** Some devices require that the SS signal is strictly defined regarding transfers. Refer to the documentation of your device. |  |  |
| ARM_SPI_SS_MASTER_HW_INPUT | Set the Slave Select mode for the master to **Hardware monitored Input**. Used with Mode Control ARM_SPI_MODE_MASTER. Used in multi-master configuration where a master does not drive the Slave Select when driving the bus, but rather monitors it. When another master activates this line, the active master backs off. This is called Mode Fault. Slave Select is configured as input and hardware only monitors the line. When the line is activated externally while we are master, it presents a Mode Fault (ARM_SPI_EVENT_MODE_FAULT) and the SPI switches to inactive mode. |  |  |
| ARM_SPI_SS_SLAVE_HW (default) | Set the Slave Select mode for the slave to **Hardware monitored**. Used with Mode Control ARM_SPI_MODE_SLAVE. Hardware monitors the Slave Select line and accepts transfers only when the line is active. Transfers are ignored while the Slave Select line is inactive. |  |  |
| ARM_SPI_SS_SLAVE_SW | Set the Slave Select mode for the slave to **Software controlled**. Used with Mode Control ARM_SPI_MODE_SLAVE. Used only when the Slave Select line is not used. For example, when a single master and slave are connected in the system then the Slave Select line is not needed. Software controls if the slave is responding or not (by default it is not responding). Software enables or disables transfers by using the Miscellaneous Control ARM_SPI_CONTROL_SS. |  |  |
| ARM_SPI_SET_BUS_SPEED | 0..21 | Miscellaneous Controls (cannot be ORed) | Set the bus speed; **arg=** Bus Speed in `bps` |
| ARM_SPI_GET_BUS_SPEED | Get the bus speed; Return values >= `0` represent the bus speed in `bps`. Negative values are spi_execution_status. |  |  |
| ARM_SPI_SET_DEFAULT_TX_VALUE | Set the default transmission value; the parameter **arg** sets the value |  |  |
| ARM_SPI_CONTROL_SS | Control the Slave Select signal (SS); the values for the parameter **arg** are: `ARM_SPI_SS_INACTIVE; ARM_SPI_SS_ACTIVE` |  |  |
| ARM_SPI_ABORT_TRANSFER | Abort the current data transfer |  |  |





**Example** 

```
  extern ARM_DRIVER_SPI Driver_SPI0;
  
  // configure: SPI master | clock polarity=1, clock phase=1 | bits per frame=16 | bus speed : 1000000 
  status = Driver_SPI0.Control(ARM_SPI_MODE_MASTER   | 
                               ARM_SPI_CPOL1_CPHA1   | 
                               ARM_SPI_DATA_BITS(16), 1000000);
```
****************************************************************************************************************
