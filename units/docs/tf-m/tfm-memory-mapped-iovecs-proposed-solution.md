---
id: "tfm-memory-mapped-iovecs-proposed-solution"
type: "concept"
domain: "security"
title: "Memory-mapped IOVECs: Proposed solution"
summary: "Remove the tfm_invalid_config check for TFM_ISOLATION_LEVEL GREATER 1 and PSA_FRAMEWORK_HAS_MM_IOVEC. This change enables MM-IOVEC for IL2 and IL3."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/mm_iovec.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/mm_iovec.html#proposed-solution"
license: "BSD-3-Clause"
mode: "V"
---

Remove the tfm_invalid_config check for `TFM_ISOLATION_LEVEL GREATER 1` and
`PSA_FRAMEWORK_HAS_MM_IOVEC`. This change enables MM-IOVEC for IL2 and IL3.

No changes to the SPM implementation are required.
However additional responsibilities are introduced for relevant partitions.

This solution enables:
 - mapping and passing of Secure Shared Memory, for example a mmio flash
 - mapping and passing NSPE buffers

This document uses the Generic TF-M Threat Model to assess the impact of the
solution.



### Targeted Threat analysis


This section presents a simplified text-based data flow sequence (DF) to help
analyse whether boundaries, data classification and actors need to change.


* DF-1..DF-5 - Data provided by NSPE

DF-1
NS sends a request to SPE with iovecs (already covered)

DF-2 - 1st partition

+ the partition maps the input/output vectors
+ processes the data
+ temporarily copies the NS vector pointers in own memory/stack and
  forward those to another partition via `psa_call()`
+ unmap the vectors

DF-3 - 2nd partition
+ the partition maps the input/output vectors
+ processes the data
+ unmap the vectors

DF-4 - 1st partition
+ the partition maps the input/output vectors
+ processes the data
+ unmap the vectors

DF-5
NS resumes with the processed data in the output vectors

* DF-6..DF-10 - Data provided by SPE

DF-6
NS sends a request to SPE WITHOUT iovecs (already covered)

DF-7 - 1st partition

+ the partition process the request, prepares the SSM references
+ processes the data
+ temporarily copies the SSM pointers into vectors in own memory/stack
  and forward those to another partition via psa_call()
+ unmap the vectors

DF-8 (equal to DF-3) - 2nd partition

+ the partition maps the input/output vectors
+ processes the data
+ unmap the vectors

DF-9 - 1st partition

+ the partition maps the input/output vectors
+ processes the data
+ unmap the vectors

DF-10
NS resumes with the processed data in the output vectors


We analyze if with the DF above the threats scenario is worsened.
We assume IL3.
The NSPE to SPE interactions are already covered by the Generic TF-M Threat
Model.
We limit the analysis for the MM-IOVEC mapping/unmapping between the partitions.

DF-1, DF-6
Already covered in Generic TF-M Threat Model

DF-2, DF-3, DF-4, DF-7, DF-8, DF-9
Not covered in the Generic TF-M Threat Model because of the definitions of
trusted boundaries (see section https://trustedfirmware-m.readthedocs.io/en/latest/security/threat_models/generic_threat_model.html#data-flows-inside-spe-informative)


**Spoofing**
The caller partition may try to access and use another's partition identity

Not a threat.
The caller partition's identity is assigned and checked by SPM and cannot be
directly provided.


**Tampering**
The caller partition may try to change or modify persistent data

Not a threat.
We trust the partition to not behave as an attacker (see FF-M).

Also, the caller partition can already map/unmap vectors from NS or from SSM by
"design (of the memory)".


**Repudiation**
The caller partition may try to perform prohibited operations in a system that
lacks the ability to trace the operations.

Not a threat.
We trust the partition to behave responsibly.


**Information disclosure**
The caller partition may try to access a file or data it was not granted access
to.

Not a threat.
We trust the partition to not behave as an attacker (see FF-M).

Allowing the mapping/unmapping does not change the isolation rules. Thus if
unprivilege code tries to access priv or another unpriv data, the system raises
a Fault.
Also, the caller partition can already map/unmap vectors from NS or from SSM by
"construction".


**DoS**
Not covered in the threat model

Out of scope as per TF-M Generic Threat Model.


**Elevation of privilege**
The caller partition may try to gain privileged access to the data

Not a threat.
We trust the partition to not behave as an attacker.



### Interaction with the isolation model analysis


According to FF-Mv1.1, in an implementation with IL2, IL3, MM-IOVEC provides a
mechanism that may conﬂict with the isolation rules.

A. Possible conflict

With IL3 a Secure Partition is not permitted to access another Secure
Partition’s Private data.
MM-IOVEC may provide a mechanism for one Secure Partition to access the other’s
Private data.

A. Mitigation

SPM implemented in TF-M ensures that:

 * the mapped vectors fulfill the requirements for the callee partition by
   testing the vectors with `cmse_check_address_range` when mapping/unmapping
 * the execution environment for ARoT provided by SPM is such that a ARoT cannot
   access data belonging
   to other ARoTs. This is enforced regardless the MM-IOVEC support
   (PSA_FRAMEWORK_HAS_MM_IOVEC)


B. Possible conflict

In a system that implements isolation rule I6 (see [FF-M] §3.1.5), only the SPM
is permitted to access memory in another protection domain when required.
MM-IOVEC can provide access from a Secure Partition directly to client memory.

B. Mitigation

Isolation rule I6 is not implemented.


C. Possible imprecise mapping

The mapping mechanism can provide more access than is strictly required.

C. Mitigation

We must take into account the hardware limitations that can impact mapping
precision.
Any client of the API must take steps to mitigate the MPU granularity, for
example by aligning the buffer and buffer size in memory.
It is IMPLEMENTATION DEFINED how such imprecise mappings are handled by the
implementation. The decision to permit imprecise mappings depends on the
security requirements for the system, and the nature of the additional access.

An implementation that provides MM-IOVEC functionality must document its
behavior when an input or output vector mapping is imprecise.

The services designed and implemented to handle such payloads may need to
provide platform hooks to correctly set the MPU alignment for the SSM.
Alternatively, the MPU can be set once at init stage to correctly bound the
region limits.
