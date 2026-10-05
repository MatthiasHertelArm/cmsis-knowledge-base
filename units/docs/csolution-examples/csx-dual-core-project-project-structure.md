---
id: "csx-dual-core-project-project-structure"
type: "concept"
domain: "project"
title: "Dual Core project: Project Structure"
summary: "The project is generated using the CMSIS-Toolbox and is defined in csolution format:"
status: "draft"
collection: "csolution-examples"
source: "Open-CMSIS-Pack/csolution-examples@02f71b2:DualCore/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/DualCore/README.md#project-structure"
license: "Apache-2.0"
mode: "V"
---

The project is generated using the [CMSIS-Toolbox](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview) and is defined in [`csolution`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format) format:

- [`HelloWorld.csolution.yml`](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/DualCore/./HelloWorld.csolution.yml) lists the required packs and defines the hardware target, build types, compiler, and target set that groups both core images and configures the debugger.
- [`./cm0plus/HelloWorld_cm0plus.cproject.yml`](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/DualCore/./cm0plus/HelloWorld_cm0plus.cproject.yml) defines the source files and the software components for the **Cortex-M0+** core.
- [`./cm4/HelloWorld_cm4.cproject.yml`](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/DualCore/./cm4/HelloWorld_cm4.cproject.yml) defines the source files and the software components for the **Cortex-M4** core.
