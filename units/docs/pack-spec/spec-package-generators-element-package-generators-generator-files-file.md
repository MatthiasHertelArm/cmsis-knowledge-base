---
id: "spec-package-generators-element-package-generators-generator-files-file"
type: "concept"
domain: "pack"
title: "/package/generators element: /package/generators/generator/files/file"
summary: "This element contains information about files used by a generator."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/generators_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element contains information about files used by a generator.

**Example**
```
<generators>
  <generator id="MyGenerator">
    <files>
      <file category="generator" name="Main.c"/>
      <file category="you_name_it" name="database/connection.odbc" version="1.2.3"/>
      ...
    <files>
  </generator>
</generators>
```


 



| Parent | Element Chain |  |  |
|---|---|---|---|
| files | element_gen_files |  |  |
| Attributes | Description | Type | Use |
| condition | Reference using the name of the respective condition specified in the conditions section of this package (element_conditions). If the condition resolves to `false`, then the element will be ignored and treated as if not present. | xs:string | optional |
| category | Describes the file type (for example: `doc`, `header`, `library`). You can use predefined values as listed in the table File Categories, however, this is not mandatory. | xs:string | required |
| name | Can consist of the path (relative to the Pack base directory) and the file name with extension. | xs:string | required |
| version | File-specific version information. The version format is described in Version Type. | VersionType | optional |
