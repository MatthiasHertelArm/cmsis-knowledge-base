---
id: "drv-ethernet-mac-control-codes"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Control Codes"
summary: "Configure and control the Ethernet MAC using the ARMETHMACControl."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

Configure and control the Ethernet MAC using the ARM_ETH_MAC_Control.
 
Many parameters of the Ethernet MAC driver are configured using the ARM_ETH_MAC_Control function.

The various Ethernet MAC control codes define:
  
  - eth_mac_ctrls                configures and controls the Ethernet MAC interface
  - eth_mac_configuration_ctrls  specifies speed mode, link mode, checksum, and frame filtering modes
  - eth_mac_flush_flag_ctrls     specify controls to flush a buffer
  - eth_mac_vlan_filter_ctrls    specifies whether to compare only the VLAN Identifier

Refer to the ARM_ETH_MAC_Control function for further details.
