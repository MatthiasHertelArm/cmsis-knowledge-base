---
id: "tfm-memory-mapped-iovecs-conclusion"
type: "concept"
domain: "security"
title: "Memory-mapped IOVECs: Conclusion"
summary: "Based on the analysis and discussion above, we don't consider that an update in the Threat Model is required."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/mm_iovec.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/mm_iovec.html#conclusion"
license: "BSD-3-Clause"
mode: "V"
---

Based on the analysis and discussion above, we don't consider that an update
in the Threat Model is required.

Relaxing the usage of MM-IOVEC to higher isolation level does not change the
threat landscape and does not violate the isolation rules.



### Build options and configs


Unchanged



### Remarks


PRoT and ARoT must not access vectors after unmapping.


--------------

*SPDX-FileCopyrightText: Copyright The TrustedFirmware-M Contributors*
