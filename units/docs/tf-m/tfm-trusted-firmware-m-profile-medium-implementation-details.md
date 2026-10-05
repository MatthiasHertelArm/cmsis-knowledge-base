---
id: "tfm-trusted-firmware-m-profile-medium-implementation-details"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Medium Design: Implementation / Implementation details"
summary: "This section discusses the details of Profile Medium implementation."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/configuration/profiles/tfm_profile_medium.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_medium.html#implementation-details"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Implementation_

This section discusses the details of Profile Medium implementation.


#### Top-level configuration files


The firmware framework configurations in `config/profile/profile_medium` are
shown below.


+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| Configs                                    | Default value                                                                                       | Descriptions                        |
+============================================+=====================================================================================================+=====================================+
| `TFM_ISOLATION_LEVEL`                    | `2`                                                                                               | Select level 2 isolation            |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_INTERNAL_TRUSTED_STORAGE` | `ON`                                                                                              | Enable ITS SP                       |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `ITS_BUF_SIZE`                           | `32`                                                                                              | ITS internal transient buffer size  |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_CRYPTO`                   | `ON`                                                                                              | Enable Crypto service               |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `CRYPTO_ASYM_ENCRYPT_MODULE_ENABLED`     | `OFF`                                                                                             | Enable Crypto asymmetric            |
|                                            |                                                                                                     | encryption operations               |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_TF_PSA_CRYPTO_CONFIG_PATH`          | `${CMAKE_SOURCE_DIR}/lib/ext/tf-psa-crypto/tfpsacrypto_config/crypto_config_profile_medium.h`     | TF-PSA-Crypto config file path      |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_INITIAL_ATTESTATION`      | `ON`                                                                                              | Enable Initial Attestation service  |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_PROTECTED_STORAGE` [1]_   | `ON`                                                                                              | Enable PS service                   |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_PLATFORM`                 | `ON`                                                                                              | Enable TF-M Platform SP             |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_POWER_MGMT`               | `OFF`                                                                                             | Enable TF-M Power Management SP     |
+--------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
.. [1] PS service is enabled by default. Platforms without off-chip storage
       devices can turn off `TFM_PARTITION_PROTECTED_STORAGE` to disable PS
       service. See Protected Storage Secure Partition for details.


Where a configuration is the same as the default in
`config/config_base.cmake`, it is omitted from the profile configuration
file.

##### Test configuration


Standard regression test configuration applies. This means that enabling
regression testing via

`-DTEST_S=ON -DTEST_NS=ON`

Will enable testing for all enabled partitions. See above for details of enabled
partitions. Because Profile Medium enables IPC model, the IPC tests are also
enabled.

Some cryptography tests are disabled due to the reduced cryptographic configuration profile.


+--------------------------------------------+---------------+-----------------------------------------------+
| Configs                                    | Default value | Descriptions                                  |
+============================================+===============+===============================================+
| `TFM_CRYPTO_TEST_ALG_CBC`                | `OFF`       | Disable CBC mode test                         |
+--------------------------------------------+---------------+-----------------------------------------------+
| `TFM_CRYPTO_TEST_ALG_CCM`                | `ON`        | Enable CCM mode test                          |
+--------------------------------------------+---------------+-----------------------------------------------+
| `TFM_CRYPTO_TEST_ALG_CFB`                | `OFF`       | Disable CFB mode test                         |
+--------------------------------------------+---------------+-----------------------------------------------+
| `TFM_CRYPTO_TEST_ALG_ECB`                | `OFF`       | Disable ECB mode test                         |
+--------------------------------------------+---------------+-----------------------------------------------+
| `TFM_CRYPTO_TEST_ALG_CTR`                | `OFF`       | Disable CTR mode test                         |
+--------------------------------------------+---------------+-----------------------------------------------+
| `TFM_CRYPTO_TEST_ALG_OFB`                | `OFF`       | Disable OFB mode test                         |
+--------------------------------------------+---------------+-----------------------------------------------+
| `TFM_CRYPTO_TEST_ALG_GCM`                | `OFF`       | Disable GCM mode test                         |
+--------------------------------------------+---------------+-----------------------------------------------+
| `TFM_CRYPTO_TEST_ALG_SHA_384`            | `OFF`       | Disable SHA-384 algorithm test                |
+--------------------------------------------+---------------+-----------------------------------------------+
| `TFM_CRYPTO_TEST_ALG_SHA_512`            | `OFF`       | Disable SHA-512 algorithm test                |
+--------------------------------------------+---------------+-----------------------------------------------+
| `TFM_CRYPTO_TEST_HKDF`                   | `OFF`       | Disable HKDF algorithm test                   |
+--------------------------------------------+---------------+-----------------------------------------------+
| `TFM_CRYPTO_TEST_ECDH`                   | `ON`        | Enable ECDH key agreement test                |
+--------------------------------------------+---------------+-----------------------------------------------+
| `TFM_CRYPTO_TEST_CHACHA20`               | `OFF`       | Disable ChaCha20 stream cipher test           |
+--------------------------------------------+---------------+-----------------------------------------------+
| `TFM_CRYPTO_TEST_CHACHA20_POLY1305`      | `OFF`       | Disable ChaCha20-Poly1305 AEAD algorithm test |
+--------------------------------------------+---------------+-----------------------------------------------+
| `TFM_CRYPTO_TEST_SINGLE_PART_FUNCS`      | `OFF`       | Test single-part operations in hash, MAC,     |
|                                            |               | AEAD and symmetric ciphers                    |
+--------------------------------------------+---------------+-----------------------------------------------+

##### Device configuration extension


To change default configurations and add platform specific configurations,
a platform can add a platform configuration file at
`platform/ext<TFM_PLATFORM>/config.cmake`


#### Crypto service configurations



##### Crypto Secure Partition


TF-M Profile Medium enables Crypto SP in top-level CMake config file.
The following PSA Crypto operationts are enabled by default.

   - Hash operations
   - Message authentication codes
   - Symmetric ciphers
   - AEAD operations
   - Asymmetric key algorithm based signature and verification
   - Key derivation
   - Key management


##### TF-PSA-Crypto configurations


TF-M Profile Medium adds a dedicated TF-PSA-Crypto config file `crypto_config_profile_medium.h`
under `/lib/ext/tf-psa-crypto/tfpsacrypto_config` folder, instead of the common one
`crypto_config_default.h` [CRYPTO-DESIGN]_.

Major cryptographic configurations are set as listed below:

    - Enable SHA256
    - Enable generic message digest wrappers
    - Enable AES
    - Enable CCM mode for symmetric ciphers
    - Disable other modes for symmetric ciphers
    - Enable ECDH
    - Enable ECDSA
    - Select ECC curve `secp256r1`
    - Other configurations required by selected option above

Other configurations can be selected to optimize the memory footprint of Crypto
module.

A device/use case can append an extra config header to the  Profile Medium
default TF-PSA-Crypto config file. This can be done by setting the
`TFM_TF_PSA_CRYPTO_PLATFORM_EXTRA_CONFIG_PATH` cmake variable in the platform
config file `platform/ext<TFM_PLATFORM>/config.cmake`. This cmake variable is
a wrapper around the `TF_PSA_CRYPTO_USER_CONFIG_FILE` options, but is
preferred as it keeps all configuration in cmake.


#### Internal Trusted Storage configurations


ITS service is enabled in top-level Profile Medium CMake config file by default.

The internal transient buffer size `ITS_BUF_SIZE` [ITS-INTEGRATE]_ is set to
32 bytes by default. A platform/use case can overwrite the buffer size in its
specific configuration extension according to its actual requirement of assets
and Flash attributes.

Profile Medium CMake config file won't touch the configurations of device
specific Flash hardware attributes [ITS-INTEGRATE]_.


#### Protected Storage Secure Partition


Data confidentiality, integrity and anti-rollback protection are enabled by
default in PS.

If PS is selected, AES-CCM is used as AEAD algorithm by default. It requires to
enable PS implementation to select diverse AEAD algorithm.

If platforms don't integrate any off-chip storage device, platforms can disable
PS in platform specific configuration extension file via
`platform/ext<TFM_PLATFORM>/config.cmake`.


#### BL2 setting


Profile Medium enables MCUBoot provided by TF-M by default. A platform can
overwrite this configuration by disabling MCUBoot in its configuration extension
file `platform/ext<TFM_PLATFORM>/config.cmake`.

If MCUBoot provided by TF-M is enabled, multiple image boot is selected by
default in TF-M Profile Medium top-level CMake config file.

If a device implements its own boot loader, the configurations are
implementation defined.
