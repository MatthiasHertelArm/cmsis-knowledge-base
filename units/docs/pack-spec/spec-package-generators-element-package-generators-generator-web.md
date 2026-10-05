---
id: "spec-package-generators-element-package-generators-generator-web"
type: "concept"
domain: "pack"
title: "/package/generators element: /package/generators/generator/web"
summary: "This element contains information about the web generation application."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/generators_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element contains information about the web generation application.

**Example:**
```
<web url="http://mygen.com/mygen">
  <argument switch="device">$D</argument>
  <argument switch="gpdsc">$P/RTE/MyGen/myGen.gpdsc</argument>
</web>
```

 



| Parent | Chain |  |  |
|---|---|---|---|
| generator | element_generator |  |  |
| Attributes | Description | Type | Use |
| url | Specifies the URL of the web service. URL | required |  |
| Child Elements | Description | Type | Occurrence |
| argument | Arguments passed along to the web service. | GeneratorCommandArgumentType | 0..* |
