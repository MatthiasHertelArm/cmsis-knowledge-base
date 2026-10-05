---
id: "tfm-log-system-design-document-background"
type: "concept"
domain: "security"
title: "Log system design document: Background"
summary: "In current TF-M log system, the SPM and Secure partitions share the same log APIs and implementations. While TF-M is keep evolving, the requirements for the log system has changed:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/tfm_log_system_design_document.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/tfm_log_system_design_document.html#background"
license: "BSD-3-Clause"
mode: "V"
---

In current TF-M log system, the SPM and Secure partitions share the same log
APIs and implementations. While TF-M is keep evolving, the requirements for the
log system has changed:

  - Log level is required for both SPM and SP sides to output message in
    different scenarios.
  - SPM only needs simple log format such as hex and string, while SP needs rich
    formatting.
  - Distinctions on log output between SPM and SP are required.

A new log system is needed to separate the SPM and Secure partitions and to
meet their different requirements.
