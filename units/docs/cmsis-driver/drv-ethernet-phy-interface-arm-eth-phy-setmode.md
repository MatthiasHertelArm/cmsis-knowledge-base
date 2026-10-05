---
id: "drv-ethernet-phy-interface-arm-eth-phy-setmode"
type: "concept"
domain: "drivers"
title: "Ethernet PHY Interface: ARM_ETH_PHY_SetMode"
summary: "The function ARMETHPHYSetMode sets the operation mode parameters for the Ethernet PHY."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_PHY.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_PHY.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_PHY_SetMode (uint32_t mode)
```


The function **ARM_ETH_PHY_SetMode** sets the operation mode parameters for the Ethernet PHY.


The table below lists the possible values for the parameter **mode.** Values from different categories can be ORed as shown in this example code:

```
phy->SetMode (ARM_ETH_PHY_SPEED_100M | ARM_ETH_PHY_LOOPBACK | ARM_ETH_PHY_DUPLEX_HALF );
```
\n



| Parameter **mode**               |  bit               |  Category               |  Description | 

| ARM_ETH_PHY_SPEED_10M       |  0..1  | Link Speed  |  Set the link speed to `10 [Mbps]`      | 

| ARM_ETH_PHY_SPEED_100M      |                                                       Set the link speed to `100 [Mbps]`           | 

| ARM_ETH_PHY_SPEED_1G        |                                                       Set the link speed to `1  [Gbps]`            | 

| ARM_ETH_PHY_DUPLEX_HALF     |  2     | Link Mode   |  Set the link mode to half duplex             | 

| ARM_ETH_PHY_DUPLEX_FULL     |                                                       Set the link mode to full duplex                   | 

| ARM_ETH_PHY_AUTO_NEGOTIATE  |            3       | Autonegotiation         |  Set the interface to Auto Negotiation mode of transmission parameters | 

| ARM_ETH_PHY_LOOPBACK        |            4       | Loopback                |  Set the interface into a Loop-back test mode       | 

| ARM_ETH_PHY_ISOLATE         |            5       | Isolation               |  Set to indicate electrical isolation of PHY interface from MII/RMII interface | 



**Note:**
Some settings may be also taken from configuration pins (example ARM_ETH_PHY_ISOLATE). Check the effect of mode settings in the actual driver implementation.
**Note:**
Some **mode** values may be unsupported by a driver implementation. For example ARM_ETH_PHY_SPEED_1G may return **ARM_DRIVER_ERROR_UNSUPPORTED.**


**Example:**
```
static ARM_ETH_MAC_CAPABILITIES capabilities;
static ARM_DRIVER_ETH_MAC *mac;
static ARM_DRIVER_ETH_PHY *phy;
 
mac = &Driver_ETH_MAC0;
phy = &Driver_ETH_PHY0;
 
// Initialize Media Access Controller
capabilities = mac->GetCapabilities ();
...
status = phy->SetInterface (capabilities.media_interface);
if (status != ARM_DRIVER_OK) ...  // error handling
status = phy->SetMode (ARM_ETH_PHY_SPEED_100M | ARM_ETH_PHY_DUPLEX_FULL | ARM_ETH_PHY_ISOLATE);
if (status != ARM_DRIVER_OK) ...  // error handling
...
```



****************************************************************************************************************
