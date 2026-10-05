---
id: "drv-ethernet-interface"
type: "concept"
domain: "drivers"
title: "Ethernet Interface"
summary: "Ethernet common definitions (%DriverETH.h)"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH.c"
license: "Apache-2.0"
mode: "V"
---

Ethernet common definitions (%Driver_ETH.h)


**Ethernet** is a networking technology for exchanging data packages between computer systems. Several microcontrollers integrate 
an Ethernet MAC (Media Access Control) data-link layer that interfaces to an Ethernet PHY (Physical Interface Transceiver).

Wikipedia offers more information about 
the **Ethernet**.


**Block Diagram**

The Ethernet PHY connects typically to the Ethernet MAC using an MII (Media Independent Interface) or RMII (Reduced Media Independent Interface).

\n
  "Block Diagram of a typical Ethernet Interface"


**Ethernet API**

The following header files define the Application Programming Interface (API) for the **Ethernet** interface:
 - **%Driver_ETH.h** : Common definitions of the Ethernet PHY and MAC part
 - **%Driver_ETH_MAC.h** : API for the Ethernet MAC
 - **%Driver_ETH_PHY.h** : API for the Ethernet PHY
 
The driver implementation of the Ethernet MAC is a typical part of a Device Family Pack (DFP) that supports the peripherals of the microcontroller family.
The driver implementation of the Ethernet PHY is a typical part of a **Network** Software Pack, since PHY is typically not integrated into the microcontroller.

**Note:**
For parameters, the value marked with (default) is the setting after the driver initialization.


**Driver Functions**

The driver functions are published in the access struct as explained in DriverFunctions
 - ARM_DRIVER_ETH_MAC : access struct for **Ethernet MAC** driver functions.
 - ARM_DRIVER_ETH_PHY : access struct for **Ethernet PHY** driver functions.

Both drivers are used in combination and usually the Ethernet MAC provides a media interface to the Ethernet PHY.
A typical setup sequence for the drivers is shown below:

**Example Code**

The following example code shows the usage of the Ethernet interface.

```
extern ARM_DRIVER_ETH_MAC Driver_ETH_MAC0;
extern ARM_DRIVER_ETH_PHY Driver_ETH_PHY0;
 
static ARM_DRIVER_ETH_MAC *mac;
static ARM_DRIVER_ETH_PHY *phy;
static ARM_ETH_MAC_ADDR          own_mac_address;
static ARM_ETH_MAC_CAPABILITIES  capabilities;
 
void ethernet_mac_notify (uint32_t event)  {
  switch (event)  {
     :
  }  
}
 
 
void initialize_ethernet_interface (void) {
  mac = &Driver_ETH_MAC0;
  phy = &Driver_ETH_PHY0;
 
  // Initialize Media Access Controller
  capabilities = mac->GetCapabilities ();
   
  mac->Initialize (ethernet_mac_notify);
  mac->PowerControl (ARM_POWER_FULL);
 
  if (capabilities.mac_address == 0)  {
    // populate own_mac_address with the address to use
    mac->SetMacAddress(&own_mac_address);
  }
  else {
    mac->GetMacAddress(&own_mac_address);
  }
 
  // Initialize Physical Media Interface
  if (phy->Initialize (mac->PHY_Read, mac->PHY_Write) == ARM_DRIVER_OK) {
    phy->PowerControl (ARM_POWER_FULL);
    phy->SetInterface (capabilities.media_interface);
    phy->SetMode (ARM_ETH_PHY_AUTO_NEGOTIATE);
  }
    :
    :
}
 
 
static ARM_ETH_LINK_STATE ethernet_link;   // current link status
 
void ethernet_check_link_status (void) {
  ARM_ETH_LINK_STATE link;
 
  link = phy->GetLinkState ();
  if (link == ethernet_link) {    
    return;                                // link state unchanged
  }
                                           // link state changed
  ethernet_link = link;   
  if (link == ARM_ETH_LINK_UP) {      // start transfer
    ARM_ETH_LINK_INFO info = phy->GetLinkInfo ();
    mac->Control(ARM_ETH_MAC_CONFIGURE,
                 info.speed  << ARM_ETH_MAC_SPEED_Pos  |
                 info.duplex << ARM_ETH_MAC_DUPLEX_Pos |
                 ARM_ETH_MAC_ADDRESS_BROADCAST);
    mac->Control(ARM_ETH_MAC_CONTROL_TX, 1);
    mac->Control(ARM_ETH_MAC_CONTROL_RX, 1);
  }
  else {                                   // stop transfer
    mac->Control(ARM_ETH_MAC_FLUSH, ARM_ETH_MAC_FLUSH_TX | ARM_ETH_MAC_FLUSH_RX);
    mac->Control(ARM_ETH_MAC_CONTROL_TX, 0);
    mac->Control(ARM_ETH_MAC_CONTROL_RX, 0);
  }
}

```
