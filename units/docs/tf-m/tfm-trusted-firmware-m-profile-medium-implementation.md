---
id: "tfm-trusted-firmware-m-profile-medium-implementation"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Medium-ARoT-less: Implementation"
summary: "The basic idea is to add dedicated profile CMake configuration files config/profile/profile_medium_arotless for this profile default configuration."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/configuration/profiles/tfm_profile_medium_arot-less.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_medium_arot-less.html#implementation"
license: "BSD-3-Clause"
mode: "V"
---

The basic idea is to add dedicated profile CMake configuration files
`config/profile/profile_medium_arotless` for this profile default configuration.

This top-level config file collects all the fundamental configuration flags and set them to default
values, to explicitly configured the features required in this profile, during TF-M build.

A platform/use case overwrite the default settings to configure this profile.

The behavior of the build flow (particularly the order of configuration loading and overriding) can
be found at tfm_cmake_configuration.

The default configurations in `config/profile/profile_medium_arotless` are shown below.


+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| Configs                                    | Default value                                                                                       | Descriptions                        |
+============================================+=====================================================================================================+=====================================+
| `TFM_ISOLATION_LEVEL`                    | `1`                                                                                               | Select level 1 isolation            |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `CONFIG_TFM_SPM_BACKEND`                 | `SFN`                                                                                             | Select SFN model                    |
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
| `TFM_PARTITION_FIRMWARE_UPDATE`          | `ON`                                                                                              | Enable Firmware Update service      |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_PROTECTED_STORAGE`        | `OFF`                                                                                             | Disable PS service                  |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_PLATFORM`                 | `ON`                                                                                              | Enable TF-M Platform SP             |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------+-------------------------------------+
| `TFM_PARTITION_POWER_MGMT`               | `OFF`                                                                                             | Enable TF-M Power Management SP     |
+--------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** Where a configuration is the same as the default in `config/config_default.cmake`, it might be omitted from the profile configuration file.


**Note:** **Implementation note** If the platform doesn't support secure update functionalities, FWU service will be disabled automatically. A warning will be thrown out during build.


### Regression test configuration


FWU regression tests and SFN regression tests are selected by default when regression tests are
enabled.
Other implementations are the same as those in Profile Medium.
