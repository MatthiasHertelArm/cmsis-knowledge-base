---
id: "drv-spi-slave-select-mode"
type: "concept"
domain: "drivers"
title: "SPI Slave Select Mode"
summary: "An SPI master does not drive or monitor the SS line. For example, when connecting to a single slave, the SS line can be connected to a fixed low level. \\sa ARM_SPI_Control"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
license: "Apache-2.0"
mode: "V"
---

Specifies SPI slave select mode.

**SPI** **Slave** **Select** **Mode** configures the behavior of the **Slave** **Select** **(SS)** signal. The configuration is
separate for **Master** (ARM_SPI_SS_MASTER_*) and for **Slave** (ARM_SPI_SS_SLAVE_HW, ARM_SPI_SS_SLAVE_SW). The
active configuration depends on the current state (Master/Slave).


### ARM_SPI_SS_MASTER_UNUSED

```c
ARM_SPI_SS_MASTER_UNUSED
```

An SPI master does not drive or monitor the SS line. For example, when connecting to a single slave, the SS line can be connected
to a fixed low level.
\sa ARM_SPI_Control

### ARM_SPI_SS_MASTER_SW

```c
ARM_SPI_SS_MASTER_SW
```

SS is configured as an output and controlled via ARM_SPI_Control (ARM_SPI_CONTROL_SS). By default, it is not active
(high). It is activated (low) by ARM_SPI_Control (ARM_SPI_CONTROL_SS, ARM_SPI_SS_ACTIVE) and deactivated by
ARM_SPI_Control (ARM_SPI_CONTROL_SS, ARM_SPI_SS_INACTIVE). It is not affected by transfer/send/receive
functions.
\sa ARM_SPI_Control

### ARM_SPI_SS_MASTER_HW_OUTPUT

```c
ARM_SPI_SS_MASTER_HW_OUTPUT
```

Here, SS is configured as an output. It will be automatically activated/deactivated for the transfers by hardware (not
controlled by ARM_SPI_Control (ARM_SPI_CONTROL_SS)). The activation/deactivation of the line is completely hardware
dependent. Typically, the hardware will activate it before starting a transfer and deactivate it after a transfer completes.
Some hardware will keep the line active as long as the SPI stays master. Due to different hardware behavior, this mode is
typically not useful because certain devices require that the SS signal is strictly defined with regards to transfers.
\sa ARM_SPI_Control

### ARM_SPI_SS_MASTER_HW_INPUT

```c
ARM_SPI_SS_MASTER_HW_INPUT
```

This is normally used in a multi-master configuration, where a master does not drive the SS line when driving the bus but only
monitors it. When another master activates this line, the active master backs off. This is called **mode** **fault.** SS is
configured as input and the hardware only monitors it. When it is externally deactivated while being the master, it presents
a mode fault and the SPI switches to **inactive** mode.
\sa ARM_SPI_Control

### ARM_SPI_SS_SLAVE_HW

```c
ARM_SPI_SS_SLAVE_HW
```

Hardware monitors the SS line and accepts transfers only when SS line is activate. Transfers while SS is not active are
ignored.
\sa ARM_SPI_Control

### ARM_SPI_SS_SLAVE_SW

```c
ARM_SPI_SS_SLAVE_SW
```

Used only when SS line is not used. For example, when a single master and slave are connected in a system, the SS line is not
needed (reduces the number of lines and pins used). Slave responses are controlled by software (by default, it is not
responding). Software enables/disables transfers by calling ARM_SPI_Control (ARM_SPI_CONTROL_SS, ARM_SPI_SS_ACTIVE / ARM_SPI_SS_INACTIVE).
\sa ARM_SPI_Control
