---
id: "tfm-uniform-secure-service-signature-declaring-secure-service-interface"
type: "concept"
domain: "security"
title: "Uniform Secure Service Signature: Declaring secure service interface"
summary: "The following alternative secure service signature is proposed as an amendment to existing implementation."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_uniform_secure_service_signature.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_uniform_secure_service_signature.html#declaring-secure-service-interface"
license: "BSD-3-Clause"
mode: "V"
---

The following alternative secure service signature is proposed as an
amendment to existing implementation.


### Individual signatures - current method


A `<service_name>_veneers.c` file is created in the `secure_fw/ns_callable`
directory, that specifies the signature for each veneer function, and calls the
secure function from the veneers. The respective
`interface/include/<service_name>_veneers.h` file with the veneer declarations
have to be created and maintained manually.
Note that at present TF-M framework limits the range of valid return values a
secure service can provide, reserving a range for framework error codes.


### Uniform signatures - proposal


The proposal is to use a uniform signature for all the secure functions of the
secure service. There are multiple advantages of this method:

- TF-M Core can do a sanity check on the access rights of the veneer
  parameters, and there is no need for the secure services to make these checks
  individually. Please note that in the present implementation sanity check is
  only fully supported for level 1 isolation.

- The veneer declarations and implementations for the secure functions can be
  generated automatically from a template (using the secure function list in the
  secure service's manifest)

The signature for such secure services would look like this:

```c

psa_status_t secure_function_name(struct psa_invec *in_vec, size_t in_len,
                                  struct psa_outvec *out_vec, size_t out_len);
```
where


#### Return value:


`psa_status_t` is a status code whose values are described in PSA Firmware
Framework (as in version 1.0-beta-0 chapter 4.3.3).


#### Note:

The return value limitations imposed by TF-M framework for proprietary
secure service veneers would not apply to secure services using the uniform
signature. This is analogous to how PSA Firmware Framework handles values
returned by `psa_reply()` function.


#### Arguments:


```c

/**
 * A read-only input memory region provided to a RoT Service.
 */
typedef struct psa_invec {
    const void *base;   /*!< the start address of the memory buffer */
    size_t len;         /*!< the size in bytes */
} psa_invec;

/**
 * A writable output memory region provided to a RoT Service.
 */
typedef struct psa_outvec {
    void *base;         /*!< the start address of the memory buffer */
    size_t len;         /*!< the size in bytes */
} psa_outvec;

/**
 * in_len: the number of input parameters, i.e. psa_invecs
 * out_len: the number of output parameters, i.e. psa_outvecs
 */
```
The number of vectors that can be passed to a secure service is constrained:

```c

in_len + out_len <= PSA_MAX_IOVEC
```
The veneer function declarations and implementations are generated in the
`interface/include/tfm_veneers.h` and `secure_fw\ns_callable\tfm_veneers.c`
files respectively. The veneer functions are created with the name
`tfm_<secure_function_name>_veneer`

Services that implement the uniform signature do not need to manually fill
the template veneer function to call `TFM_CORE_SFN_REQUEST` macro.
