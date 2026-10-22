---
id: "mcuboot-compressed-binary-file-internals-tlvs"
type: "concept"
domain: "boot-update"
title: "Compressed binary file internals: TLVs"
summary: "The following Type-Length-Values (TLVs) are used in the context of decompressed images:"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/compression_format.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/compression_format.md#tlvs"
license: "Apache-2.0"
mode: "V"
---

The following Type-Length-Values (TLVs) are used in the context of
decompressed images:

-   `DECOMP_SIZE (0x70)`: Specifies the size of the decompressed image.
-   `DECOMP_SHA (0x71)`: Contains the hash of the decompressed image.
-   `DECOMP_SIGNATURE (0x72)`: Holds the signature of either the hash or
    the entire image.

These TLVs are placed in the protected TLV section, ensuring they are
included in the hashing and signature calculations during the
verification process. The process for choosing the type of cryptographic
signature and hash algorithm used for securing the image is the same,
regardless of whether the image has undergone compression.
