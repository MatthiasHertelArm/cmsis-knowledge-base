---
id: "mcuboot-ecdsa-signature-format-background"
type: "concept"
domain: "boot-update"
title: "ECDSA signature format: Background"
summary: "ECDSA signatures are encoded as ASN.1, notably with the signature itself encoded as follows:"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/ecdsa.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/ecdsa.md#background"
license: "Apache-2.0"
mode: "V"
---

ECDSA signatures are encoded as ASN.1, notably with the signature
itself encoded as follows:

```
    ECDSA-Sig-Value ::= SEQUENCE {
      r  INTEGER,
      s  INTEGER
    }
```

Both `r` and `s` are 256-bit numbers. Because these are
unsigned numbers that are being encoded in ASN.1 as signed values, if
the high bit of the number is set, the DER-encoded representation will
require 33 bytes instead of 32. This means that the length of the
signature will vary by a couple of bytes, depending on whether one or
both of these numbers have the high bit set.

Originally, MCUboot added padding to the entire signature and just
removed any trailing 0 bytes from the data block. This turned out to be fine 255 out of 256
times, each time the last byte of the signature was non-zero, but if the
signature ended in a zero, MCUboot would remove too many bytes and render the
signature invalid.

The correct approach here is to accept that ECDSA signatures are of
variable length, and to make sure that we can handle them as such.
