---
id: "spec-system-description-file-sdf-format-system-description-platform-topology"
type: "concept"
domain: "pack"
title: "System Description File (*.SDF) Format: /system_description/platform/topology"
summary: "System Description File (*.SDF) Format: /system_description/platform/topology"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/sdf_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/sdf_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes the system topology.



| Parents | Element Chain |  |  |
|---|---|---|---|
| platform | /system_description/platform |  |  |
| Child Elements | Description | Type | Occurrence |
| sdf_element_topology_link | Describes how CoreSight devices and cores are connected. | complexType | 0..* |



**Example:**
```
<system_description version="2.0">
    <debug_and_trace_config>
    </debug_and_trace_config>
    <platform>
	    ...
        <topology>
            <!-- Trace Links -->
            <!-- Core Trace - Cortex-M4 -->
            <topology_link type="CoreTrace" master="CM4_CPU" slave="CM4_DWT"/>
            <topology_link type="CoreTrace" master="CM4_CPU" slave="CM4_ITM"/>
            <topology_link type="CoreTrace" master="CM4_CPU" slave="CM4_ETM"/>
            <topology_link type="ATB" master="CM4_ETM"       slave="CM4_TPIU" slave_interface="0"/>
            <topology_link type="ATB" master="CM4_ITM"       slave="CM4_TPIU" slave_interface="1"/>
            <!-- Trace - Cortex-M4 ETB (Direct Connection ETM -> ETB) -->
            <topology_link type="ATB" master="CM4_ETM"       slave="CM4_ETB"/>
        </topology>
    </platform>
</system_description>
```
\delim
