---
id: "tfm-trusted-firmware-m-profile-small-d-implementation-details"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Small Design: Implementation / Implementation details"
summary: "This section discusses the details of Profile Small implementation."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/configuration/profiles/tfm_profile_small.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_small.html#implementation-details"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Implementation_

This section discusses the details of Profile Small implementation.


#### Top-level configuration files


The firmware framework configurations in `config/profile/profile_small` are
shown below.


+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| Configs                                    | Default value                                                                                       | Descriptions                        |
+============================================+=====================================================================================================+=====================================+
| `TFM_ISOLATION_LEVEL`                    | `1`                                                                                               | Select level 2 isolation            |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_INTERNAL_TRUSTED_STORAGE` | `ON`                                                                                              | Enable ITS SP                       |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `ITS_BUF_SIZE`                           | `32`                                                                                              | ITS internal transient buffer size  |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_CRYPTO`                   | `ON`                                                                                              | Enable Crypto service               |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_TF_PSA_CRYPTO_CONFIG_PATH`          | `${CMAKE_SOURCE_DIR}/lib/ext/tf-psa-crypto/tfpsacrypto_config/crypto_config_profile_small.h`      | TF-PSA-Crypto config file path      |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `CRYPTO_ASYM_SIGN_MODULE_ENABLED`        | `OFF`                                                                                             | Enable asymmetric signature         |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `CRYPTO_ASYM_ENCRYPT_MODULE_ENABLED`     | `OFF`                                                                                             | Enable asymmetric encryption        |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_INITIAL_ATTESTATION`      | `ON`                                                                                              | Enable Initial Attestation service  |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `SYMMETRIC_INITIAL_ATTESTATION`          | `ON`                                                                                              | Enable symmetric attestation        |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_PROTECTED_STORAGE`        | `OFF`                                                                                             | Enable PS service                   |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_PLATFORM`                 | `OFF`                                                                                             | Enable TF-M Platform SP             |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_POWER_MGMT`               | `OFF`                                                                                             | Enable TF-M Power Management SP     |
+--------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
.. note ::

    **Implementation note**

    The following sections focus on the feature selection via configuration
    setting.
    Dedicated optimization on memory footprint is not covered in this document.


##### Device configuration extension


To change default configurations and add platform specific configurations,
a platform can add a platform configuration file at
`platform/ext<TFM_PLATFORM>/config.cmake`


#### TF-M framework setting


The top-level Profile Small CMake config file selects SFN model and level 1
isolation.

In SFN model, `-DPSA_FRAMEWORK_HAS_MM_IOVEC` is enabled by default.
It reduces memory footprint by avoiding the transient copy from input
vectors and copy to output vectors.


#### Crypto service configuration



##### Crypto Secure Partition


TF-M Profile Small enables Crypto Secure Partition (SP) in its top-level CMake
config file. Crypto SP modules not supported in TF-M Profile Small are disabled.
The disabled modules/features are shown below.

    - Disable asymmetric cipher
    - Disable single-part operations in Hash, MAC, AEAD and symmetric ciphers
      via selecting `CRYPTO_SINGLE_PART_FUNCS_DISABLED`

Other modules and configurations [11]_ are kept as default values.

Additional configuration flags with more fine granularity can be added to
control building of specific crypto algorithms and corresponding test cases.


##### TF-PSA-Crypto configurations


TF-M Profile Small adds a dedicated TF-PSA-Crypto config file `crypto_config_profile_small.h`
under `/lib/ext/tf-psa-crypto/tfpsacrypto_config` folder, instead of the common one
`crypto_config_default.h` [11]_.

Major cryptographic configurations are set as listed below:

    - Enable SHA256
    - Enable generic message digest wrappers
    - Enable AES
    - Enable CCM mode for symmetric ciphers
    - Disable other modes for symmetric ciphers
    - Disable asymmetric ciphers
    - Disable HMAC-based key derivation function (HKDF)

Other configurations can be selected to optimize the memory footprint of Crypto
module.

A device/use case can append an extra config header to the  Profile Small
default TF-PSA-Crypto config file. This can be done by setting the
`TFM_TF_PSA_CRYPTO_PLATFORM_EXTRA_CONFIG_PATH` cmake variable in the platform
config file `platform/ext<TFM_PLATFORM>/config.cmake`. This cmake variable is
a wrapper around the `TF_PSA_CRYPTO_USER_CONFIG_FILE` options, but is
preferred as it keeps all configuration in cmake.


#### Internal Trusted Storage configurations


ITS service is enabled in top-level Profile Small CMake config file.

The internal transient buffer size `ITS_BUF_SIZE` [8]_ is set to 32 bytes by
default. A platform/use case can overwrite the buffer size in its specific
configuration extension according to its actual requirement of assets and Flash
attributes.

Profile Small CMake config file won't touch the configurations of device
specific Flash hardware attributes [8]_.


#### Initial Attestation secure service


TF-M Profile Small provides a reference implementation of symmetric key
algorithms based Initial Attestation, using HMAC SHA-256 as MAC algorithm in
`COSE_Mac0` structure. The implementation follows PSA Attestation API document
[9]_.

Profile Small top-level config file enables Initial Attestation secure service
and selects symmetric key algorithms based Initial Attestation by default.

    - Set `TFM_PARTITION_INITIAL_ATTESTATION` to `ON`
    - Set `SYMMETRIC_INITIAL_ATTESTATION` to `ON`

Symmetric and asymmetric key algorithms based Initial Attestation can share the
same generations of token claims, except Instance ID claim.

Profile Small may implement the procedure or rely on a 3rd-party tool to
construct and sign `COSE_Mac0` structure.

Details of symmetric key algorithms based Initial Attestation design will be
covered in a dedicated document.


#### Disabled secure services


Protected Storage and Platform Service are disabled by default
in Profile Small top-level CMake config file.


#### Test configuration


Some cryptography tests are disabled due to the reduced cryptographic configuration profile.
Some of them are shown in the table below.


+--------------------------------------------+---------------+----------------------------------------+
| Configs                                    | Default value | Descriptions                           |
+============================================+===============+========================================+
| `TFM_CRYPTO_TEST_ALG_CBC`                | `OFF`       | Test CBC cryptography mode             |
+--------------------------------------------+---------------+----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_CCM`                | `ON`        | Test CCM cryptography mode             |
+--------------------------------------------+---------------+----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_CFB`                | `OFF`       | Test CFB cryptography mode             |
+--------------------------------------------+---------------+----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_ECB`                | `OFF`       | Test ECB cryptography mode             |
+--------------------------------------------+---------------+----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_CTR`                | `OFF`       | Test CTR cryptography mode             |
+--------------------------------------------+---------------+----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_OFB`                | `OFF`       | Test OFB cryptography mode             |
+--------------------------------------------+---------------+----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_GCM`                | `OFF`       | Test GCM cryptography mode             |
+--------------------------------------------+---------------+----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_SHA_384`            | `OFF`       | Test SHA-384 cryptography algorithm    |
+--------------------------------------------+---------------+----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_SHA_512`            | `OFF`       | Test SHA-512 cryptography algorithm    |
+--------------------------------------------+---------------+----------------------------------------+
| `TFM_CRYPTO_TEST_HKDF`                   | `OFF`       | Test HKDF key derivation algorithm     |
+--------------------------------------------+---------------+----------------------------------------+
| `TFM_CRYPTO_TEST_ECDH`                   | `OFF`       | Test ECDH key agreement algorithm      |
+--------------------------------------------+---------------+----------------------------------------+
| `TFM_CRYPTO_TEST_CHACHA20`               | `OFF`       | Test ChaCha20 stream cipher            |
+--------------------------------------------+---------------+----------------------------------------+
| `TFM_CRYPTO_TEST_CHACHA20_POLY1305`      | `OFF`       | Test ChaCha20-Poly1305 AEAD algorithm  |
+--------------------------------------------+---------------+----------------------------------------+
| `TFM_CRYPTO_TEST_SINGLE_PART_FUNCS`      | `OFF`       | Test single-part operations in hash,   |
|                                            |               | MAC, AEAD and symmetric ciphers        |
+--------------------------------------------+---------------+----------------------------------------+

#### BL2 setting


Profile Small enables MCUBoot provided by TF-M by default. A platform can
overwrite this configuration by disabling MCUBoot in its configuration extension
file `platform/ext<TFM_PLATFORM>/config.cmake`.

If MCUBoot provided by TF-M is enabled, single image boot is selected in TF-M
Profile Small top-level CMake config file.

If a device implements its own boot loader, the configurations are
implementation defined.


+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| Configs                                    | Default value                                                                                       | Descriptions                        |
+============================================+=====================================================================================================+=====================================+
| `BL2`                                    | `ON`                                                                                              | Enable MCUBoot bootloader           |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `MCUBOOT_IMAGE_NUMBER`                   | `1`                                                                                               | Combine S and NS images             |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
