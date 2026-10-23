---
id: "tfm-log-system-design-document-log-devices"
type: "concept"
domain: "security"
title: "Log system design document: Log Devices"
summary: "In most of the cases, a serial device could be used as a log device. And in other particular cases, a memory-based log device could be applied as well. These log device interfaces are abstracted into HAL APIs."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/tfm_log_system_design_document.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/tfm_log_system_design_document.html#log-devices"
license: "BSD-3-Clause"
mode: "V"
---

In most of the cases, a serial device could be used as a log device. And in
other particular cases, a memory-based log device could be applied as well.
These log device interfaces are abstracted into HAL APIs.


**Note:** It is not recommended to reuse the same HAL for both SPM and SP log outputting especially when SPM and SP run under different privileged level, which makes them have a different information confidential level. Unless: - The SPM log outputting would be disabled as silence in the release version.

--------------

*SPDX-FileCopyrightText: Copyright The TrustedFirmware-M Contributors*
