---
id: "tfm-scheduling-for-a-hybrid-platform-s-introduction"
type: "concept"
domain: "security"
title: "Scheduling for a Hybrid Platform Solution: Introduction"
summary: "The Hybrid Platform solution refers to the more generic support for platforms with one local NSPE client and one or more NSPE remote client."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/multi-cpu/hybrid_platform_solution.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/hybrid_platform_solution.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

The Hybrid Platform solution refers to the more generic support for platforms
with one local NSPE client and one or more NSPE remote client. The local client
resides in the same cpu as the SPE, while the remote clients reside on separate
CPUs.

A Hybrid Platform solution requires applications to run from both local and
remote clients.
This inevitably brings some scheduling trade-offs and limitations on the table.

The implementation provided and explained in this section aims to give a
reference implementation for some use-cases where different systems need to
satisfy various scheduling preferences.

Those are broadly:

- SPE is in charge of scheduling
- NSPE is in charge of scheduling
- a BALANCED combination of the above

and are explained below.
