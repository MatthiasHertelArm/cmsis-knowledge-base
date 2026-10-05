---
id: "mcuboot-custom-crypto-backend"
type: "concept"
domain: "boot-update"
title: "Custom Crypto Backend"
summary: "MCUboot's crypto abstraction layer supports several open source backends like MCUBOOT_USE_MBED_TLS, MCUBOOT_USE_TINYCRYPT, etc."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/custom_crypto.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/custom_crypto.md"
license: "Apache-2.0"
mode: "V"
---

MCUboot's crypto abstraction layer supports several open source backends like
`MCUBOOT_USE_MBED_TLS`, `MCUBOOT_USE_TINYCRYPT`, etc. The
`MCUBOOT_USE_CUSTOM_CRYPTO` option allows to implement a custom backend that
lets users plug in any crypto library —
hardware accelerator, proprietary SDK, or another software implementation —
without modifying MCUboot's own source.
