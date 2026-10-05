---
id: "spec-package-csolution-element-package-csolution"
type: "concept"
domain: "pack"
title: "/package/csolution element: /package/csolution"
summary: "Grouping element for csolution. No more than one such group can exist in a package description."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/csolution_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_csolution_pg.html"
license: "Apache-2.0"
mode: "V"
---

Grouping element for csolution. No more than one such group can exist in a package description.



| Parent | Chain |  |  |
|---|---|---|---|
| package | /package |  |  |
| Child Elements | Description | Type | Occurrence |
| clayer | Description of a clayer; a software layer collects source files and software components along with configuration files for re-use in different projects. | ClayerType | 0..* |
| template | Description of project templates that are used in an IDE to start new *csolution projects*. | ClayerType | 0..* |



**Example:**

```
<csolution> 
  <template name="Basic csolution project" path="templates/blank" file="Blank.csolution.yml" copy-to="Blank" condition="STM32H7S-Series">
    <description>Create a basic project with empty main function</description>
  </template>
  <clayer type="Board" path="layers/board/FRDM-MCXA153-MW" file="Board.clayer.yml" copy-to="board/FRDM-MCXA153" condition="FRDM-MCXA153-Board" />
</csolution>
```
