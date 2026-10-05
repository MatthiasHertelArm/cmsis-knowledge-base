---
id: "tfm-trusted-firmware-m"
type: "concept"
domain: "security"
title: "Trusted Firmware M"
summary: "Trusted Firmware-M (TF-M) implements the Secure Processing Environment (SPE) for Armv8-M, Armv8.1-M architectures (e.g. the Cortex-M33, Cortex-M23, Cortex-M55, Cortex-M85 processors) and dual-core platforms."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/introduction/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/introduction/.html"
license: "BSD-3-Clause"
mode: "V"
---

Trusted Firmware-M (TF-M) implements the Secure Processing Environment (SPE)
for Armv8-M, Armv8.1-M architectures (e.g. the Cortex-M33, Cortex-M23,
Cortex-M55, Cortex-M85 processors) and dual-core platforms.
It is the platform security architecture reference implementation aligning with
PSA Certified guidelines, enabling chips, Real Time Operating Systems and
devices to become PSA Certified.

TF-M relies on an isolation boundary between the Non-secure Processing
Environment (NSPE) and the Secure Processing Environment (SPE). It can but is
not limited to using the Arm TrustZone technology on Armv8-M and Armv8.1-M
architectures. In pre-Armv8-M architectures physical core isolation is required.

**TF-M consists of:**

- Secure Boot to authenticate NSPE and SPE images
- TF-M Core for controlling the isolation, communication
  and execution within SPE and with NSPE
- Crypto, Internal Trusted Storage (ITS), Protected Storage (PS),
  Firmware Update and Attestation secure services

TF-M implements PSA-FF-M defined IPC and SFN mechanisms to allow communication
between isolated firmware partitions. TF-M is highly configurable allowing users
to only include the required secure services and features. Project provides
Base_configuration build with just TF-M core and platform drivers and 4 predefined
configurations known as tf-m_profiles. TF-M Profiles or TF-M base can
be configured to include required services and features as described in the
tf-m_configuration section.

Applications and Libraries in the Non-secure Processing Environment can
utilize these secure services with a standardized set of PSA Functional APIs.
Applications running on Cortex-M devices can leverage TF-M services to ensure
secure connection with edge gateways and IoT cloud services. It also protects
the critical security assets such as sensitive data, keys and certificates on
the platform. TF-M is supported on several Cortex-M based
Microcontrollers and Real Time Operating
Systems (RTOS).

Terms `TFM` and `TF-M` are commonly used in documents and code and both
refer to `Trusted Firmware M.` Glossary has the list
of terms and abbreviations.
