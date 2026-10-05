---
id: "mcuboot-compressed-binary-file-internals-extracting-lzma-stream-from-image-extrac"
type: "concept"
domain: "boot-update"
title: "Compressed binary file internals: [Extracting LZMA stream from image](#Extracting-LZMA-stream-from-image)"
summary: "To extract and decompress the LZMA stream from the image, follow these steps:"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/compression_format.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/compression_format.md#extracting-lzma-stream-from-image-extracting-lzma-stream-from-image"
license: "Apache-2.0"
mode: "V"
---

To extract and decompress the LZMA stream from the image, follow these
steps:

1.  Determine the offset of the compressed stream by adding the
    `lzma2_header` size and the value stored under
    `image_header.ih_hdr_size`. For the size of the compressed stream,
    see `image_header.ih_img_size`.
2.  If the compressed stream is isolated and stored in a file named
    `raw.lzma`, you can perform
    decompression using the following commands:

 -   Without an ARM thumb filter:

     ```bash
     unlzma --lzma2 --format=raw --suffix=.lzma raw.lzma
     ```

 -   With an ARM thumb filter:

     ```bash
     unlzma --armthumb --lzma2 --format=raw --suffix=.lzma raw.lzma
     ```

Once the command is executed you will see a newly created file named
`raw`, which is identical to the
image before compression.
