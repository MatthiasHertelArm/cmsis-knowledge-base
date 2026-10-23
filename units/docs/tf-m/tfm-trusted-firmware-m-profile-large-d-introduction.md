---
id: "tfm-trusted-firmware-m-profile-large-d-introduction"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Large Design: Introduction"
summary: "As one of TF-M Profiles, Profile Large protects less resource-constrained Arm Cortex-M devices."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/configuration/profiles/tfm_profile_large.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_large.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

As one of TF-M Profiles, Profile Large protects less resource-constrained Arm
Cortex-M devices.

Compared to Profile Small [1]_ and Profile Medium [2]_, Profile Large aims to
enable more secure features to support higher level of security required in more
complex usage scenarios.

    - Isolation level 3 enables additional isolation between
      `Application RoT` (App RoT) services.
    - More crypto algorithms and cipher suites are selected to securely connect
      devices to remote services offered by various major Cloud Service
      Providers (CSP)
    - Basic software countermeasures against physical attacks can be enabled.

Profile Large can be aligned as a reference implementation with the requirements
defined in PSA Certified Level 3 Lightweight Protection Profile [3]_.
