---
id: "spec-package-requirements-package-requirements-languages"
type: "concept"
domain: "pack"
title: "/package/requirements: /package/requirements/languages"
summary: "/package/requirements: /package/requirements/languages"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_requirements_pg.html"
license: "Apache-2.0"
mode: "V"
---

**Example** languages section:
```
<package xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="PACK.xsd"/>
  ...
  <requirements>
    <languages>
      <language name="C" version="99"/>
    <languages>
  </requirements>
  ...
</package>
```

**/language**


| Parents | Element Chain |  |  |
|---|---|---|---|
| requirements | element_requirements |  |  |
| Attributes | Description | Type | Use |
| name | Name of the programming language (i.e. "C", "C++") | xs:string | required |
| version | Version of the language standard (i.e. 90, 99, etc.). The setting will be reflected in the compiler commandline. | xs:string | required |
