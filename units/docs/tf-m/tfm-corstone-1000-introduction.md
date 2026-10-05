---
id: "tfm-corstone-1000-introduction"
type: "concept"
domain: "security"
title: "Corstone-1000: Introduction"
summary: "The ARM's Corstone-1000 platform is a reference implementation of PSA FF-M architecture where NSPE and SPE environments are partitioned/isolated into Cortex-A35 and Cortex-M0+ respectively."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/arm/corstone1000/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/arm/corstone1000/.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

The ARM's Corstone-1000 platform is a reference implementation of PSA FF-M
architecture where NSPE and SPE environments are partitioned/isolated into
Cortex-A35 and Cortex-M0+ respectively.

Cortex-M0+ acting as Secure Enclave is the Root-of-trust of SoC. Its
software comprises of two boot loading stages, i.e. Bl1 and Bl2 (based on
mcuboot) and TF-M as run time software. Cortex-A35, also referred as host,
is treated as non-secure from the Secure Enclave perspective.
The Cortex-A35 is brought out of rest by Secure Enclave in aarch64 bit mode,
and boots the software ecosystem based on linux, u-boot, UEFI run time
services, TF-A, Secure Partitions and Optee.

The communication between NSPE and SPE is based on PSA IPC protocol running on
top of the RSE communication protocol. The Corstone-1000 supports only the
`Embed protocol`, and the ATU support is removed.

The secure enclave subsystem has ARM's CC-312 (Crypto Cell) hardware to
accelerate cryptographic operations. Additionally, platform supports Secure Debug
using SDC-600 as the communication interface between host debugger and platform
target. The platform has the build option to enable secure debug protocol to
unlock debug ports during boot time. The protocol is based on ARM's ADAC
(Authenticated Debug Access Control) standard.
