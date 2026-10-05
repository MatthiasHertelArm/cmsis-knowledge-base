---
id: "mcuboot-bootloader-dependency-check"
type: "concept"
domain: "boot-update"
title: "Bootloader: Dependency check"
summary: "MCUboot can handle multiple firmware images. It is possible to update them independently but in many cases it can be desired to be able to describe dependencies between the images (e.g. to ensure API compliance and avoid interoperability issues)."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#dependency-check"
license: "Apache-2.0"
mode: "V"
---

MCUboot can handle multiple firmware images. It is possible to update them
independently but in many cases it can be desired to be able to describe
dependencies between the images (e.g. to ensure API compliance and avoid
interoperability issues).

The dependencies between images can be described with additional TLV entries in
the protected TLV area after the end of an image. There can be more than one
dependency entry, but in practice if the platform only supports two individual
images then there can be maximum one entry which reflects to the other image.

At the phase of dependency check all aborted swaps are finalized if there were
any. During the dependency check the bootloader verifies whether the image
dependencies are all satisfied. If at least one of the dependencies of an image
is not fulfilled then the swap type of that image has to be modified
accordingly and the dependency check needs to be restarted. This way the number
of unsatisfied dependencies will decrease or remain the same. There is always at
least 1 valid configuration. In worst case, the system returns to the initial
state after dependency check.

For more information on adding dependency entries to an image,
see: [imgtool](https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/imgtool.md).
