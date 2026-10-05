---
id: "mcuboot-compressed-binary-file-internals"
type: "concept"
domain: "boot-update"
title: "Compressed binary file internals"
summary: "This article describes the structure of the zephyr.signed.bin file when image compression is enabled."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/compression_format.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/compression_format.md"
license: "Apache-2.0"
mode: "V"
---

This article describes the structure of the
`zephyr.signed.bin` file when image
compression is enabled. You do not need to know these details to use the
image compression subsystem, but they can be beneficial if you want to
use them for verification or custom integration purposes.

For an example, see the following structure of the file:

(figure: LZMA header)
