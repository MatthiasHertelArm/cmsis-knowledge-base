---
id: "spec-package-generators-element-package-generators-generator-files"
type: "concept"
domain: "pack"
title: "/package/generators element: /package/generators/generator/files"
summary: "The group files specifies files that are required by the generator tool. Only one such group can exist."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/generators_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html"
license: "Apache-2.0"
mode: "V"
---

The group **files** specifies files that are required by the generator tool. Only one such group can exist.

**Example**
```
<generators>
  <generator id="MyGenerator">
    <files>
      ...
    <files>
  </generator>
</generators>
```


 



| Parent | Element Chain |  |  |
|---|---|---|---|
| generator | element_generator |  |  |
| Child Elements | Description | Type | Occurrence |
| file | Frame for files used by the generator. group | 0..1 |  |
