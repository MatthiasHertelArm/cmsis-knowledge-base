---
id: "spec-package-csolution-element-package-csolution-clayer"
type: "concept"
domain: "pack"
title: "/package/csolution element: /package/csolution/clayer"
summary: "A clayer section provides the information for accessing a software layer that is stored in a pack. If a condition is specified, the clayer is only listed when the condition resolves to true."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/csolution_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_csolution_pg.html"
license: "Apache-2.0"
mode: "V"
---

A clayer section provides the information for accessing a software layer that is stored in a pack. If a condition is specified, the clayer is only listed when the condition resolves to true.



| Parent | Chain |  |  |
|---|---|---|---|
| csolution | element_csolution |  |  |
| Attributes | Description | Type | Use |
| type | Type of the clayer | xs:string | required |
| path | Path to the directory that contains the software layer. | xs:string | required |
| file | Name of the `*.clayer.yml` file (optional with relative path to the directory specified with path). | xs:string | required |
| copy-to | Path that used to copy the software layer into the *csolution project* (default is attribute path). | xs:string | optional |
| condition | Enter the **id** of a condition. The clayer is available and will be listed only when the filter condition is true (no component dependencies are evaluated). | xs:string | optional |



**Example:**
```
<csolution> 
  <clayer type="Board" path="layers/board/FRDM-MCXA153-MW" file="Board.clayer.yml" copy-to="board/FRDM-MCXA153" condition="FRDM-MCXA153-Board" />
  <clayer type="Board" path="board/FRDM-MCXA153" file="Board.clayer.yml" condition="FRDM-MCXA153-Board"/>
</csolution>
```
