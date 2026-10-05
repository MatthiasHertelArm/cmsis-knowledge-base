---
id: "tfm-hardware-abstraction-layer-overview"
type: "concept"
domain: "security"
title: "Hardware Abstraction Layer: Overview"
summary: "This section provides an overview of the abstraction layer structure."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/hardware_abstraction_layer.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/hardware_abstraction_layer.html#overview"
license: "BSD-3-Clause"
mode: "V"
---

This section provides an overview of the abstraction layer structure.

Here lists a minimal set of necessary functionalities:

  - **Isolation API**: Provides the necessary isolation functionalities required
    by the `PSA-FF-M` and `TBSA-M`, and provides APIs to `SPM`
    to check the permissions of memory access.
  - **Platform API**: Provides the platform initialization, platform-specific
    memory information, system reset, etc.
  - **Log dev API**: Provides the log system functions.
  - **Interrupt API**: Provides the interrupt functions.


**Note:** - There is a non-secure `HAL` that focuses on the mailbox operation API for Dual-core topology. For more information about it, please refer to </design_docs/multi-cpu/mailbox_design>`. - The minimal set of `TF-M` `HAL` is sufficient for Secure Partitions by using customized peripheral interfaces. To provide easier portability for the Secure Partitions, a Secure Partition `HAL` is provided in this design too. - The debug mechanisms give the external entity the corresponding right to access the system assets. `TF-M` ensures that the external entity is permitted access to those assets. Currently, `TF-M` only needs the debug authentication. The whole debug mechanism and related `HAL` will be enhanced in the future. Please refer to the Debug authentication settings section for more details.
