---
id: "spec-system-description-file-sdf-format-system-description"
type: "concept"
domain: "pack"
title: "System Description File (*.SDF) Format: /system_description"
summary: "System Description File (*.SDF) Format: /system_description"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/sdf_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/sdf_pg.html"
license: "Apache-2.0"
mode: "V"
---

| Parents | Element Chain |  |  |
|---|---|---|---|
| root | description root point for SDF |  |  |
| Attributes | Description | Type | Use |
| schemaVersion | Version of sdf_schema.xsd the description is compatible with | xs:decimal | required |
| Child Elements | Description | Type | Occurrence |
| sdf_element_debug_and_trace_config | Description how to configure debug and trace. | complexType | 1..1 |
| sdf_element_platform | Overall platform description. | complexType | 1..1 |



\delim
