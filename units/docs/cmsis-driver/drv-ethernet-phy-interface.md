---
id: "drv-ethernet-phy-interface"
type: "concept"
domain: "drivers"
title: "Ethernet PHY Interface"
summary: "Driver API for Ethernet PHY Peripheral (%DriverETHPHY.h) The following section describes the Ethernet PHY Interface as defined in the %DriverETHPHY.h header file."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_PHY.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_PHY.c"
license: "Apache-2.0"
mode: "V"
---

Driver API for Ethernet PHY Peripheral (%Driver_ETH_PHY.h)
 The following section describes the Ethernet PHY Interface as defined in the %Driver_ETH_PHY.h header file.

The %Driver_ETH_PHY.h contains two \#defines that are used to configure the connection between the PHY and the
microcontroller device:
- `ETH_PHY_NUM` and
- `ETH_PHY_ADDR`

Usually, the Serial Management Interface (**SMI)** (using MDC and MDIO) is used to access the PHY’s internal registers to read
the state of the link (up/down), duplex mode, speed, and to restart auto-negotiation etc. SMI is a serial bus, which allows
to connect up to 32 devices. Devices on the bus are accessed using a 5-bit device address. A default device address is
hardware configurable by pin-strapping on the device (some pins are sampled when a reset is asserted or at power-up).

The device’s internal weak pull-up or pull-down resistors define a default device address. This address can be changed by
connecting strong pull-up or pull-down resistors externally. In this case, the `ETH_PHY_ADDR` needs to be defined by the
user.

If a microcontroller device offers more than one Ethernet PHY driver, the user needs to set the correct `ETH_PHY_NUM` in his
application.
