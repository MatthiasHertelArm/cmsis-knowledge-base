---
id: "tfm-trusted-firmware-m-profile-small-d-design-details"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Small Design: Design details"
summary: "More details of TF-M Profile Small design are discussed in following sections."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/configuration/profiles/tfm_profile_small.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_small.html#design-details"
license: "BSD-3-Clause"
mode: "V"
---

More details of TF-M Profile Small design are discussed in following sections.


### Lightweight framework



#### TF-M framework model


SFN model is selected by default in Profile Small implementation.
SFN model is defined in FF-M 1.1 extensions [2]_. It is a more simple
implementation of TF-M framework and may also reduce memory footprint, compared
with Inter-Process Communication (IPC) model [3]_.


#### Level 1 isolation


PSA Security Model [4]_ defines 3 levels of isolation.

  - Level 1 isolation isolates Secure Processing Environment (SPE) from
    Non-secure Processing Environment (NSPE).
  - PSA Root of Trust (PSA RoT) and Application Root of Trust (ARoT) are
    isolated from each other in level 2 isolation.
  - Individual secure partitions are isolated from each other even within a
    particular security domain (PSA RoT, ARoT), in level 3 isolation.

Profile Small dedicated use cases with simple service model may not require
level 2 or level 3 isolation. Devices which Profile Small aims at may be unable
to implement stricter isolation, limited by hardware capabilities.

Level 1 isolation reduces requirements enforced by hardware isolation and cost
of software for management.

.. note ::

    **Security note**

    If a device or a use case enforces level 2 or level 3 isolation, it is
    suggested to apply other configurations, other than TF-M Profile Small.


### Crypto service


TF-M Profile Small only requires symmetric crypto since symmetric algorithms
require shorter keys and less computational burden, compared with asymmetric
crypto.

By default, TF-M Profile Small requires the same capabilities as defined in
TLS-PSK, to support symmetric key algorithms based protocols.

.. note ::

    **Implementation note**

    Please note that TF-M Profile Small doesn't require that TLS-PSK is
    mandatory in applications. Instead, Profile Small only requires the same
    capabilities as defined in TLS-PSK, such as one symmetric cipher algorithm
    and one hash function.

TF-M Profile Small selects TLS-PSK cipher suite TLS_PSK_WITH_AES_128_CCM [5]_
as reference, which requires:

    - AES-128-CCM (AES CCM mode with 128-bit key) as symmetric crypto algorithm
    - SHA256 as Hash function
    - HMAC as Message Authentication Code algorithm

TLS_PSK_WITH_AES_128_CCM is selected since it requires small key length and less
hardware capabilities, while keeping enough level of security.

.. note ::

    **Implementation note**

    Developers can replace default algorithms with others or implement more
    algorithms.

    Proper symmetric key algorithms and cipher suites should be selected
    according to device capabilities, the use case and the requirement of peers
    in connection.

    Refer to Crypto service configuration for implementation details of
    configuring algorithms and cipher suites.

.. note ::

    **Security note**

    It is recommended not to use MD5 or SHA-1 for message digests as they are
    subject to collision attacks [6]_ [7]_.

By default, Profile Small only enables multi-part functions defined in PSA
Cryptography API [13]_ in hash, symmetric ciphers, MAC and AEAD operations.
Disabling single-part functions optimizes the code size of TF-M crypto service.
Multi-part operations allows the message data to be processed in fragments
instead of all at once. In static memory allocation, single-part operation may
require to allocate a large memory space to support long message with unknown
length. Therefore single-part operations can help users optimize memory
footprint, especially while dealing with streaming data on IoT devices.

It may slightly increase the code size in applications to replace single-part
implementation with mulit-part implementation. Althgouth the code size increment
can be qaulified, if users are concerned about the code size increment, they can
enable single-part operations by toggling Profile Small default configuration.

It may increase latency and overall time cost to implement cryptography
functionality with single-part operations, compared to with multi-part ones.
Users can enable single-part operations if the usage scenario requires
single-part operations to meet its performance metrics.


### Secure Storage


TF-M Profile Small assumes that extremely constrained devices only contain basic
on-chip storage, without external or removable storage.
As a result, TF-M Profile Small includes ITS service and disables Protected
Storage service.


#### Encryption and rollback protection


Neither encryption nor rollback protection is enabled in current ITS
implementation.

It is expected that ITS relies solely on the physical inaccessibility property
of on-chip storage, together with PSA isolation, without requiring additional
cryptographic protection.


#### Internal transient buffer


ITS implements a internal transient buffer [8]_ to hold the data read
from/written to storage, especially for flash, to solve the alignment and
security issues.

The internal transient buffer is aligned to the flash device’s program unit.
Copying data to it from the caller can align all write requests to the flash
device’s program unit.
The internal transient buffer can help protect Flash access from some attacks,
such as TOCTOU attack.

Although removing this internal buffer can save some memory consumption,
typically 512 bytes, it may bring alignment or security issues.
Therefore, to achieve a better trade-off between memory footprint and security,
TF-M Profile Small optimizes the internal buffer size to 32 bytes by default.

As discussed in Crypto service, TF-M Profile Small requires AES-128 and
SHA-256, which use 128-bit key and 256-bit key respectively.
Besides, either long public/private keys or PKI-based certificates should be
very rare as asymmetric crypto is not supported in Profile Small.
Therefore, a 32-byte internal buffer should cover the assets in TF-M Profile
Small use cases.

The buffer size can be adjusted according to use case and device Flash
attributes. Refer to Internal Trusted Storage configurations for more
details.


### Initial Attestation


Profile Small requires an Initial Attestation secure service based on symmetric
key algorithms. Refer to PSA Attestation API document [9]_ for details of
Initial Attestation based on symmetric key algorithms.

It can heavily increase memory footprint to support Initial Attestation based on
asymmetric key algorithms, due to asymmetric ciphers and related PKI modules.

.. note ::

    **Implementation note**

    As pointed out by PSA Attestation API document [9]_, the use cases of
    Initial Attestation based on symmetric key algorithms can be limited due to
    the associated infrastructure costs for key management and operational
    complexities. It may also restrict the ability to interoperate with
    scenarios that involve third parties.

    If asymmetric key algorithms based Initial Attestation is required in use
    scenarios, it is recommended to select other TF-M Profiles which support
    asymmetric key algorithms.

.. note ::

    **Implementation note**

    It is recommended to utilize the same MAC algorithm supported in Crypto
    service to complete the signing in `COSE_Mac0`, to minimize memory
    footprint.


### Lightweight boot


If MCUBoot provided by TF-M is enabled, single image boot [10]_ is selected by
default in Profile Small.
In case of single image boot, secure and non-secure images are handled as a
single blob and signed together during image generation.

However, secure and non-secure images must be updated together in single image
boot. It may decrease the flexibility of image update and cost longer update
process. Since the image sizes should usually be small with limited
functionalities in Profile Small dedicated use case, the cost may still be
reasonable.

BL2 implementation can be device specific. Devices may implement diverse
boot processes with different features and configurations.
However, anti-rollback protection is required as a mandatory feature of boot
loader. Boot loader should be able to prevent unauthorized rollback, to protect
devices from being downgraded to earlier versions with known vulnerabilities.
