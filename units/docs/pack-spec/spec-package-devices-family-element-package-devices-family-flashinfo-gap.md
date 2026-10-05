---
id: "spec-package-devices-family-element-package-devices-family-flashinfo-gap"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../flashinfo/gap"
summary: "Specify a gap between \\<block> elements of the parent. Its base address calculates from the parent \\<flashinfo> start address incremented by the size of all previous \\<block> and \\<gap> elements of this flash device."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Specify a gap between \`<block>` elements of the parent.
Its base address calculates from the parent \`<flashinfo>` `start` address incremented by the
size of all previous \`<block>` and \`<gap>` elements of this flash device.



| Parents | Element Chain |  |  |
|---|---|---|---|
| flashinfo | element_flashinfo |  |  |
| Attributes | Description | Type | Use |
| size | Gap size in bytes. | NonNegativeInteger | required |
