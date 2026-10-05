---
id: "tfm-protected-storage-service-key-mana-background"
type: "concept"
domain: "security"
title: "Protected Storage service key management: Background"
summary: "The PSA Protected Storage API requires confidentiality for external storage to be provided by:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/ps_key_management.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/ps_key_management.html#background"
license: "BSD-3-Clause"
mode: "V"
---

The PSA Protected Storage API requires confidentiality for external storage to
be provided by:

    **cryptographic ciphers using device-bound keys**, a tamper resistant
    enclosure, or an inaccessible deployment location, depending on the threat
    model of the deployed system.

A TBSA-M-compliant device must embed a Hardware Unique Key (HUK), which provides
the root of trust (RoT) for confidentiality in the system. It must have at least
128 bits of entropy (and a 128 bit data size), and be accessible only to Trusted
code or Trusted hardware that acts on behalf of Trusted code. [TBSA-M]_
