---
id: "drv-ethernet-mac-interface-arm-eth-mac-control"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_Control"
summary: "The function ARM_ETH_MAC_Control controls the Ethernet MAC interface and executes various operations. After initialization, the Ethernet transceiver and receiver are disabled."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_MAC_Control (uint32_t control, uint32_t arg)
```


The function **ARM_ETH_MAC_Control** controls the Ethernet MAC interface and executes various operations. 
After initialization, the Ethernet transceiver and receiver are disabled.

The parameter **control** specifies an operation as defined in the table **Parameter **control**.** \n
The parameter **arg** provides, depending on the operation, additional information or values.

The table lists values for the parameter **control.**

Parameter **control**                                | Operation
:----------------------------------------------------|:--------------------------------------------
ARM_ETH_MAC_CONFIGURE                           | Configure the Ethernet MAC interface; For **arg** values, see table **Parameter **arg** for CONFIGURE**
ARM_ETH_MAC_CONTROL_TX                          | Enable or disable the transmitter; **arg** :  `0=disable; 1=enable`
ARM_ETH_MAC_CONTROL_RX                          | Enable or disable the receiver; **arg** :  `0=disable; 1=enable`
ARM_ETH_MAC_FLUSH                               | Flush a buffer; **arg** : see table **Parameter **arg** for FLUSH**
ARM_ETH_MAC_SLEEP                               | Exit/Enter Sleep mode; **arg** : `0=exit; 1=enter and wait for Magic packet`
ARM_ETH_MAC_VLAN_FILTER                         | Configure VLAN Filter for received frames;  **arg** : See table **Parameter **arg** for VLAN Filter**


The table **Parameter **arg** for CONFIGURE** lists the **arg** values for the **control** **ARM_ETH_MAC_CONFIGURE.**
The values can be ORed in the following way:
```
    mac->Control(ARM_ETH_MAC_CONFIGURE, ARM_ETH_MAC_SPEED_100M | ARM_ETH_MAC_DUPLEX_FULL | ARM_ETH_MAC_LOOPBACK);
```



| Parameter **arg** CONFIGURE |  |  |  |
|---|---|---|---|
| Parameter **arg** | Bit | Category | Description |
| ARM_ETH_MAC_SPEED_10M | 0..1 | Link Speed | Set the link speed to `10 [Mbps]` |
| ARM_ETH_MAC_SPEED_100M | Set the link speed to `100 [Mbps]` |  |  |
| ARM_ETH_MAC_SPEED_1G | Set the link speed to `1 [Gbps]` |  |  |
| ARM_ETH_MAC_DUPLEX_HALF | 2 | Link Mode | Set the link mode to half duplex |
| ARM_ETH_MAC_DUPLEX_FULL | Set the link mode to full duplex |  |  |
| n.a. | 3 | n.a. | **reserved** |
| ARM_ETH_MAC_LOOPBACK | 4 | Loopback Test Mode | Set the interface into a Loop-back test mode |
| ARM_ETH_MAC_CHECKSUM_OFFLOAD_RX | 5 | Receiver Checksum offload | Enable Receiver Checksum offload |
| ARM_ETH_MAC_CHECKSUM_OFFLOAD_TX | 6 | Transmitter Checksum offload | Enable Transmitter Checksum offload |
| ARM_ETH_MAC_ADDRESS_BROADCAST | 7 | Broadcast Frame address | Accept frames with Broadcast address |
| ARM_ETH_MAC_ADDRESS_MULTICAST | 8 | Multicast Frame address | Accept frames with any Multicast address |
| ARM_ETH_MAC_ADDRESS_ALL | 9 | Any Frame address | Accept frames with any address (Promiscuous Mode) |



The table **Parameter **arg** for FLUSH** lists the **arg** values for the **control** **ARM_ETH_MAC_FLUSH.**
The **arg** values can be ORed. 



| Parameter **arg** for FLUSH |  |  |  |
|---|---|---|---|
| Parameter **arg** | Bit | Category | Description |
| ARM_ETH_MAC_FLUSH_RX | 1 | Receive buffer | Flush the Receive buffer |
| ARM_ETH_MAC_FLUSH_TX | 2 | Transmit buffer | Flush the Transmit buffer |



The table **Parameter **arg** for VLAN Filter** lists the **arg** values for the **control** **ARM_ETH_MAC_VLAN_FILTER.**
The **arg** values can be ORed. 



| Parameter **arg** for VLAN Filter |  |  |  |
|---|---|---|---|
| Parameter **arg** | Bit | Category | Description |
| **value** | 0..15 | VLAN Tag | Set VLAN Tag value |
| `0` | 16 | Use of VLAN | Compare the complete 16-bit VLAN Tag value |
| ARM_ETH_MAC_VLAN_FILTER_ID_ONLY | Compare only the 12-bit VLAN Identifier |  |  |
| `0` | 0..16 | Disable | Disable the VLAN Filter |




**Example:**

```
...
                                         // start transfer
    mac->Control(ARM_ETH_MAC_CONFIGURE, ARM_ETH_MAC_SPEED_100M | ARM_ETH_MAC_DUPLEX_FULL | ARM_ETH_MAC_ADDRESS_BROADCAST);
    mac->Control(ARM_ETH_MAC_CONTROL_TX, 1);
    mac->Control(ARM_ETH_MAC_CONTROL_RX, 1);
	 
...                                      // stop transfer
    mac->Control(ARM_ETH_MAC_FLUSH, ARM_ETH_MAC_FLUSH_TX | ARM_ETH_MAC_FLUSH_RX);
    mac->Control(ARM_ETH_MAC_CONTROL_TX, 0);
    mac->Control(ARM_ETH_MAC_CONTROL_RX, 0);
  }
}
```

For a complete example, refer to  eth_interface_gr - Driver Functions.

******************************************************************************************************************
