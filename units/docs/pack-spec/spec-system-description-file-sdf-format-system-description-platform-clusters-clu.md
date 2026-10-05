---
id: "spec-system-description-file-sdf-format-system-description-platform-clusters-clu"
type: "concept"
domain: "pack"
title: "System Description File (*.SDF) Format: /system_description/platform/clusters/cluster"
summary: "Lists the devices that make up the cluster."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/sdf_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/sdf_pg.html"
license: "Apache-2.0"
mode: "V"
---

Lists the devices that make up the cluster.



| Parents | Element Chain |  |  |
|---|---|---|---|
| clusters | /system_description/platform/clusters |  |  |
| Attributes | Description | Type | Use |
| name | Unique name for the cluster (for example Cortex-A15_SMP_0). | xs:string | required |
| devices | Colon separated list of named devices in the cluster, for example "Cortex-A15_0:Cortex-A15_1:Cortex-A15_2:Cortex-A15_3". | xs:string | required |



\delim
