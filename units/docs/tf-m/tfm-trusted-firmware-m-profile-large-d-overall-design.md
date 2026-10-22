---
id: "tfm-trusted-firmware-m-profile-large-d-overall-design"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Large Design: Overall design"
summary: "TF-M Profile Large defines the following feature set:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/configuration/profiles/tfm_profile_large.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_large.html#overall-design"
license: "BSD-3-Clause"
mode: "V"
---

TF-M Profile Large defines the following feature set:

    - Firmware Framework

        - Inter-Process Communication (IPC) model [4]_
        - Isolation level 3 [4]_

    - Internal Trusted Storage (ITS)

    - Crypto

        - Support both symmetric ciphers and asymmetric ciphers
        - Asymmetric key based cipher suites defined in TLS 1.2 [5]_ to support
          direct secure connection to major CSPs, including

            - Authenticated Encryption with Associated Data (AEAD) algorithm
            - Asymmetric key algorithm based signature and verification
            - Public-key cryptography based key exchange
            - Hash function
            - HMAC for default Pseudorandom Function (PRF)

        - Asymmetric digital signature and verification for Initial Attestation
          Token (IAT)
        - Asymmetric algorithms for firmware image signature verification
        - Key derivation

    - Initial Attestation

        - Asymmetric key algorithm based Initial Attestation

    - Secure boot
        - Anti-rollback protection
        - Multiple image boot

    - Protected Storage (PS) if off-chip storage device is integrated

        - Data confidentiality
        - Data integrity
        - Rollback protection

    - Software countermeasures against physical attacks
