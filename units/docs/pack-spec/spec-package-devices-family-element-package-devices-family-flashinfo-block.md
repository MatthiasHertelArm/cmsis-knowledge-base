---
id: "spec-package-devices-family-element-package-devices-family-flashinfo-block"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../flashinfo/block"
summary: "Specify properties of one or multiple subsequent blocks of flash device that have the attributes. Its base address calculates from the parent \\<flashinfo> start address incremented by the size of all previous \\<block> and \\<gap> elements of this flash device."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Specify properties of one or multiple subsequent blocks of flash device that have the attributes.
Its base address calculates from the parent \`<flashinfo>` `start` address incremented by the
size of all previous \`<block>` and \`<gap>` elements of this flash device.




| Parents | Element Chain |  |  |
|---|---|---|---|
| flashinfo | element_flashinfo |  |  |
| Attributes | Description | Type | Use |
| count | Number of subsequent blocks of this flash device with identical properties. | NonNegativeInteger | required |
| size | Block size in bytes. The overall memory size that is covered by this \`<block>` element is `count` times `size`. | NonNegativeInteger | required |
| arg | An optional argument to pass to flash operation sequence. A debugger writes this value to the pre-defined debug access variable **__FlashArg** at start of a flash operation. It is a non-negative number specific to this device. Defaults to `0` if not specified. | NonNegativeInteger | optional |




\delim
