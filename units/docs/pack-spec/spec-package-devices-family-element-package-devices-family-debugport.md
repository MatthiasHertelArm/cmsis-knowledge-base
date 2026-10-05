---
id: "spec-package-devices-family-element-package-devices-family-debugport"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../debugport"
summary: "Describes a CoreSight debug port of the device and its capabilities. The element can occur on various levels. Use unique ID values for the attribute _dp to distinguish multiple debugport elements in later references."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes a CoreSight debug port of the device and its capabilities. The element can occur on various
levels. Use unique ID values for the attribute **__dp** to distinguish multiple **debugport**
elements in later references.

**debugport** elements are required for targets with multiple debug ports. These elements can be omitted
for devices with a single debug port. If no **debugport** element exists, then the only
allowed **__dp** ID in later references is `0`.

**Example**
```
<family Dfamily="LPC4300 Series" Dvendor="NXP:11">
  ...
  <debugconfig default="jtag" clock="10000000" swj="1"/>
  
  <debugport __dp="0">
    <jtag tapindex="0"/>
    <swd/>
  </debugport>
  
  <debugport __dp="1">
    <jtag tapindex="1"/> 
  </debugport>
  ...
</family>
```


 	



| Parents | Element Chain |  |  |
|---|---|---|---|
| family | element_family |  |  |
| subFamily | element_subFamily |  |  |
| device | element_device |  |  |
| Attributes | Description | Type | Use |
| __dp | Unique ID of this **debugport**. It must be used consistently in references within the scope of the parent section. | xs:unsignedInt | required |
| Child Elements | Description | Type | Occurrence |
| jtag | Describe JTAG Test Access Port (TAP) properties of this debug port. | JtagType | 0..1 |
| swd | Describe CoreSight Serial Wire Debug Port (SW-DP) properties of this debug port. | SwdType | 0..1 |
| cjtag | Describe CJTAG Test Access Port (TAP) properties of this debug port. | CjtagType | 0..1 |
