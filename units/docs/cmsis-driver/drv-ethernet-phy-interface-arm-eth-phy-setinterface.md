---
id: "drv-ethernet-phy-interface-arm-eth-phy-setinterface"
type: "concept"
domain: "drivers"
title: "Ethernet PHY Interface: ARM_ETH_PHY_SetInterface"
summary: "The function ARM_ETH_PHY_SetInterface specifies the eth_interface_types1 that links the Ethernet MAC and Ethernet PHY. After initialization of the PHY interface, you can set the media type."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_PHY.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_PHY.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_PHY_SetInterface (uint32_t interface)
```



The function **ARM_ETH_PHY_SetInterface** specifies the eth_interface_types1 that links the Ethernet MAC and Ethernet PHY. 
After initialization of the PHY interface, you can set the media type.
The function ARM_ETH_MAC_GetCapabilities retrieves the media interface type encoded in the data field **media_interface** of the structure
ARM_ETH_MAC_CAPABILITIES. 

The parameter **interface** can have the following values:

Parameter **interface**       | Media Type
:-----------------------------|:-------------------------
ARM_ETH_INTERFACE_MII    | Media Independent Interface (MII)
ARM_ETH_INTERFACE_RMII   | Reduced Media Independent Interface (RMII)
ARM_ETH_INTERFACE_SMII   | Serial Media Independent Interface (SMII)
ARM_ETH_INTERFACE_GMII   | Gigabit Media Independent Interface (GMII)
ARM_ETH_INTERFACE_RGMII  | Reduced Gigabit Media Independent Interface (RGMII)
ARM_ETH_INTERFACE_SGMII  | Serial Gigabit Media Independent Interface (SGMII)

**Note:**
Some **interface** values may be unsupported by a driver implementation. For example ARM_ETH_INTERFACE_SMII may return **ARM_DRIVER_ERROR_UNSUPPORTED.**

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
status = phy->SetMode (ARM_ETH_PHY_AUTO_NEGOTIATE);
if (status != ARM_DRIVER_OK) ...  // error handling
...
```
****************************************************************************************************************
