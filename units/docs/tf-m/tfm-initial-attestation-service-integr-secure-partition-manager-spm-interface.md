---
id: "tfm-initial-attestation-service-integr-secure-partition-manager-spm-interface"
type: "concept"
domain: "security"
title: "Initial Attestation Service Integration Guide: Code structure / Secure Partition Manager (SPM) interface"
summary: "The Initial Attestation Service defines the following interface towards the secure partition manager (SPM). System integrators must port this interface according to their SPM implementation."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_attestation_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_attestation_integration_guide.html#secure-partition-manager-spm-interface"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Code structure_

The Initial Attestation Service defines the following interface towards the
secure partition manager (SPM). System integrators **must** port this interface
according to their SPM implementation.

```c

enum psa_attest_err_t
attest_get_boot_data(uint8_t major_type, void *ptr, uint32_t len);

enum psa_attest_err_t
attest_get_caller_client_id(int32_t *caller_id);
```
- `attest_get_boot_data()`: Service can retrieve the relevant data from shared
  memory area between boot loader and runtime software. It might be the case
  that only SPM has direct access to the shared memory area, therefore this
  function can be used to copy the service related data from shared memory to
  a local memory buffer. In TF-M implementation this function must be called
  during service initialization phase, because the shared memory region is
  deliberately overlapping with secure main stack to spare some memory and reuse
  this area during execution. If boot loader is not available in the system to
  provide attributes of software components then this function must be
  implemented in a way that just initialize service's memory buffer to:

```c

struct shared_data_tlv_header *tlv_header = (struct shared_data_tlv_header *)ptr;
tlv_header->tlv_magic   = 2016;
tlv_header->tlv_tot_len = sizeof(struct shared_data_tlv_header *tlv_header);
```
- `attest_get_caller_client_id()`: Retrieves the ID of the caller thread.
- `tfm_client.h`: Service relies on the following external definitions, which
  must be present or included in this header file:

```c

typedef struct psa_invec {
    const void *base;
    size_t len;
} psa_invec;

typedef struct psa_outvec {
    void *base;
    size_t len;
} psa_outvec;
```
