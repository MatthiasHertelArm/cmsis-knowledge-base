---
id: "tfm-trusted-firmware-m-profile-medium-design-details"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Medium Design: Design details"
summary: "More details of TF-M Profile Medium design are described in following sections."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/configuration/profiles/tfm_profile_medium.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_medium.html#design-details"
license: "BSD-3-Clause"
mode: "V"
---

More details of TF-M Profile Medium design are described in following sections.


### Firmware framework


Profile Medium with IPC model and isolation level 2 aims to support usage
scenarios which require more complicated secure service model and additional
protection to PSA RoT.


#### Level 2 isolation


Profile Medium selects isolation level 2 by default. In addition to isolation
level 1, the PSA Root of Trust (PSA RoT) is also protected from access by the
Application Root of Trust (App RoT) in level 2 isolation.


#### IPC model


Profile Medium enables IPC model by default. IPC model can achieve a more
flexible framework and higher levels of isolation, but may require more memory
footprint and bring in longer latency, compared to SFN model.

TF-M IPC model implementation follows the PSA Firmware Framework for M
(PSA-FF-M) [PSA-FF-M]_.


### Crypto service


Compared to Profile Small, Profile Medium includes asymmetric cryptography to
support direct connection to Cloud services via common protocols, such as
TLS/DTLS 1.2.

As suggested in CoAP [RFC7252]_ and [RFC7925]_, TF-M Profile Medium by default
selects `TLS_ECDHE_ECDSA_WITH_AES_128_CCM` as reference, which requires:

    - ECDHE_ECDSA as key exchange algorithm.
    - AES-128-CCM (AES CCM mode with 128-bit key) as AEAD algorithm.
      Platforms can implement AES-128-CCM with truncated authentication tag to
      achieve less network bandwidth [RFC7925]_.
    - SHA256 as Hash function.
    - HMAC as Message Authentication Code algorithm.

Applications can also support TLS PSK [RFC4279]_ cipher suites, such as
`TLS_PSK_WITH_AES_128_CCM` [RFC7925]_.

.. note ::

    **Implementation note**

    Developers can replace default algorithms with others or implement more
    algorithms according to actual usage scenarios and device capabilities.

    If a Crypto hardware accelerator is integrated, the cipher suites and
    algorithms also depend on those accelerator features.

More details of cipher suite are described below.


#### Digital signature and verification


ECDSA is selected by default in Profile Medium.
ECDSA requires much shorter keys compared with RSA at the same security level.
Therefore, ECDSA can cost less storage area for assets and less network
bandwidth to setup a TLS connection.
ECDSA is also preferred for forward compatibility of future TLS versions.

As requested in [RFC7251]_, ECC curve `secp256r1` should be supported. More
ECC curves can be added based on the requirements in production.

If usage scenarios require RSA algorithm for backward compatibility and legacy
applications, platforms can add RSA support or replace ECDSA with RSA. The
cipher suite should be switched accordingly.


#### AEAD algorithm


If Protected Storage (PS) is implemented, it is recommended to select the same
AEAD algorithm for PS service as the one used by TLS/DTLS cipher suite.


### Internal Trusted Storage


The configuration of ITS is the same as those in Profile Small [PROFILE-S]_.


### Lightweight boot


BL2 implementation can be device specific. Devices may implement diverse
boot processes with different features and configurations.
However, the boot loader must support anti-rollback protection. Boot loader must
be able to prevent unauthorized rollback, to protect devices from being
downgraded to earlier versions with known vulnerabilities.

MCUBoot in TF-M is configured as multiple image boot by default in Profile
Medium. In multiple image boot, secure and non-secure images can be signed
independently with different keys and they can be updated separately. It can
support multiple vendors scenarios, in which non-secure and secure images are
generated and updated by different vendors.
Multiple image boot may require more storage area compared with single image
boot.


### Protected Storage


PS service is required if an off-chip storage device is integrated and used on
the platform.

TF-M PS service relies on an AEAD algorithm to ensure data confidentiality and
integrity. It is recommended to select the same AEAD algorithm as the one used
for TLS/DTLS cipher suite.

Anti-rollback protection in PS relies on non-volatile counter(s) provided by
TF-M Platform Secure Partition (SP).
