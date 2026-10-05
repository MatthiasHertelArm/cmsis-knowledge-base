---
id: "mcuboot-custom-crypto-backend-how-it-works"
type: "concept"
domain: "boot-update"
title: "Custom Crypto Backend: How it works"
summary: "When MCUBOOT_USE_CUSTOM_CRYPTO is defined, the crypto abstraction headers (sha.h, ecdsa.h, hmac_sha256.h, aes_ctr.h, ecdh_p256.h) do not define any types or functions for the custom crypto path. Instead, you must provide them via your platform's custom crypto header."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/custom_crypto.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/custom_crypto.md#how-it-works"
license: "Apache-2.0"
mode: "V"
---

When `MCUBOOT_USE_CUSTOM_CRYPTO` is defined, the crypto abstraction headers
(`sha.h`, `ecdsa.h`, `hmac_sha256.h`, `aes_ctr.h`, `ecdh_p256.h`) do not
define any types or functions for the custom crypto path. Instead, you must
provide them via your platform's custom crypto header.

Your custom header must be included **before** any bootutil crypto headers.
The simplest approach is to add your header's directory to the compiler include
path and have every translation unit include your custom header first (e.g.,
via a force-include compiler flag or by including it at the top of
`mcuboot_config.h`).
