---
id: "mcuboot-custom-crypto-backend-minimal-example-structure"
type: "concept"
domain: "boot-update"
title: "Custom Crypto Backend: Minimal example structure"
summary: "Add my_board/crypto/ to the include path and compile my_enc.c when MCUBOOT_ENC_IMAGES is enabled. MCUboot will resolve all crypto calls through the types and functions you define."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/custom_crypto.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/custom_crypto.md#minimal-example-structure"
license: "Apache-2.0"
mode: "V"
---

```
my_board/
  crypto/
    mcuboot_custom_crypto.h   ← dispatcher — includes the headers below
    my_sha.h                  ← SHA-256 context + functions
    my_ecdsa.h                ← ECDSA-P256 context + functions
    my_enc.c                  ← boot_enc_* symbols (if MCUBOOT_ENC_IMAGES)
```

`mcuboot_custom_crypto.h`:

```c
#ifndef MCUBOOT_CUSTOM_CRYPTO_H
#define MCUBOOT_CUSTOM_CRYPTO_H

#include "my_sha.h"
#include "my_ecdsa.h"
#if defined(MCUBOOT_ENC_IMAGES)
#include "my_hmac_sha256.h"
#include "my_aes_ctr.h"
#include "my_ecdh_p256.h"
#endif

#endif /* MCUBOOT_CUSTOM_CRYPTO_H */
```

Add `my_board/crypto/` to the include path and compile `my_enc.c` when
`MCUBOOT_ENC_IMAGES` is enabled.  MCUboot will resolve all crypto calls
through the types and functions you define.
