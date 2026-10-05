---
id: "svd-device-peripherals-peripheral-regi-device-peripherals-peripheral-registers-6"
type: "concept"
domain: "pack"
title: "/device/peripherals/peripheral/registers element: /device/peripherals/peripheral/registers/.../enumeratedValue element"
summary: "An enumeratedValue defines a map between an unsigned integer and a string."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_registers.html"
license: "Apache-2.0"
mode: "V"
---

An **enumeratedValue** defines a map between an unsigned integer and a string.


**/device/peripherals/peripheral/registers/.../enumeratedValue**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<enumeratedValues>` | elem_enumeratedValues |  |  |
| `<dimArrayIndex>` | elem_dimArrayIndex |  |  |
| Child Elements | Description | Type | Occurrence |
| name | String describing the semantics of the value. Can be displayed instead of the value. | identifierType | 0..1 |
| description | Extended string describing the value. | xs:string | 0..1 |
| choice of | 1..1 |  |  |
| value | Defines the constant for the bit-field as decimal, hexadecimal (0x...) or binary (0b... or #...) number. E.g.: \`<value>`15\`</value>` \`<value>`0xf\`</value>` \`<value>`0b1111\`</value>` \`<value>`#1111\`</value>` In addition the binary format supports 'do not care' bits represented by **`x`**. E.g. specifying value 14 and 15 as: \`<value>`0b111x\`</value>` \`<value>`#111x\`</value>` | scaledNonNegativeInteger | 0..1 |
| isDefault | Defines the name and description for all other values that are not listed explicitly. | xs:boolean | 0..1 |
