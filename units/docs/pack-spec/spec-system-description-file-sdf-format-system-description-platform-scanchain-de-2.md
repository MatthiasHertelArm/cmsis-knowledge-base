---
id: "spec-system-description-file-sdf-format-system-description-platform-scanchain-de-2"
type: "concept"
domain: "pack"
title: "System Description File (*.SDF) Format: /system_description/platform/scanchain/../../device_info_items"
summary: "The device information items are specific to the type of device or DAP and describe implementation specific details. Refer to sdf_element_device_info_item for a list of applicable device information items and a code example."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/sdf_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/sdf_pg.html"
license: "Apache-2.0"
mode: "V"
---

The device information items are specific to the type of device or DAP and describe implementation specific details. Refer to
sdf_element_device_info_item for a list of applicable device information items and a code example.



| Parents | Element Chain |  |  |
|---|---|---|---|
| device | /system_description/platform/../device |  |  |
| dap | /system_description/platform/scanchain/dap |  |  |
| Child Elements | Description | Type | Occurrence |
| sdf_element_device_info_item | Describes a sequence of device information items. | xs:string | 0..* |



\delim
