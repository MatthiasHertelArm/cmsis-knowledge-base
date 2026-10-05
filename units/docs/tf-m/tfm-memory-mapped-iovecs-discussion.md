---
id: "tfm-memory-mapped-iovecs-discussion"
type: "concept"
domain: "security"
title: "Memory-mapped IOVECs: Discussion"
summary: "The FF-M architecture assumes that RoT partitions do not behave maliciously and are implemented correctly. Through secure boot, such RoTs are authenticated."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/mm_iovec.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/mm_iovec.html#discussion"
license: "BSD-3-Clause"
mode: "V"
---

The FF-M architecture assumes that RoT partitions do not behave maliciously and
are implemented correctly. Through secure boot, such RoTs are authenticated.

Based on the above, there is no need to introduce new trust boundaries between
partitions' domains.

The assets protection does not change when the mapping/unmapping is performed,
because the isolation boundaries are enforced (take place) when SPM changes the
running partition and is independent from the MM-IOVEC mapping.

Accessing NS buffers with IL3 is not any different from IL1 since the isolation
domain b/w NS and the PRoT-ARoT does not change.

Accessing non-private shared secure data does not conflict with the isolation
domains, that is, there's no direct data sharing b/w partitions.

SPM ensures that the vectors can be accessed by the partitions according to
their boundaries settings, irrespective of the PSA_FRAMEWORK_HAS_MM_IOVEC
capability.

When mapping/unmapping is required, additional memory checks are performed to
ensure the calling partition can safely access the given vectors.

The non-private shared secure regions need to have the correct attributes for
the mapping partitions to be consumed.
