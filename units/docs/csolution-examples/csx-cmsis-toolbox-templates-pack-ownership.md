---
id: "csx-cmsis-toolbox-templates-pack-ownership"
type: "concept"
domain: "project"
title: "CMSIS-Toolbox Templates: Pack Ownership"
summary: "Pack declarations define which software packs are available within solution, project, or layer scope. Avoid duplicate or conflicting pack requirements so projects and layers remain reusable."
status: "draft"
collection: "csolution-examples"
source: "Open-CMSIS-Pack/csolution-examples@02f71b2:Templates/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/Templates/README.md#pack-ownership"
license: "Apache-2.0"
mode: "V"
---

Pack declarations define which software packs are available within solution, project, or layer scope. Avoid duplicate or conflicting pack requirements so projects and layers remain reusable.

- `*.csolution.yml`: specify hardware packs and packs shared by all projects.
- `*.cproject.yml`: specify packs required by that project.
- `*.clayer.yml`: specify packs required by the reusable layer so they are available to every project that uses it.
