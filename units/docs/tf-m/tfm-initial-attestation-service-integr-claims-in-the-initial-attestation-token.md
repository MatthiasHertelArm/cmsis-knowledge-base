---
id: "tfm-initial-attestation-service-integr-claims-in-the-initial-attestation-token"
type: "concept"
domain: "security"
title: "Initial Attestation Service Integration Guide: Claims in the initial attestation token"
summary: "The initial attestation token is formed of claims. A claim is a data item, which is represented in a key - value structure. The following fixed set of claims are included in the token:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_attestation_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_attestation_integration_guide.html#claims-in-the-initial-attestation-token"
license: "BSD-3-Clause"
mode: "V"
---

The initial attestation token is formed of claims. A claim is a data item,
which is represented in a key - value structure. The following fixed set of
claims are included in the token:

    - **Auth challenge**: Input object from caller. Can be a single nonce from
      server or hash of nonce and attested data. It is intended to provide
      freshness to report and the caller has responsibility to arrange
      this. Allowed length: 32, 48, 64 bytes. The claim is modeled to be
      eventually represented by the EAT standard claim nonce. Until such a
      time as that standard exists, the claim will be represented by a custom
      claim. Value is encoded as byte string.

    - **Instance ID**: It represents the unique identifier of the instance.
      In the PSA definition it is:

        - a hash of the public attestation key of the instance in asymmetric
          attestation.
        - hashes of the symmetric attestation key of the instance in symmetric
          attestation.

      The claim is modeled to be eventually represented by the EAT standard
      claim UEID of type GUID. Until such a time as that standard exists, the
      claim will be represented by a custom claim Value is encoded as byte
      string.

    - **Verification service indicator**: Optional, recommended claim. It
      is used by a Relying Party to locate a validation service for the
      token. The value is a text string that can be used to locate the service
      or a URL specifying the address of the service. The claim is modelled to
      be eventually represented by the EAT standard claim origination. Until
      such a time as that standard exists, the claim will be represented by
      a custom claim. Value is encoded as text string.

    - **Profile definition**: Optional, recommended claim. It contains the
      name of a document that describes the 'profile' of the token, being
      a full description of the claims, their usage, verification and token
      signing. The document name may include versioning. Custom claim with a
      value encoded as text string.

    - **Implementation ID**: Uniquely identifies the underlying immutable PSA
      RoT. A verification service can use this claim to locate the details of
      the verification process. Such details include the implementation's origin
      and associated certification state. Custom claim with a value encoded as
      byte string.

    - **Client ID**: The partition ID of that secure partition or non-secure
      thread who called the initial attestation API. Custom claim with a value
      encoded as a `signed` integer. Negative number represents non-secure
      caller, positive numbers represents secure callers, zero is invalid.

    - **Security lifecycle**: It represents the current lifecycle state of
      the instance. Custom claim with a value encoded as an integer.

    - **Hardware version**: Optional claim. Globally unique number in EAN-13
      format identifying the GDSII that went to fabrication, HW and ROM. It can
      be used to reference the security level of the PSA-ROT via a certification
      website. Custom claim with a value is encoded as text string.

    - **Boot seed**: It represents a random value created at system boot
      time that will allow differentiation of reports from different system
      sessions. The size is 32 bytes. Custom claim with a value is encoded as
      byte string.

    - **Software components**: Optional, but required in order to be compliant
      with the PSA-SM. It represents the software state of the system. The value
      of the claim is an array of CBOR map entries, with one entry per software
      component within the device. Each map contains multiple claims that
      describe evidence about the details of the software component.

    - **No software measurements**: Optional, but required if no software
      component claims are made. In the event that the implementation does not
      contain any software measurements then it is mandatory to include this
      claim to indicate this is a deliberate state. Custom claim with a value
      encoded as an unsigned integer set to 1.

Each software component claim can include the following properties. Any property
that is not optional must be included:

    - **Measurement type**: Optional claim. It represents the role of the
      software component. Value is encoded as short(!) text string.

    - **Measurement value**: It represents a hash of the invariant software
      component in memory at start-up time. The value must be a cryptographic
      hash of 256 bits or stronger. Value is encoded as byte string.

    - **Version**: Optional claim. It represents the issued software
      version. Value is encoded as text string.

    - **Signer ID**: Optional claim, but required in order to be compliant with
      the PSA-SM. It represents the hash of a signing authority public key.
      Value is encoded as byte string.

    - **Measurement description**: Optional claim. It represents the way in
      which the measurement value of the software component is computed. Value
      is encoded as text string containing an abbreviated description (name)
      of the measurement method.
