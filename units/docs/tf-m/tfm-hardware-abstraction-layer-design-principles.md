---
id: "tfm-hardware-abstraction-layer-design-principles"
type: "concept"
domain: "security"
title: "Hardware Abstraction Layer: Design Principles"
summary: "As TF-M runs on resource-constrained devices, the HAL tries to avoid multiple level abstractions which cost more resources."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/hardware_abstraction_layer.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/hardware_abstraction_layer.html#design-principles"
license: "BSD-3-Clause"
mode: "V"
---

As `TF-M` runs on resource-constrained devices, the `HAL` tries to
avoid multiple level abstractions which cost more resources.

Part of the `HAL` interfaces does not focus on exact hardware operations
such as power on/off or PIN manipulation.
Instead, the `HAL` abstracts higher-level interfaces to reserve the
implementation flexibility for the platform vendors.

The `TF-M` `HAL` should be easy to deprecate APIs and provide
compatibilities.
Any API incompatibility should be detected during building.

`TF-M` relies on the `HAL` APIs to be implemented correctly and
trusts the `HAL` APIs.
`TFM` can provide assertions to detect common programming errors but
essentially no further extensive checks will be provided.
