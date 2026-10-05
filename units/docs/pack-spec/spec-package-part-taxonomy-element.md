---
id: "spec-package-part-taxonomy-element"
type: "concept"
domain: "pack"
title: "/package/part-taxonomy element"
summary: "Group to list description elements that define part classes and part group names used within a package description. This element is optional."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_part-taxonomy.html"
license: "Apache-2.0"
mode: "V"
---

Group to list description elements that define part classes and part group names used within a package description.
This element is optional.

**Example:**
```
<package>
  ...
  <part-taxonomy>
    ...
  </part-taxonomy>
  ...
</package>
```


 



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| package | element_package |  |  |
| Child Elements | Description | Type | Occurrence |
| element_part-taxonomyDescription "description" | Describes or defines a part class or class-group combination. | PartTaxonomyDescriptionType | 1..* |
