---
id: "tfm-trusted-firmware-m-profile-large-d-implementation"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Large Design: Implementation"
summary: "The basic idea is to add dedicated profile CMake configuration files under folder config/profile for TF-M Profile Large default configuration, the same as other TF-M Profiles do."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/configuration/profiles/tfm_profile_large.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_large.html#implementation"
license: "BSD-3-Clause"
mode: "V"
---

### Overview


The basic idea is to add dedicated profile CMake configuration files under
folder `config/profile` for TF-M Profile Large default configuration, the
same as other TF-M Profiles do.

The top-level Profile Large config file collects all the necessary configuration
flags and set them to default values, to explicitly enable the features required
in Profile Large and disable the unnecessary ones, during TF-M build.

A platform/use case can provide a configuration extension file to overwrite
Profile Large default setting and append other configurations.
This configuration extension file can be added via parameter
`TFM_EXTRA_CONFIG_PATH` in build command line.

The behaviour of the Profile Large build flow (particularly the order of
configuration loading and overriding) can be found at
tfm_cmake_configuration

The details of configurations will be covered in each module in
Implementation details.


### Implementation details


This section discusses the details of Profile Large implementation.


#### Top-level configuration files


The firmware framework configurations in `config/profile/profile_large` are
shown below.


+--------------------------------------------+------------------------------------+----------------------------------------------------------------------------------------------------+
| Configs                                    | Descriptions                       | Default value                                                                                      |
+============================================+====================================+====================================================================================================+
| `TFM_ISOLATION_LEVEL`                    | Select level 3 isolation           | `3`                                                                                              |
+--------------------------------------------+------------------------------------+----------------------------------------------------------------------------------------------------+
| `TFM_PARTITION_INTERNAL_TRUSTED_STORAGE` | Enable ITS SP                      | `ON`                                                                                             |
+--------------------------------------------+------------------------------------+----------------------------------------------------------------------------------------------------+
| `TFM_PARTITION_CRYPTO`                   | Enable Crypto service              | `ON`                                                                                             |
+--------------------------------------------+------------------------------------+----------------------------------------------------------------------------------------------------+
| `TFM_TF_PSA_CRYPTO_CONFIG_PATH`          | TF-PSA-Crypto config file path     | `${CMAKE_SOURCE_DIR}/lib/ext/tf-psa-crypto/tfpsacrypto_config/crypto_config_profile_large.h`     |
+--------------------------------------------+------------------------------------+----------------------------------------------------------------------------------------------------+
| `TFM_PARTITION_INITIAL_ATTESTATION`      | Enable Initial Attestation service | `ON`                                                                                             |
+--------------------------------------------+------------------------------------+----------------------------------------------------------------------------------------------------+
| `TFM_PARTITION_PROTECTED_STORAGE` [a]_   | Enable PS service                  | `ON`                                                                                             |
+--------------------------------------------+------------------------------------+----------------------------------------------------------------------------------------------------+
| `TFM_PARTITION_PLATFORM`                 | Enable TF-M Platform SP            | `ON`                                                                                             |
+--------------------------------------------+------------------------------------+----------------------------------------------------------------------------------------------------+
| `TFM_PARTITION_POWER_MGMT`               | Enable TF-M Power Management SP    | `OFF`                                                                                            |
+--------------------------------------------+------------------------------------+----------------------------------------------------------------------------------------------------+
.. [a] PS service is enabled by default. Platforms without off-chip storage
       devices can turn off `TFM_PARTITION_PROTECTED_STORAGE` to disable PS
       service. See Protected Storage Secure Partition for details.


#### Crypto service configurations



##### Crypto Secure Partition


TF-M Profile Large enables Crypto SP in top-level CMake config file and selects
all the Crypto modules.


##### TF-PSA-Crypto configurations


TF-M Profile Large adds a dedicated TF-PSA-Crypto config file `crypto_config_profile_large.h`
under `/lib/ext/tf-psa-crypto/tfpsacrypto_config` folder, instead of the common one
`crypto_config_default.h` [7]_.

Major cryptographic configurations are set as listed below:

    - Enable SHA256, SHA384 and SHA512
    - Enable generic message digest wrappers
    - Enable AES
    - Enable CCM mode, GCM mode, CTR mode, CFB mode and CBC mode for symmetric ciphers
    - Disable other modes for symmetric ciphers
    - Enable ECDH
    - Enable ECDSA
    - Enable RSA
    - Select ECC curve `secp256r1` and `secp384r1`
    - Enable HMAC-based key derivation function
    - Other configurations required by selected option above

A device/use case can append an extra config header to the Profile Large default
TF-PSA-Crypto config file to override the default settings. This can be done by
setting the `TFM_TF_PSA_CRYPTO_PLATFORM_EXTRA_CONFIG_PATH` cmake variable in
the platform config file `platform/ext<TFM_PLATFORM>/config.cmake`.
This cmake variable is a wrapper around the `TF_PSA_CRYPTO_USER_CONFIG_FILE`
options, but is preferred as it keeps all configuration in cmake.


#### Internal Trusted Storage configurations


ITS service is enabled in top-level Profile Large CMake config file by default.

The internal transient buffer size `ITS_BUF_SIZE` [8]_ is set to 64 bytes by
default. A platform/use case can overwrite the buffer size in its specific
configuration extension according to its actual requirement of assets and Flash
attributes.

Profile Large CMake config file won't touch the configurations of device
specific Flash hardware attributes.


#### Protected Storage Secure Partition


Data confidentiality, integrity and anti-rollback protection are enabled by
default in PS.

If PS is selected, AES-CCM is used as AEAD algorithm by default. If platform
hardware crypto accelerator supports the AEAD algorithm, the AEAD operations can
be executed in hardware crypto accelerator.

If platforms don't integrate any off-chip storage device, platforms can disable
PS in platform specific configuration extension file via
`platform/ext<TFM_PLATFORM>/config.cmake`.


#### BL2 setting


Profile Large enables MCUBoot provided by TF-M by default. A platform can
overwrite this configuration by disabling MCUBoot in its configuration extension
file `platform/ext<TFM_PLATFORM>/config.cmake`.

If MCUBoot provided by TF-M is enabled, multiple image boot is selected by
default.

If a device implements its own boot loader, the configurations are
implementation defined.


#### Software countermeasure against physical attacks


Profile Large selects TF-M FIH library Profile Medium by specifying
`-DTFM_FIH_PROFILE=MEDIUM` in top-level CMake config file.

System integrators shall implement software countermeasures in platform specific
implementations.


#### Device configuration extension


To change default configurations and add platform specific configurations,
a platform can add a platform configuration file at
`platform/ext<TFM_PLATFORM>/config.cmake`


#### Test configuration


Some cryptography tests are disabled due to the reduced cryptographic configuration profile.
Profile Large specific test configurations are also specified in Profile Large
top-level CMake config file `config/profile/profile_large_test.cmake`.


+--------------------------------------------+---------------+-----------------------------------------+
| Configs                                    | Default value | Descriptions                            |
+============================================+===============+=========================================+
| `TFM_CRYPTO_TEST_ALG_CBC`                | `ON`        | Test CBC cryptography mode              |
+--------------------------------------------+---------------+-----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_CCM`                | `ON`        | Test CCM cryptography mode              |
+--------------------------------------------+---------------+-----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_CFB`                | `OFF`       | Test CFB cryptography mode              |
+--------------------------------------------+---------------+-----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_ECB`                | `OFF`       | Test ECB cryptography mode              |
+--------------------------------------------+---------------+-----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_CTR`                | `OFF`       | Test CTR cryptography mode              |
+--------------------------------------------+---------------+-----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_OFB`                | `OFF`       | Test OFB cryptography mode              |
+--------------------------------------------+---------------+-----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_GCM`                | `ON`        | Test GCM cryptography mode              |
+--------------------------------------------+---------------+-----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_SHA_384`            | `OFF`       | Test SHA-384 cryptography algorithm     |
+--------------------------------------------+---------------+-----------------------------------------+
| `TFM_CRYPTO_TEST_ALG_SHA_512`            | `ON`        | Test SHA-512 cryptography algorithm     |
+--------------------------------------------+---------------+-----------------------------------------+
| `TFM_CRYPTO_TEST_HKDF`                   | `ON`        | Test HMAC-based key derivation function |
+--------------------------------------------+---------------+-----------------------------------------+
| `TFM_CRYPTO_TEST_ECDH`                   | `ON`        | Test ECDH key agreement algorithm       |
+--------------------------------------------+---------------+-----------------------------------------+
| `TFM_CRYPTO_TEST_CHACHA20`               | `OFF`       | Test ChaCha20 stream cipher             |
+--------------------------------------------+---------------+-----------------------------------------+
| `TFM_CRYPTO_TEST_CHACHA20_POLY1305`      | `OFF`       | Test ChaCha20-Poly1305 AEAD algorithm   |
+--------------------------------------------+---------------+-----------------------------------------+
| `TFM_CRYPTO_TEST_SINGLE_PART_FUNCS`      | `OFF`       | Test single-part operations in hash,    |
|                                            |               | MAC, AEAD and symmetric ciphers         |
+--------------------------------------------+---------------+-----------------------------------------+
