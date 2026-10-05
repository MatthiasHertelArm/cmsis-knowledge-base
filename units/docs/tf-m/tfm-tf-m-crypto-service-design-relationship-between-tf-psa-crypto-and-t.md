---
id: "tfm-tf-m-crypto-service-design-relationship-between-tf-psa-crypto-and-t"
type: "concept"
domain: "security"
title: "TF-M Crypto Service design: Relationship between TF-PSA-Crypto and the TF-M Crypto service"
summary: "Up until TF-Mv2.0, the TF-M Crypto service used to provide its own separate implementation of the PSA Certified Crypto APIs, i.e. it provided its own version of the implementation defined aspects of the specifications."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/tfm_crypto_design.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_crypto_design.html#relationship-between-tf-psa-crypto-and-the-tf-m-crypto-service"
license: "BSD-3-Clause"
mode: "V"
---

### TF-M Crypto as a particular configuration of TF-PSA-Crypto


Up until `TF-Mv2.0`, the TF-M Crypto service used to provide its own separate
implementation of the PSA Certified Crypto APIs, i.e. it provided its own
version of the implementation defined aspects of the specifications. Starting
from `TF-Mv2.1`, the TF-M Crypto service fully aligns to the implementation
defined by the Mbed TLS project (aligns to TF-PSA-Crypto starting from
`TF-Mv2.3`), i.e. its implementation defined aspects are the same as the ones
defined by TF-PSA-Crypto/Mbed TLS.

As a consequence, starting from `TF-Mv2.1` the PSA Crypto headers available
in TF-M are a copy of those distributed by the TF-PSA-Crypto/Mbed TLS project.
TF-M just uses them and won't accept any contribution to them, as those need to
be discussed in the scope of the TF-PSA-Crypto/Mbed TLS project.

TF-M then represents just a configuration of the TF-PSA-Crypto reference
implementation where the TF-M Crypto APIs are provided as a remote call across
a transport channel, which might be represented by a TrustZone boundary (in
Armv8.x-M systems), by a mailbox channel in heterogeneous systems, e.g. Cortex-A
+ Cortex-M systems, by an SPM mediated interface, e.g. partition to partition
calls or, in general, through a mechanism which provides process separation
between the client and the service sides of the API.
In this context, the client must always define the TF-PSA-Crypto config option
`MBEDTLS_PSA_CRYPTO_CLIENT`, while the service must always have
`MBEDTLS_PSA_CRYPTO_SPM`, mainly to avoid symbol clashing at link time between
the library interface and the `tfm_crypto_api.c` interface. When there is a
component on the service side which is able to identify the client through an
ID, it is recommended to also define `MBEDTLS_PSA_CRYPTO_KEY_ID_ENCODES_OWNER`
option in order to provide separation in the key space.


### Usage of TF-PSA-Crypto configuration header


Crypto uses a configuration header, specified through the setting of the
`TF_PSA_CRYPTO_CONFIG_FILE`, i.e. PSA Crypto configuration.  In order to be
able to perform header inclusion for `psa/crypto.h`, the configuration file
must be visible to the compilation unit through the include hierarchy. If the
macro is not defined, the fall back strategy is to include the default config
file available in the TF-PSA-Crypto repo, i.e. `include/psa/crypto_config.h`,
which contains a set of default values for the macros.

Usage of the default header config when using the TF-M Crypto service is highly
discouraged, mainly because both on the client side and on the service side a
set of options must always be defined (or undefined), as described in the
previous section. TF-M provides example _profiles_ which show the options and
how they should be used on both client and service side of the integration. The
symbol to enable the Crypto config `TF_PSA_CRYPTO_CONFIG_FILE` instead must
be available to the unit being compiled which is including `psa/crypto.h`,
i.e. passed by the build system config stage.


### Hardware acceleration


The TF-M Crypto partition must handle all HW related crypto tasks, if the
platform is capable of offering hardware acceleration or if a complete Secure
Element is present. The main difference between the two is that a hardware
accelerator does not store keys but just accelerates operations, while a Secure
Element is capable of storing keys and the PSA Crypto core running on the host
must interface with it to store, retrieve or use them for crypto tasks, etc.

There are currently two methods to interface an accelerator into the Crypto
service, and both rely on the Crypto partition fully owning the Crypto hardware,
i.e. the memory mapped IO space must be bound the Crypto partition only. Both
methods are implemented through the capability of the _backend_ library to
either:

1. Provide a link time mechanism to replace pure SW implementations for algorithms
   with HW assisted implementations. In this case, the TF-M platform provides some
   additional HW abstraction through the usage of `crypto_hw_accelerator_*()`
   APIs. This is dubbed the `_ALT` approach and will be soon to be deprecated
   potentially starting from the release of Mbed TLS 4.0
2. Provide a cleanly defined interface specification [4]_ to describe the APIs that
   a driver must expose to the PSA Crypto core in order for the core to be able to
   offload operations to hardware. This is the preferred method for interfacing with
   HW.

Both solutions are currently handled at build time (either compilation or linking)
by TF-PSA-Crypto. For details on how to integrate a driver please refer directly to the
documentation referenced above and to the TF-PSA-Crypto repo.


### Builtin keys


A particular driver using the interface described in [4]_ is the TF-M Builtin
Key Loader driver [5]_. The goal of the driver is to make TF-PSA-Crypto aware of
*transparent builtin keys*, i.e. keys which can be read from the core (i.e. not
fully opaque keys), but that are normally bound to the platform and provisioned
in it, for which it would be more appropriate to treat them as standard
*transparent keys*. The concept of *transparent builtin keys* is not defined
in the spec so it is specifically a non standard extension added by TF-M to the
TF-PSA-Crypto implementation, which might be changed between releases until a standard
solution is adopted. TF-M patches TF-PSA-Crypto on the fly to enable such behaviour
using patches available in `lib/ext/tf-psa-crypto`. Implementations might disable
the `tfm_builtin_key_loader` and then must provide their own alternative storage
location for all of the TF-M required builtin keys, e.g. by having them stored in
a Secure Element with a corresponding opaque driver.
