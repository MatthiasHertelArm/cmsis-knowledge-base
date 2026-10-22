---
id: "mcuboot-compressed-binary-file-internals-sample"
type: "concept"
domain: "boot-update"
title: "Compressed binary file internals: Sample"
summary: "For practical implementation, you can find a simple stand-alone verification program under the following path bootloader/mcuboot/samples/compression_test/independent_cmp.c"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/compression_format.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/compression_format.md#sample"
license: "Apache-2.0"
mode: "V"
---

For practical implementation, you can find a simple stand-alone
verification program under the following path
`bootloader/mcuboot/samples/compression_test/independent_cmp.c`

This program demonstrates how to independently verify the integrity and
authenticity of a decompressed image using the specified TLVs.
