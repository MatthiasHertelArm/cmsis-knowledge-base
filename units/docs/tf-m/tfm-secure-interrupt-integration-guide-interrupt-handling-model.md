---
id: "tfm-secure-interrupt-integration-guide-interrupt-handling-model"
type: "concept"
domain: "security"
title: "Secure Interrupt Integration Guide: Interrupt Handling Model"
summary: "TF-M supports the two interrupt handling models defined by FF-M:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/tfm_secure_irq_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/tfm_secure_irq_integration_guide.html#interrupt-handling-model"
license: "BSD-3-Clause"
mode: "V"
---

TF-M supports the two interrupt handling models defined by FF-M:

- First-Level Interrupt Handling (FLIH)

  In this model, the interrupt handling is carried out immediately when the
  interrupt exception happens.

  The interrupt handling can optionally set an interrupt signal for the Secure
  Partition Thread to have further data processing.

- Second-Level Interrupt Handling (SLIH)

  In this model, the interrupt handling is deferred after the interrupt
  exception. The handling occurs in the Secure Partition Thread thus is subject
  to scheduling.

The FLIH supports handling an interrupt in a bounded time, but very limited APIs
are allowed in the FLIH handling because the handling occurs in an special
exception context.

The SLIH is deferred and subject to scheduling but all Secure Partition APIs are
allowed as the SLIH handling is in the Secure Partition Thread.

Both the FLIH and the SLIH can be used by Secure Partitions which conform to
Firmware Framework v1.1.

While the SLIH is the only supported model for Secure Partitions which conform
to Firmware Framework v1.0.

Please refer to chapter 6.2 of FF-M v1.1 [1]_ for more details on the interrupt
handling models.
