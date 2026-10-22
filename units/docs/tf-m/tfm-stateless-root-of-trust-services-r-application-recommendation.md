---
id: "tfm-stateless-root-of-trust-services-r-application-recommendation"
type: "concept"
domain: "security"
title: "Stateless Root of Trust Services Reference: Application Recommendation"
summary: "There are particular services that do not need sessions. The access to the service is a one-shot connection."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/stateless_rot_service.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/stateless_rot_service.html#application-recommendation"
license: "BSD-3-Clause"
mode: "V"
---

There are particular services that do not need sessions. The access to the
service is a one-shot connection. These services provide standalone operations
that do not require any non-volatile state of resources to be maintained by the
RoT service itself or do not expose any kind of context or session to the
caller. Such services are recommended to be implemented as stateless, to provide
quick access and to avoid extra overheads.

In this case, `rhandle` access would be prohibited as it is used for saving
state or non-volatile resources while stateless services do not need them.


### Update Feasibility of Existing Services


TF-M native services are used widely. They only need standalone operations and
do not need to keep state between sessions. For example, the service in Crypto
partition does not do anything during `psa_connect()` or `psa_close()`
process. Same for services in other partitions, thus all of them can be
implemented as stateless.

Analysis for them:


* - Partition
  - Number of Services
  - Can be Stateless
* - ITS
  - 4
  - All
* - PS
  - 5
  - All
* - Crypto
  - 1
  - All
* - FWU
  - 6
  - All
* - Platform
  - 4
  - All
* - Initial Attestation
  - 2
  - All
Other services are not analyzed here.


### Grouping Services


Stateless service table is stored statically, and TF-M supports 32 stateless
services currently.

Similar stateless services in a partition could be grouped, and assign one
`SID` for the group. The `type` parameter in `psa_call()` could be
extended to identify the service in group. In this case, it is recommended to
use consecutive values for `type`.

It is recommended that each Secure Partition declares one stateless service
and uses the type parameter to distinguish different stateless services.
Therefore, more stateless services can be supported.


### Migrating to Stateless Services


Please refer to Chapter 4 "Stateless Root of Trust services", Appendix B.3.2
"Using a stateless RoT Service", and Appendix D "Implementing session-less RoT
Services" in FF-M v1.1 document for details on which kind of service can be
stateless and how to implement a stateless service.
