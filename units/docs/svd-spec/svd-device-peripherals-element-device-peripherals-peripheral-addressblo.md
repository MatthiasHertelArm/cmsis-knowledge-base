---
id: "svd-device-peripherals-element-device-peripherals-peripheral-addressblo"
type: "concept"
domain: "pack"
title: "/device/peripherals element: /device/peripherals/peripheral/addressBlock element"
summary: "Specify an address range uniquely mapped to this peripheral. A peripheral must have at least one address block. If a peripheral is derived form another peripheral, the \\tagem{addressBlock} is not mandatory."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_peripherals.html"
license: "Apache-2.0"
mode: "V"
---

Specify an address range uniquely mapped to this peripheral. A peripheral must
have at least one address block. If a peripheral is derived form another peripheral, the \tagem{addressBlock} is not mandatory.

**/device/peripherals/peripheral/addressBlock**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| peripheral | elem_peripheral |  |  |
| Child Elements | Description | Type | Occurrence |
| offset | Specifies the start address of an address block relative to the peripheral **baseAddress. | scaledNonNegativeInteger | 1..1 |
| size | Specifies the number of addressUnitBits being covered by this address block. The end address of an address block results from the sum of baseAddress, offset, and (size - 1). | scaledNonNegativeInteger | 1..1 |
| usage | The following predefined values can be used: - `registers` - `buffer` - `reserved`. | enumerated token | 1..1 |
| protection | Set the protection level for an address block. | protectionStringType | 0..1 |



\delim_sec
