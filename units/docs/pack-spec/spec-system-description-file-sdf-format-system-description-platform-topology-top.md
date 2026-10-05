---
id: "spec-system-description-file-sdf-format-system-description-platform-topology-top"
type: "concept"
domain: "pack"
title: "System Description File (*.SDF) Format: /system_description/platform/topology/topology_link"
summary: "Describes how CoreSight devices and cores are connected."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/sdf_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/sdf_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes how CoreSight devices and cores are connected.



| Parents | Element Chain |  |  |
|---|---|---|---|
| topology | /system_description/platform/topology |  |  |
| Attributes | Description | Type | Use |
| name | Unique name for the link. | xs:string | optional |
| type | Specifies the link type. Can be on of the following: ATB, CoreTrace, or CTITrigger. | xs:string | required |
| master | Unique name of the master device in the link. | xs:string | required |
| slave | Unique name of the slave device in the link. | xs:string | required |
| mater_interface | Specifies the mater interface number. | xs:string | optional |
| slave_interface | Specifies the slave interface number. | xs:string | optional |
| trigger | Specifies the trigger number. | xs:string | optional |



**Example:**

A complete set of links for a Cortex-A7 implementation with ETM and TPIU might look like this:
```
master="Cortex-A7_0" slave="CSCTI_6"     trigger="7"         type="CTITrigger"
master="CSETM_0"     slave="CSCTI_6"     trigger="6"         type="CTITrigger"
master="Cortex-A7_0" slave="CSETM_0"                         type="CoreTrace"
master="CSETM_0"     slave="CSTFunnel_2" slave_interface="0" type="ATB"
master="CSTFunnel_2" slave="CSTFunnel_0" slave_interface="1" type="ATB"
master="CSTFunnel_0" slave="CSTMC_0"                         type="ATB"
master="CSTMC_0"     slave="CSTPIU"                          type="ATB"
```
\delim
