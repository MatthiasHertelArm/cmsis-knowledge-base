---
id: "tfm-initial-attestation-service-integr-initial-attestation-service-compile-time"
type: "concept"
domain: "security"
title: "Initial Attestation Service Integration Guide: Code structure / Initial Attestation Service compile time options"
summary: "There is a defined set of flags that can be used to compile in/out certain service features. The config_base.cmake file sets the default values of those flags. The list of flags are:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_attestation_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_attestation_integration_guide.html#initial-attestation-service-compile-time-options"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Code structure_

There is a defined set of flags that can be used to compile in/out certain
service features. The `config_base.cmake` file sets the default values of
those flags. The list of flags are:

- `ATTEST_INCLUDE_OPTIONAL_CLAIMS`: Include also the optional claims to the
  attestation token. Default value: ON in base configure and profile large while
  OFF in profile small and medium.
- `ATTEST_INCLUDE_COSE_KEY_ID`: COSE key-id is an optional field in the COSE
  unprotected header. Key-id is calculated and added to the COSE header based
  on the value of this flag. Default value: OFF.
- `SYMMETRIC_INITIAL_ATTESTATION`: Select symmetric initial attestation.
  Default value: OFF.
- `ATTEST_STACK_SIZE`- Defines the stack size of the Initial Attestation
  Partition. This value mainly depends on the build type(debug, release and
  minisizerel) and compiler.
  Default value: Depends on the profile.
- `ATTEST_KEY_BITS` Defines the size of the initial attestation key, in bits.
  Default value: 256.
- `PSA_INITIAL_ATTEST_MAX_TOKEN_SIZE` Defines the maximum possible size of a
  token.
  Default value: 0x250.


#### Related compile time options

- `BOOT_DATA_AVAILABLE`: The boot data is expected to be present in the shared
  data area between the boot loader and the runtime firmware when set to `ON`.
  Otherwise, when it's `OFF` TF-M does not check the content of the shared
  data area but instead assumes that the TLV header is present and valid (the
  magic number is correct) and there are no data entries. Its default value
  depends on the BL2 flag.
