---
id: "tfm-symmetric-key-algorithm-based-init-hal-apis"
type: "concept"
domain: "security"
title: "Symmetric key algorithm based Initial Attestation: HAL APIs"
summary: "tfm_plat_get_symmetric_iak() fetches device symmetric IAK."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/symmetric_initial_attest.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/symmetric_initial_attest.html#hal-apis"
license: "BSD-3-Clause"
mode: "V"
---

HAL APIs are summarized below.


### Fetch device symmetric IAK


`tfm_plat_get_symmetric_iak()` fetches device symmetric IAK.

```c

enum tfm_plat_err_t tfm_plat_get_symmetric_iak(uint8_t *key_buf,
                                               size_t buf_len,
                                               size_t *key_len,
                                               psa_algorithm_t *key_alg);
```
  **Parameters:**

  +-------------+-----------------------------------------------------------+
  | `key_buf` | Buffer to store the symmetric IAK.                        |
  +-------------+-----------------------------------------------------------+
  | `buf_len` | The length of `key_buf`.                                |
  +-------------+-----------------------------------------------------------+
  | `key_len` | The length of the symmetric IAK.                          |
  +-------------+-----------------------------------------------------------+
  | `key_alg` | The key algorithm. Only HMAC SHA-256 is supported so far. |
  +-------------+-----------------------------------------------------------+

It returns error code specified in `enum tfm_plat_err_t`.


### Get symmetric IAK key identifier


`attest_plat_get_symmetric_iak_id()` gets the key identifier of the symmetric
IAK as the `kid` parameter in COSE Header.

Optional if device doesn't install a key identifier for symmetric IAK.

```c

enum tfm_plat_err_t attest_plat_get_symmetric_iak_id(void *kid_buf,
                                                     size_t buf_len,
                                                     size_t *kid_len);
```
  **Parameters:**

  +-------------+-------------------------------------+
  | `kid_buf` | Buffer to store the IAK identifier. |
  +-------------+-------------------------------------+
  | `buf_len` | The length of `kid_buf`.          |
  +-------------+-------------------------------------+
  | `kid_len` | The length of the IAK identifier.   |
  +-------------+-------------------------------------+

It returns error code specified in `enum tfm_plat_err_t`.
