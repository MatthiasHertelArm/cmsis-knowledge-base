---
id: "drv-media-interface-types"
type: "concept"
domain: "drivers"
title: "Media Interface Types"
summary: "Encodes the supported media interface between Ethernet MAC and Ethernet PHY. The function ARM_ETH_MAC_GetCapabilities retrieves the media interface type encoded in the data field media_interface of the struct ARM_ETH_MAC_CAPABILITIES."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH.c"
license: "Apache-2.0"
mode: "V"
---

Ethernet Media Interface type

Encodes the supported media interface between Ethernet MAC and Ethernet PHY. 
The function ARM_ETH_MAC_GetCapabilities retrieves the media interface type encoded in the data field **media_interface** of the struct
 ARM_ETH_MAC_CAPABILITIES. 

**Parameter for:**
- ARM_ETH_PHY_SetInterface


### ARM_ETH_INTERFACE_MII

```c
ARM_ETH_INTERFACE_MII
```

\sa ARM_ETH_PHY_SetInterface

### ARM_ETH_INTERFACE_RMII

```c
ARM_ETH_INTERFACE_RMII
```

\sa ARM_ETH_PHY_SetInterface

### ARM_ETH_INTERFACE_SMII

```c
ARM_ETH_INTERFACE_SMII
```

\sa ARM_ETH_PHY_SetInterface

### ARM_ETH_INTERFACE_GMII

```c
ARM_ETH_INTERFACE_GMII
```

\sa ARM_ETH_PHY_SetInterface

### ARM_ETH_INTERFACE_RGMII

```c
ARM_ETH_INTERFACE_RGMII
```

\sa ARM_ETH_PHY_SetInterface

### ARM_ETH_INTERFACE_SGMII

```c
ARM_ETH_INTERFACE_SGMII
```

\sa ARM_ETH_PHY_SetInterface
