---
id: "tfm-hardware-abstraction-layer-introduction"
type: "concept"
domain: "security"
title: "Hardware Abstraction Layer: Introduction"
summary: "TF-M HAL abstracts the hardware-oriented and platform specific operations on the SPE side and provides a set of APIs to the upper layers such as SPM, RoT Service."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/hardware_abstraction_layer.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/hardware_abstraction_layer.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

`TF-M` `HAL` abstracts the hardware-oriented and platform specific
operations on the `SPE` side and provides a set of APIs to the upper
layers such as `SPM`, `RoT Service`.
The `HAL` aims to cover the platform different aspects whereas common
architecturally defined aspects are done generically within the common
`SPE`.
In some cases, although the operations are defined architecturally,
it may not be possible to generalize implementations because lots of information
is only known to platforms.
It is more efficient to define a `HAL` API for those architectural
operations as well.


**Note:** the interfaces from the software perspective only. Please reference


### Design Goals

`TF-M` `HAL` is designed to simplify the integration efforts on
different platforms.

`TF-M` `HAL` is designed to make it easy to use the hardware and
develop the `SPM` and `RoT Service` which need to access the
devices.

`TF-M` `HAL` is designed to make the structure clearer and let the
`TF-M` mainly focus on `PSA` implementation.
