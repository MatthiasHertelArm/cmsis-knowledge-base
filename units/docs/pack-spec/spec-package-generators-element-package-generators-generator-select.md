---
id: "spec-package-generators-element-package-generators-generator-select"
type: "concept"
domain: "pack"
title: "/package/generators element: /package/generators/generator/select"
summary: "This element contains information about the vendor and device the GPDSC file has been generated for. Only one such element can exist in \\<generator>."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/generators_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element contains information about the vendor and device the GPDSC file has been generated for. Only one such
element can exist in \`<generator>`.

**Example:**
```
  <generators>
    <generator id="STM32CubeMX" Gvendor="STMicroelectronics" Gtool="STM32CubeMX" Gversion="4.10.0">
      <select Dname="STM32F746NGHx" Dvendor="STMicroelectronics:13"/>
    </generator>
  </generators>
```

 



| Parent | Chain |  |  |
|---|---|---|---|
| generator | element_generator |  |  |
| Attributes | Description | Type | Use |
| Dvendor | Vendor name of the targeted device. Use predefined values as listed in the table Device Vendor. | DeviceVendorEnum | required |
| Dname | Name of the targeted device. If no Dvariant is specified this tag is required | xs:string | optional |
| Dvariant | Name of the targeted device variant. If a variant is specified, the device name will be ignored and the variant rules. If no Dname is specified, this tag is required. | xs:string | optional |
| Pname | Name of the targeted processor of a device with multiple processors. For devices with multiple processors this tag is required. | xs:string | optional |
