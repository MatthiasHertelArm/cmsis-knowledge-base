---
id: "mcuboot-custom-crypto-backend-build-requirements"
type: "concept"
domain: "boot-update"
title: "Custom Crypto Backend: Build requirements"
summary: "Custom Crypto Backend: Build requirements"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/custom_crypto.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/custom_crypto.md#build-requirements"
license: "Apache-2.0"
mode: "V"
---

| Step | Action |
|------|--------|
| 1. Compiler define | `-DMCUBOOT_USE_CUSTOM_CRYPTO` |
| 2. Include order | Ensure your custom header is included before `bootutil/crypto/*.h` |
| 3. Source files | Compile `.c` files that back your custom implementations |
| 4. Link | Link any required libraries from your crypto SDK |

**Note:** The simplest way to ensure correct include order is to use a
force-include compiler flag (e.g., `-include mcuboot_custom_crypto.h` with GCC)
or include your custom header at the top of `mcuboot_config.h`.
