---
id: "tfm-tf-m-crypto-service-design-configuration-parameters"
type: "concept"
domain: "security"
title: "TF-M Crypto Service design: Configuration parameters"
summary: "The TF-M Crypto service exposes some configuration parameters to tailor the service configuration in terms of supported functionalities and hence FLASH/RAM size to meet the requirements of different platforms and use cases."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_crypto_design.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_crypto_design.html#configuration-parameters"
license: "BSD-3-Clause"
mode: "V"
---

The TF-M Crypto service exposes some configuration parameters to tailor
the service configuration in terms of supported functionalities and
hence FLASH/RAM size to meet the requirements of different platforms and
use cases. These parameters can be provided via CMake parameters during
the CMake configuration step and as a configuration header to allow the
configuration of the TF-PSA-Crypto library. When using Kconfig they are also
exported in the Kconfig menus.


+------------------------------------+---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
| **Parameter**                      | **Type**                  | **Description**                                                | **Default**                                                              |
+====================================+===========================+================================================================+==========================================================================+
| `CRYPTO_ENGINE_BUF_SIZE`           | CMake build               | Buffer used by TF-PSA-Crypto for its own allocations at        | 8096 (bytes)                                                             |
|                                    | configuration parameter   | runtime. This is a buffer allocated in static memory.          |                                                                          |
+------------------------------------+---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
| `CRYPTO_CONC_OPER_NUM`             | CMake build               | This parameter defines the maximum number of possible          | 8                                                                        |
|                                    | configuration parameter   | concurrent operation contexts (cipher, MAC, hash and key deriv)|                                                                          |
|                                    |                           | for multi-part operations, that can be allocated simultaneously|                                                                          |
|                                    |                           | at any time.                                                   |                                                                          |
+------------------------------------+---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
| `CRYPTO_IOVEC_BUFFER_SIZE`         | CMake build               | This parameter applies only to IPC model builds. In IPC model, | 5120 (bytes)                                                             |
|                                    | configuration parameter   | during a Service call, input and outputs are allocated         |                                                                          |
|                                    |                           | temporarily in an internal scratch buffer whose size is        |                                                                          |
|                                    |                           | determined by this parameter.                                  |                                                                          |
+------------------------------------+---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
| `CRYPTO_STACK_SIZE`                | CMake build               | Defines the stack size assigned to the crypto partition in     | 6912 (bytes)                                                             |
|                                    | configuration parameter   | higher level of isolation configurations (L1 isolation has a   |                                                                          |
|                                    |                           | common stack shared by all partitions)                         |                                                                          |
+------------------------------------+---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
| `CRYPTO_NV_SEED`                   | CMake build               | Uses the TF-PSA-Crypto NV seed feature to provide entropy in   | Defined for platforms which don't have `CRYPTO_HW_ACCELERATOR`         |
|                                    | configuration parameter   | case there is no HW acceleration providing HW entropy          |                                                                          |
+------------------------------------+---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
| `CRYPTO_IOVEC_BUFFER_SIZE`         | CMake build               | Defines the size of scratch buffers to handle input/outputs if | 5120 (bytes)                                                             |
|                                    | configuration parameter   | the Memory Mapped IOVEC feature is not enabled                 |                                                                          |
+------------------------------------+---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
| `CRYPTO_SINGLE_PART_FUNCS_DISABLED`| CMake build               | When enabled, only the multipart, i.e. non-integrated APIs will| Not defined (Profile default)                                            |
|                                    | configuration parameter   | be available in the service                                    |                                                                          |
+------------------------------------+---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
| `CRYPTO_*_MODULE_ENABLED`          | CMake build               | When enabled, the corresponding shim layer module and relative | Defined (Profile default)                                                |
|                                    | configuration parameters  | APIs are available in the service                              |                                                                          |
+------------------------------------+---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
| `TF_PSA_CRYPTO_CONFIG_FILE`        | Configuration header      | The TF-PSA-Crypto library can be configured to support         | `lib/ext/tf-psa-crypto/tfpsacrypto_config/crypto_config_default.h`     |
|                                    |                           | different algorithms through the usage of a configuration      | (Profile default)                                                        |
|                                    |                           | header file at build time. This specifies which cryptographic  |                                                                          |
|                                    |                           | mechanisms are available through the PSA API and also allows   |                                                                          |
|                                    |                           | for tailoring FLASH/RAMrequirements for different platforms    |                                                                          |
|                                    |                           | and use cases.                                                 |                                                                          |
+------------------------------------+---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
