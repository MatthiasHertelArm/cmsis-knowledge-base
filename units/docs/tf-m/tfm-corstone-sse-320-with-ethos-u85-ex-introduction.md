---
id: "tfm-corstone-sse-320-with-ethos-u85-ex-introduction"
type: "concept"
domain: "security"
title: "Corstone SSE-320 with Ethos-U85 Example Subsystem for Ecosystem FVP: Introduction"
summary: "Corstone-320 is an Arm reference subsystem for secure System on Chips containing an Armv8.1-M Cortex-M85 processor and LCM, KMU and SAM IPs. and an Ethos-U85 neural network processor. It is an MPS4 based platform."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/arm/mps4/corstone320/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/arm/mps4/corstone320/.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

Corstone-320 is an Arm reference subsystem for secure System on Chips containing
an Armv8.1-M Cortex-M85 processor and LCM, KMU and SAM IPs. and an
Ethos-U85 neural network processor. It is an MPS4 based platform.

This platform port supports all TF-M regression tests (Secure and Non-secure)
with Isolation Level 1 and 2.


**Note:** For Ethos-U85 IP this platform support only provides base address, interrupt number and an example NPU setup as non-secure, unprivileged.


**Note:** For Armclang compiler v6.18 or later version is required.
