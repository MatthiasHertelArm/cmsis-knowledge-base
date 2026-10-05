---
id: "csx-simple-trustzone-application-project-structure"
type: "concept"
domain: "project"
title: "Simple TrustZone Application: Project Structure"
summary: "The project is generated using the CMSIS-Toolbox and is defined in csolution format:"
status: "draft"
collection: "csolution-examples"
source: "Open-CMSIS-Pack/csolution-examples@02f71b2:SimpleTrustZone/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/SimpleTrustZone/README.md#project-structure"
license: "Apache-2.0"
mode: "V"
---

The project is generated using the [CMSIS-Toolbox](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview) and is defined in [`csolution`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format) format:

- [`SimpleTZ.csolution.yml`](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/SimpleTrustZone/./SimpleTZ.csolution.yml) lists the required packs and defines the hardware target, build types, supported compilers, and target sets.
- [`CM33_s.cproject.yml`](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/SimpleTrustZone/./CM33_s/CM33_s.cproject.yml) defines the source files and the software components used for the secure part.
- [`CM33_ns.cproject.yml`](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/SimpleTrustZone/./CM33_ns/CM33_ns.cproject.yml) defines the source files and the software components used for the non-secure part.
