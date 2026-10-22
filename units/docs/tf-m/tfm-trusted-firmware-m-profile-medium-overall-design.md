---
id: "tfm-trusted-firmware-m-profile-medium-overall-design"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Medium Design: Overall design"
summary: "TF-M Profile Medium defines the following feature set:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/configuration/profiles/tfm_profile_medium.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_medium.html#overall-design"
license: "BSD-3-Clause"
mode: "V"
---

TF-M Profile Medium defines the following feature set:

    - Firmware Framework

        - Inter-Process Communication (IPC) model [PSA-FF-M]_
        - Isolation level 2 [PSA-FF-M]_

    - Internal Trusted Storage (ITS)

    - Crypto

        - Support both symmetric cryptography and asymmetric cryptography
        - Asymmetric key based cipher suite suggested in TLS/DTLS profiles for
          IoT [RFC7925]_ and CoAP [RFC7252]_, including

            - Authenticated Encryption with Associated Data (AEAD) algorithm
            - Asymmetric key algorithm based signature and verification
            - Public-key cryptography based key exchange
            - Hash function
            - HMAC for default Pseudorandom Function (PRF)

        - Asymmetric digital signature and verification for Initial Attestation
          Token (IAT)

    - Initial Attestation

        - Asymmetric key algorithm based Initial Attestation

    - Lightweight boot

        - Anti-rollback protection
        - Multiple image boot

    - Protected Storage (PS) if off-chip storage device is integrated

        - Data confidentiality
        - Data integrity
        - Rollback protection
