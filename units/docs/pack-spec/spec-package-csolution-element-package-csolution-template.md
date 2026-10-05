---
id: "spec-package-csolution-element-package-csolution-template"
type: "concept"
domain: "pack"
title: "/package/csolution element: /package/csolution/template"
summary: "A template section provide one or more project templates for starting a new csolution project in an IDE. If a condition is specified, the template is only available when the condition resolves to true."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/csolution_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_csolution_pg.html"
license: "Apache-2.0"
mode: "V"
---

A template section provide one or more project templates for starting a new *csolution project* in an IDE. If a condition is specified, the template is only available when the condition resolves to true.



| Parent | Chain |  |  |
|---|---|---|---|
| csolution | element_csolution |  |  |
| Attributes | Description | Type | Use |
| name | Name of the template | xs:string | required |
| path | Path to the directory that contains the template. | xs:string | required |
| file | Name of the `*.csolution.yml` file (optional with relative path to the directory specified with path). | xs:string | required |
| copy-to | Path that used to copy the template into the *csolution project* (default is attribute path). | xs:string | optional |
| condition | Enter the **id** of a condition. The template is available and will be listed only when the filter condition is true (no component dependencies are evaluated). | xs:string | optional |
| Child Elements | Description | Type | Occurrence |
| description | Briefly documents the purpose and scope of the template (maximum 256 characters, recommended 128 characters). | BriefDescType | 1 |



**Example:**
```
<csolution> 
  <template name="Basic csolution project" path="templates/blank" file="Blank.csolution.yml" copy-to="Blank" condition="STM32H7S-Series">
    <description>Create a basic project with empty main function</description>
  </template>
  <template name="TrustZone csolution project" path="templates/trustzone" file="TrustZone.csolution.yml" condition="STM32H7S-Series">
    <description>Create a basic solution with secure and non-secure projects</description>
  </template>
</csolution>
```
