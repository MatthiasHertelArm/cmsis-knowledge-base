---
id: "tfm-ff-m-isolation-introduction"
type: "concept"
domain: "security"
title: "FF-M Isolation: Introduction"
summary: "This chapter describes the definitions from Firmware Framework for M (FF-M) [1] and analyzes the possible implementation keypoints."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/ff_isolation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/ff_isolation.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

This chapter describes the definitions from Firmware Framework for M (FF-M) [1]_
and analyzes the possible implementation keypoints.


### Isolation Levels

There are 3 isolation levels (1-3) defined in FF-M, the greater level number has
more isolation boundaries.

The definition for Isolation Level 1:

- L1.1 NPSE needs protection from nobody.
- L1.2 SPE needs protection from NSPE.

The definition for Isolation Level 2:

- L2.1 NPSE needs protection from nobody.
- L2.2 Application Root of Trust (ARoT) needs protection from NSPE.
- L2.3 PSA Root of Trust (PRoT) needs protection from NSPE and ARoT.

The definition for Isolation Level 3:

- L3.1 NPSE needs protection from nobody.
- L3.2 Secure Partition needs protection from NSPE and other Secure Partitions.
- L3.3 PSA Root of Trust (RoT) domain needs protection from NSPE and all Secure
  Partitions.


**Important:** A Secure Partition RoT Service is a Root of Trust Service implemented within a Secure Partition. An Application RoT Service must be implemented as a Secure Partition RoT Service. But it is implementation-defined whether a PSA RoT Service is a Secure Partition RoT Service. Here listed several possible PSA RoT Service implementation mechanisms: 1. Implement PSA RoT Services in Secure Partitions with respective boundaries. 2. Implement PSA RoT Services in Secure Partitions, but no boundaries between these Secure Partitions as they are in the PSA RoT Domain. 3. Implement PSA RoT Services in a customized way instead of Secure Partitions, an internal library of PSA RoT domain e.g. TF-M chooses the 2nd option to balance performance and complexity.


### Isolation Rules

The essence of isolation is to protect the assets of one protection domain from
being accessed from other domains. The isolation levels define where the
isolation boundaries should be placed, the isolation rules define the strength
of the isolation the boundaries should offer.


**Note:** Refer to chapter *Memory Assets* in FF-M [1]_ to know asset class items. Assets are represented by memory addresses in the system memory map, which makes assets named *Memory Assets*. The often-seen asset items are ROM, RAM, and memory-mapped peripherals.


#### Memory Asset Class

There are 3 memory asset classes defined in FF-M:

- Code
- Constant data
- Private data

There are 7 isolation rules for protecting assets described in chapter `3.1`
of FF-M 1.0 [1]_ and chapters `8.4` to `8.5` of FF-M 1.1 [2]_. The following
is a summary of the rules:

- I1. (Changed in FF-M 1.1) Private data is not executable.
- I2. Only private data is writable.
- I3. If domain A needs protection from domain B, then Private data in domain A
  cannot be accessed by domain B.
- I4. (Optional, changed in FF-M 1.1) If domain A needs protection from domain
  B, then Code and Constant data in domain A, which is not part of a shared
  library, is not readable or executable by domain B.
- I5. (Optional, changed in FF-M 1.1) Code in a domain, which is not part of a
  shared library, is not executable by any other domain.
- I6. (Optional) All assets in a domain are private to that domain and cannot be
  accessed by any other domain, with the following exception:
  The domain containing the SPM can only access Private data and Constant data
  assets of other domains when required to implement the PSA Firmware Framework
  API.
- I7. (Optional, added in FF-M 1.1) Constant data is not executable.

 The first 3 rules from `I1` to `I3` define the mandatory rules to comply
 with the PSA security model, while `I4` to `I7` are optional rules to
 enhance the isolation boundaries.


**Important:** There is a table in chapter `3.1.2` of FF-M 1.0 [1]_ under `I1` that lists the asset types and allowed access method. Preventing executable access to constant data costs more hardware resources, so there is an optional rule I7 created in FF-M 1.1 [2]_ to aid implementations with constrained hardware resources.


### Hardware Infrastructure

To implement a secure system, the hardware security framework (e.g. TrustZone or
multiple-core) and their auxiliary components (e.g. SAU) are required to ensure
the isolation between SPE and NSPE, as described in Trusted Base System
Architecture for M (TBSA-M) [3]_.


**Important:** The interface between secure and non-secure states needs to be fully enumerated and audited to prove the integrity of the secure state isolation.

Besides this SPE and NSPE isolation mechanism, the following analyzes the
implementation rules to find out the hardware requirements for isolation inside
SPE domains:

- I1, I2 and I7: The assets can be categorized into 3 Memory Asset Class,
  each type has the specific access rules.
- I3: The private data access from the prevented domain needs to be blocked.
- I4: All the assets access from the prevented domain needs to be blocked.
- I5: Code execution from all other domains (even the domain not prevented
  from) needs to be blocked.
- I6: All the assets access from all other domains (includes non-prevented
  domain) needs to be blocked, but, SPM is an exception, which can access the
  private data and constant data of the current domain.

The above items list the requirements for memory access, here are two more
points:

- If the memory device or the peripheral are shared between multiple hosts
  (such as multiple CPU or DMA, etc.), specific hardware protection units need
  to be available for validating accesses to that device or peripheral.
- The MMIO range for Secure Partitions is not allowed to be overlapped, which
  means each partition should have exclusive memory-mapped region if they
  require a peripheral device. The memory-mapped region is regarded as
  the private data so access to this area needs to be validated.
