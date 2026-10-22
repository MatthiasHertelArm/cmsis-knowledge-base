---
id: "tfm-bl1-immutable-bootloader-post-quantum-signature-verification-in-b"
type: "concept"
domain: "security"
title: "BL1 Immutable bootloader: Post-Quantum signature verification in BL1_2"
summary: "BL1_2 uses a post-quantum asymmetric signature scheme to verify the next stage. The scheme used is Leighton-Michaeli Signatures (henceforth LMS). LMS is standardised in NIST SP800-208 <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-208.pdf> and IETF RFC8554."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/bl1.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/bl1.html#post-quantum-signature-verification-in-bl1-2"
license: "BSD-3-Clause"
mode: "V"
---

BL1_2 uses a post-quantum asymmetric signature scheme to verify the next stage.
The scheme used is Leighton-Michaeli Signatures (henceforth LMS). LMS is
standardised in `NIST SP800-208
<https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-208.pdf>`_
and [IETF RFC8554.](https://datatracker.ietf.org/doc/html/rfc8554)

LMS is a stateful-hash signature scheme, meaning that:

 1) It is constructed from a cryptographic hash function, in this case SHA256.

    - This function can be accelerated by existing hardware accelerators, which
      can make LMS verification relatively fast compared to other post-quantum
      signature schemes that cannot be accelerated in hardware yet.

 2) Each private key can only be used to sign a certain number of images.

    - BL1_2 uses the SHA256_H10 parameter set, meaning each key can sign 1024
      images.

The main downside, the limited amount of possible signatures, can be mitigated
by limiting the amount of image upgrades that are done. As BL2 is often
currently not upgradable, it is not anticipated that this limit will be
problematic. If BL1 is being used to directly boot a TF-M/NS combined image, the
limit is more likely to be problematic, and care should be taken to examine the
likely update amount.

LMS public keys are 32 bytes in size, and LMS signatures are 1912 bytes in size.
The signature size is larger than some asymmetric schemes, though most devices
should have enough space in flash to accommodate this.

The main upside of LMS, aside from the security against attacks involving
quantum computers, is that it is relatively simple to implement. The software
implementation that is used by BL1 is ~3KiB in size, which is considerably
smaller than the corresponding RSA implementation which is at least 6.5K. This
simplicity of implementation is useful to avoid bugs.

BL1_2 uses the Mbed TLS implementation of LMS. More information about it is
available in the `Mbed TLS documentation
<https://mbed-tls.readthedocs.io/projects/api/en/development/api/file/lms_8h/>`_
