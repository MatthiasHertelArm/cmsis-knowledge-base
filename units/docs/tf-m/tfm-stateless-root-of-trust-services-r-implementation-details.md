---
id: "tfm-stateless-root-of-trust-services-r-implementation-details"
type: "concept"
domain: "security"
title: "Stateless Root of Trust Services Reference: Implementation Details"
summary: "This chapter describes the implementation-defined items, including stateless handle value definition, tooling update, and programming API changes."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/stateless_rot_service.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/stateless_rot_service.html#implementation-details"
license: "BSD-3-Clause"
mode: "V"
---

This chapter describes the implementation-defined items, including stateless
handle value definition, tooling update, and programming API changes.


### Stateless Handle Value Definition


The index, stateless indicator, and service version information are encoded into
a handle by the manifest tooling, and then generated to header file `sid.h`.


* - Bits
  - Field Description
* - bit 31
  - reserved
* - bit 30
  - stateless handle indicator bit, always 1
* - bit 29 - bit 16
  - reserved
* - bit 15 - bit 8
  - service version requested by client - for client version check
* - bit 7 - bit 5
  - reserved
* - bit 4 - bit 0
  - the handle index, [0, 31]
Since connection-based services and stateless services share the same PSA API
`psa_call()`, an indicator bit is set in the handle indicate the type of the
handle. If it is set, the handle is stateless, and definition is as described
in the table above. Maximum connection-based handle is 0x3FFFFFFF, thus the
indicator bit is always 0.

The index is used for organizing stateless services in manifest tool and
locating a stateless service in SPM logic. A range of index [0, 31] is the
initial implementation. Future expansion is possible.


### Tooling Support


TF-M provides a tool (`tools/tfm_parse_manifest_list.py`) to generate source
header files required by partition and services. For example, the generated
`sid.h` contains service ID and version. The tooling is extended to generate
stateless handle from partition manifests automatically.

The `stateless_handle` attribute in manifest is only supported by partitions
with firmware framework version 1.1.

- If `stateless_handle` in manifest is set to an integer, the index is
  `stateless_handle - 1`.
- If it is `auto` or not set, the first empty index in range [0, 31] is
  assigned.
- Other settings - tooling reports an error.

Finally, the tooling encodes the handle according to definitions in
Stateless Handle Value Definition section, and writes them to `sid.h`
header file.


### Changes in Programming API


This chapter describes the changes in programming API for stateless services.
The following APIs' behaviours and message data structure members are updated to
support the stateless service.


#### psa_connect()


According to FF-M v1.1, client calling `psa_connect()` with the SID of a
stateless RoT Service is a `PROGRAMMER_ERROR`.


#### psa_close()


According to FF-M v1.1, client passing a stateless handle to call this API is a
`PROGRAMMER_ERROR`.


#### psa_call()


```c

psa_status_t psa_call(psa_handle_t handle, int32_t type,
                      const psa_invec *in_vec, size_t in_len,
                      psa_outvec *out_vec, size_t out_len)
```
API parameters and behaviour change:

1. The `handle` parameter must be a stateless handle defined in
   `psa_manifest/sid.h` when requesting a stateless service.
2. This API validates stateless handle, decodes index and service version
   information from it. SPM uses the index to know which stateless service is
   requested.
3. This API performs some operations as `psa_connect()` does, such as the
   authorization check, service and client version check, and handle space
   allocation.

Service behaviour change during a "psa_call":

Service does not accept connection and disconnection messages. After a
"psa_call" request is serviced, it calls `psa_reply()`, frees the connection
handle to handle pool.


#### psa_set_rhandle()


According to FF-M v1.1, stateless service calling this API on a message is a
`PROGRAMMER_ERROR` and it will never return.


#### psa_msg_t type


The `rhandle` member of a `psa_msg_t` type received by a stateless RoT
Service is always `NULL`.
