---
id: "tfm-fixing-implicit-casting-for-c-enum-design-proposal-for-tf-m"
type: "concept"
domain: "security"
title: "Fixing implicit casting for C enumeration values: Design proposal for TF-M"
summary: "In TF-M, an action will be taken for all enumerated types and enumeration constants that are used for implicit casting. The goal of this proposal is to remove all implicit casting of enumeration values in TF-M."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/software/enum_implicit_casting.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/enum_implicit_casting.html#design-proposal-for-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

In TF-M, an action will be taken for all enumerated types and enumeration
constants that are used for implicit casting. The goal of this proposal is to
remove all implicit casting of enumeration values in TF-M.

The following enumerated types will be removed and replaced with preprocessor
constants (strategy 0). These enumerated types are not used in TF-M
but only the constants they declare.

* `enum spm_part_state_t`
* `enum spm_part_flag_mask_t`
* `enum tfm_partition_priority`

The following enumerated types will be kept because they are used in the
prototypes of functions and are useful for debugging. Whenever possible,
strategy 1 will be applied to remove implicit casting related with those
enumerations but dynamic conversions will be used if the first option would
create too much change in the code base.

* `enum tfm_status_e`: the return type of the following functions will be
  changed to return the `enum tfm_status_e` type. These functions are already
  returning the enumeration constants, but implicitly casted to an integer type
  like `int32_t`.

  * `int32_t check_address_range`
  * `int32_t has_access_to_region`
  * `int32_t tfm_core_check_sfn_parameters`
  * `int32_t tfm_start_partition`
  * `int32_t tfm_return_from_partition`
  * `int32_t tfm_check_sfn_req_integrity`
  * `int32_t tfm_core_check_sfn_req_rules`
  * `int32_t tfm_spm_sfn_request_handler`
  * `int32_t tfm_spm_sfn_request_thread_mode`
* `enum tfm_buffer_share_region_e`: the following function prototypes will be
  changed:

  * `tfm_spm_partition_set_share(uint32_t partition_idx, uint32_t share)` -> `tfm_spm_partition_set_share(uint32_t partition_idx, enum tfm_buffer_share_region_e share)`
* `enum tfm_memory_access_e`
* `enum attest_memory_access_t`
* `enum engine_cipher_mode_t`
* `mbedtls_cipher_type_t`

The following enumerated types are used for error code values of Secure service
calls. They should be kept as they are part of the interface and might be used
by external parties in Non-Secure code. For the Initial Attestation service,
the enumeration is defined in the PSA Attestation API specifications.

* `enum psa_attest_err_t`
* `enum psa_audit_err`
* `enum tfm_platform_err_t`

Implicit casting related with these enumerations is happening in two locations
of TF-M and need conversion functions in those locations, because the types can
not be changed:

* In the Non-Secure Client library, all of the Secure Service functions
  implicitly cast the `uint32_t` returned by `tfm_ns_lock_dispatch` to
  these enumerated types. Strategy 3 is needed here.
* In all of the veneer functions, there is an implicit cast from the `int32_t`
  value returned by the SVC request function (`tfm_core_*_request`) to these
  enumerated types. Strategy 3 is needed here as well. The implicit cast will
  eventually be removed if all of the services are using the Uniform Signatures
  Prototypes so that the veneer functions all return `psa_status_t` which is
  an `int32_t`.

If the interface of those services can be changed, these enumerations could be
removed and replaced with the `psa_status_t` type to remove the implicit
casting.

.. [1] C99 standard: http://www.open-std.org/jtc1/sc22/WG14/www/docs/n1256.pdf


--------------


*Copyright (c) 2019-2020, Arm Limited. All rights reserved.*
