---
id: "tfm-trusted-firmware-m-profile-small-d-overall-design"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Small Design: Overall design"
summary: "TF-M Profile Small defines the following features:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/configuration/profiles/tfm_profile_small.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_small.html#overall-design"
license: "BSD-3-Clause"
mode: "V"
---

TF-M Profile Small defines the following features:

    - Lightweight framework

        - Secure Function (SFN) model [2]_
        - Level 1 isolation
        - Buffer sharing allowed
        - Single secure context

    - Crypto

        - Symmetric cipher only
        - Cipher suite for symmetric-key algorithms based protocols, such as
          cipher suites defined in TLS pre-shared key (TLS-PSK) [1]_.

            - Advanced Encryption Standard (AES) as symmetric crypto algorithm
            - SHA256 as Hash function
            - HMAC as Message Authentication Code algorithm
        - Only enable multi-part functions in hash, symmetric ciphers,
          Message Authentication Code (MAC) and Authenticated Encryption with
          Associated Data (AEAD) operations.

    - Internal Trusted Storage (ITS)

        - No encryption
        - No rollback protection
        - Decrease internal transient buffer size

    - Initial Attestation

        - Based on symmetric key algorithms

    - Lightweight boot

        - Single image boot
        - Anti-rollback protection is enabled


Protected Storage, firmware update and other Secure Services provided by TF-M are
disabled by default.
