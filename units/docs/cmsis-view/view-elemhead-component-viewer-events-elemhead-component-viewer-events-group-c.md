---
id: "view-elemhead-component-viewer-events-elemhead-component-viewer-events-group-c"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/events}: \\elemhead{component_viewer/events/group/component}"
summary: "Define software components that are tied to an event number."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Define software components that are tied to an event number.



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| group | elem_group |  |  |
| Attributes | Description | Type | Use |
| name | Descriptive component name. | xs:string | required |
| brief | Short component name for display purposes. | xs:string | required |
| no | Event id component number (bits 8..15). See er_theory. | xs:string | required |
| prefix | Added to hyperlink in context sensitive help system before the \`<event name\>`. | xs:string | required |
| info | Descriptive text shown when hovering over the component brief. | xs:string | optional |
| Child Element | Description | Type | Occurrence |
| \refelem{elem_group_component_state,state} | State information for a component | ComponentType | 0..* |


 
**Example:**
```
<events>	  
<!-- event groups for Network Component --> 
  <group name="Network">
    <group name="System Events">
      <component name="Memory Management"      brief="NetMM"    no="0x80" prefix="EvrNetMM_"    info="Network - System - Dynamic Memory Management"/>
      <component name="ETH Interface"          brief="NetETH"   no="0x81" prefix="EvrNetETH_"   info="Network - System - Ethernet Interface"/>
      <component name="PPP Interface"          brief="NetPPP"   no="0x82" prefix="EvrNetPPP_"   info="Network - System - Serial PPP Interface"/>
      <component name="SLIP Interface"         brief="NetSLIP"  no="0x83" prefix="EvrNetSLIP_"  info="Network - System - Serial SLIP Interface"/>
      <component name="Loopback Interface"     brief="NetLB"    no="0x84" prefix="EvrNetLB_"    info="Network - System - Local Loopback Interface"/> 
    </group>
 
    <group name="IPv4 Core Events">
      <component name="IP4 Core"               brief="NetIP4C"  no="0x85" prefix="EvrNetIP4C_"  info="Network - IPv4 - Core/localhost"/>
      <component name="ICMP Control"           brief="NetICMP"  no="0x86" prefix="EvrNetICMP_"  info="Network - IPv4 - Internet Control Message"/>
      <component name="IGMP Management"        brief="NetIGMP"  no="0x87" prefix="EvrNetIGMP_"  info="Network - IPv4 - Internet Group Message (multicast)"/>
      <component name="NBNS Client"            brief="NetNBNS"  no="0x88" prefix="EvrNetNBNS_"  info="Network - IPv4 - NetBIOS Name Service Client"/>
      <component name="DHCP Client"            brief="NetDHCP"  no="0x89" prefix="EvrNetDHCP_"  info="Network - IPv4 - Dynamic Host Client"/>
      <component name="ARP Address Resolution" brief="NetARP"   no="0x8A" prefix="EvrNetARP_"   info="Network - IPv4 - Ethernet Address Resolution"/>
    </group>
  
   <group name="IPv6 Core Events">
      <component name="IP6 Core"               brief="NetIP6C"  no="0x8B" prefix="EvrNetIP6C_"  info="Network - IPv6 - Core/localhost"/>
      <component name="ICMP6 Control"          brief="NetICMP6" no="0x8C" prefix="EvrNetICMP6_" info="Network - IPv6 - Internet Control Message"/>
      <component name="DHCP6 Client"           brief="NetDHCP6" no="0x8D" prefix="EvrNetDHCP6_" info="Network - IPv6 - Dynamic Host Client"/>
      <component name="NDP Neighbor Discovery" brief="NetNDP"   no="0x8E" prefix="EvrNetNDP_"   info="Network - IPv4 - Neighbor Discovery"/>
    </group>
  </group>
  :
  :
</events>
```
