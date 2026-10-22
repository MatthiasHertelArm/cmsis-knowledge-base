---
id: "tbx-reference-applications-introduction"
type: "concept"
domain: "project"
title: "Reference Applications: Introduction"
summary: "The CMSIS-Pack format supports different types of project examples:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/ReferenceApplications.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/#introduction"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Pack format supports different types of project examples:

- *Template Projects* are [stub projects](https://github.com/Open-CMSIS-Pack/csolution-examples/tree/main/Templates) that help getting started. Some software packs may contain device-specific templates.
- *Examples* are created for a specific hardware or evaluation board. These are typically complete projects that directly interface with board and device peripherals.
- *Reference Applications* use defined interfaces (APIs) and are therefore target agnostic. These project examples show the usage of middleware components and require additional [software layers](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/build-overview.md#software-layers) with API drivers for an evaluation board or an FVP simulation model.

The following sections explain the usage, structure, and creation of *Reference Applications* that can target different evaluation boards and FVP simulation models.

Refer to [Pack Creation: Project Examples](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/pack-tools.md#project-examples) for information on how to publish project examples as part of software packs.
