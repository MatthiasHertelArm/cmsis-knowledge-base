---
id: "spec-package-generators-element-package-generators-generator-gpdsc"
type: "concept"
domain: "pack"
title: "/package/generators element: /package/generators/generator/gpdsc"
summary: "Path and name of the GPDSC that the generator creates and updates. The path is either absolute or relative to the working directory."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/generators_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html"
license: "Apache-2.0"
mode: "V"
---

Path and name of the GPDSC that the generator creates and updates. 
The path is either absolute or relative to the working directory. 
If no explicit gpdsc file is provided, then a gpdsc file named after the project with extension gpdsc in the working directory is assumed (\
.gpdsc).
Only one such element can exist in \`<generator>`.

**Example:**
```
  <generators>
    <generator id="MyGen">
      <gpdsc name="$P/RTE/MyGen/myGen.gpdsc"/>
    </generator>
  </generators>
```

 



| Parent | Chain |  |  |
|---|---|---|---|
| generator | element_generator |  |  |
| Attributes | Description | Type | Use |
| name | Path and name of the GPDSC that the generator creates and updates. | xs:string | required |
