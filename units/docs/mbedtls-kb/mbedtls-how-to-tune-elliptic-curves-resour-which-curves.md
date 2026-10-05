---
id: "mbedtls-how-to-tune-elliptic-curves-resour-which-curves"
type: "concept"
domain: "security"
title: "How to tune Elliptic Curves resource usage: Which curves?"
summary: "This page refers to \"short Weierstrass\" form curves. This includes NIST, Brainpool, and \"Koblitz\" curves such as the one used by Bitcoin—in short, all except newer curves like Curve25519 and Curve448."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/how-do-i-tune-elliptic-curves-resource-usage.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/how-do-i-tune-elliptic-curves-resource-usage.md#which-curves"
license: "Apache-2.0"
mode: "V"
---

This page refers to "short Weierstrass" form curves. This includes NIST, Brainpool, and "Koblitz" curves such as the one used by Bitcoin—in short, all except newer curves like Curve25519 and Curve448.

On the reference machine, Curve25519 performed 358 ECDHE/s (ephemeral Elliptic Curve Diffie-Hellman key exchanges per second) using around 1500 bytes on the heap.
