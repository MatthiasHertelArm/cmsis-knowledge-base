---
id: "tfm-corstone-sse-310-with-ethos-u55-u6-introduction"
type: "concept"
domain: "security"
title: "Corstone SSE-310 with Ethos-U55/U65 Example Subsystem for Arm Ecosystem FVP and for MPS3 (AN555): Introduction"
summary: "Corstone-310 (formerly Corstone-Polaris) is an Arm reference subsystem for secure System on Chips containing an Armv8.1-M Cortex-M85 processor and an Ethos-U55/U65 neural network processor. It is an MPS3 based platform with the usual MPS3 peripherals."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/arm/mps3/corstone310/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/arm/mps3/corstone310/.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

Corstone-310 (formerly Corstone-Polaris) is an Arm reference subsystem for
secure System on Chips containing an Armv8.1-M Cortex-M85 processor and an
Ethos-U55/U65 neural network processor. It is an MPS3 based platform with the
usual MPS3 peripherals.

This platform port supports all TF-M regression tests (Secure and Non-secure)
with Isolation Level 1 and 2.


**Note:** For Ethos-U55/U65 IP this platform support only provides base address, interrupt number and an example NPU setup as non-secure, unprivileged.


**Note:** For Armclang compiler v6.18 or later version is required.
