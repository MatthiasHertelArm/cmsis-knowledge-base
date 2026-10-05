---
id: "tfm-crypto-service-integration-guide-considerations-on-service-configuration"
type: "concept"
domain: "security"
title: "Crypto Service Integration Guide: Considerations on service configuration"
summary: "The TF-M Crypto service relies on a cryptographic library to provide the functionalities specific by the PSA Crypto API spec and the PSA cryptoprocessor driver interface spec. At the moment, the only supported library is TF-PSA-Crypto [3]."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_crypto_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_crypto_integration_guide.html#considerations-on-service-configuration"
license: "BSD-3-Clause"
mode: "V"
---

### Crypto *backend* library configuration

The TF-M Crypto service relies on a cryptographic library to provide the
functionalities specific by the PSA Crypto API spec and the PSA cryptoprocessor
driver interface spec. At the moment, the only supported library is
TF-PSA-Crypto [3]_.

The configuration of the backend library is supplied using the
`TFM_TF_PSA_CRYPTO_CONFIG_PATH` config option that points to a configuration
header following the configuration scheme of TF-PSA-Crypto.

Platforms can specify an extra config file by setting the
`TFM_TF_PSA_CRYPTO_PLATFORM_EXTRA_CONFIG_PATH` variable (which is a wrapper
around the `TF_PSA_CRYPTO_USER_CONFIG_FILE` option). This is preferred for
platform configuration over `TFM_TF_PSA_CRYPTO_CONFIG_PATH` as it does not
interfere with config changes due to TFM Profile.


The default entropy source configured for TF-PSA-Crypto is
`MBEDTLS_ENTROPY_NV_SEED` with a unique seed. For production devices, an
alternative hardware entropy source can be specified using the config option
`MBEDTLS_PSA_DRIVER_GET_ENTROPY`
Starting from Mbed TLS 3.3.0, the Python package `jsonschema` must be
available when building as it is required by the autogen framework for the
driver integrations into the PSA Crypto core and driver wrapper modules

### Crypto service build time options


  - `CRYPTO_STACK_SIZE` : Defines the stack size of the Crypto Secure
    Partition. This value might depend on several parameters such as the build
    type, the compiler being used, the cryptographic functionalities that are
    enabled at build time
  - `CRYPTO_<COMPONENT>_MODULE_ENABLED` : A series of defines, one per each
    `<COMPONENT>` that processes cryptographic operations, that are used to
    disable modules at build time. Each define corresponds to a component as
    described in the components list.



### Crypto service *builtin* keys integration

A detailed description of how the service interacts with *builtin* keys is
available in the `tfm_builtin_key_loader`
design document.


The crypto service integration with builtin keys relies on implementation
details of TF-PSA-Crypto that are not standardized in the spec and might
change between releases due to ongoing work [4]_

#### References


.. [1] PSA Crypto APIs: \ https://arm-software.github.io/psa-api/crypto/1.1/
.. [2] PSA cryptoprocessor driver interface: \ https://github.com/Mbed-TLS/TF-PSA-Crypto/blob/development/docs/proposed/psa-driver-interface.md
.. [3] TF-PSA-Crypto library: \ https://github.com/Mbed-TLS/TF-PSA-Crypto/
.. [4] Interface for platform keys:  `https://github.com/ARM-software/psa-crypto-api/issues/550` (private)


--------------

*SPDX-License-Identifier: BSD-3-Clause*

*SPDX-FileCopyrightText: Copyright The TrustedFirmware-M Contributors*
