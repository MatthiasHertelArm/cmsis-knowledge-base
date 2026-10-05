---
id: "mcuboot-custom-crypto-backend-enabling-the-custom-backend"
type: "concept"
domain: "boot-update"
title: "Custom Crypto Backend: Enabling the custom backend"
summary: "Define exactly one crypto backend macro in your mcuboot_config.h (or via a compiler flag):"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/custom_crypto.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/custom_crypto.md#enabling-the-custom-backend"
license: "Apache-2.0"
mode: "V"
---

Define exactly one crypto backend macro in your `mcuboot_config.h` (or via a
compiler flag):

```c
#define MCUBOOT_USE_CUSTOM_CRYPTO
```

Do **not** define any other `MCUBOOT_USE_*` crypto backend at the same time —
that is a compile-time error.
