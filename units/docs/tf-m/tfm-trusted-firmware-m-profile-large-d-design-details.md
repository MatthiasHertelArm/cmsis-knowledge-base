---
id: "tfm-trusted-firmware-m-profile-large-d-design-details"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Large Design: Design details"
summary: "More details of TF-M Profile Large design are described in following sections."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/configuration/profiles/tfm_profile_large.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_large.html#design-details"
license: "BSD-3-Clause"
mode: "V"
---

More details of TF-M Profile Large design are described in following sections.


### Firmware framework


Profile Large selects IPC model and isolation level 3 by default.

Isolation level 3 supports additional isolation between App RoT services,
compared to isolation level 2. It can protect `RoT` services from each
other when their vendors don't trust each other.


### Crypto service


Profile Large supports direct connection to Cloud services via common protocols,
such as TLS 1.2.

In some usage scenarios, PSA RoT can be managed by device manufacturer or other
vendors and is out of control of application developers.
Profile Large selects alternative crypto algorithms for each crypto function to
support multiple common cipher suites required by various major CSPs. Therefore,
application developers can support services for diverse CSPs on same devices
with Profile Large, without relying on PSA RoT upgrades of crypto.

Devices meeting Profile Large should be in a position to offer at least two
alternatives to every cryptographic primitive for symmetric, asymmetric and
hash, and be able to use them for encryption, AEAD, signature and verification.

It will cost more resource in Profile Large to support more crypto algorithms
and cipher suites, compared to Profile Medium [2]_.


### Boot loader


BL2 implementation can be device specific. Devices may implement diverse
boot processes with different features and configurations.
However, the boot loader must support anti-rollback protection. Boot loader must
be able to prevent unauthorized rollback, to protect devices from being
downgraded to earlier versions with known vulnerabilities.

MCUBoot in TF-M is configured as multiple image boot by default in Profile
Large. In multiple image boot, secure and non-secure images can be signed
independently with different keys and they can be updated separately. It can
support multiple vendors scenarios, in which non-secure and secure images are
generated and updated by different vendors.
Multiple image boot may cost larger memory footprint compared with single image
boot.

Boot loader can implement software countermeasures to mitigate physical attacks.


### Protected Storage


PS service is required if an off-chip storage device is integrated and used on
the platform.

Anti-rollback protection in PS relies on non-volatile counter(s) provided by
TF-M Platform `Secure Partition` (SP).


### Software countermeasures against physical attacks


TF-M Profile Large enables TF-M Fault Injection Hardening (FIH) library Profile
Medium by default. It enables the following countermeasure techniques:

    - Control flow monitor
    - Failure loop hardening
    - Complex constants
    - Redundant variables and condition checks

Refer to TF-M physical attack mitigation design document [6]_ for FIH library
details.

.. note ::

    **TF-M FIH library is still under development**.

    TF-M FIH library hardens TF-M critical execution steps to make physical
    attacks more difficult, together with device hardware countermeasures.
    It is not guaranteed that TF-M FIH library is able to mitigate all kinds of
    physical attacks.

.. note ::

    **Implementation note**

    TF-M FIH library doesn't cover platform specific critical configurations.
    Platforms shall implement software countermeasures against physical attacks
    to protect platform specific implementation.
