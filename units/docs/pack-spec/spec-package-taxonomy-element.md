---
id: "spec-package-taxonomy-element"
type: "concept"
domain: "pack"
title: "/package/taxonomy element"
summary: "Group to list description elements that define component classes and component group names used within a package description. This element is optional."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_taxonomy.html"
license: "Apache-2.0"
mode: "V"
---

Group to list description elements that define component classes and component group names used within a package description.
This element is optional.

**Example:**
```
<package>
  ...
  <taxonomy>
    ...
  </taxonomy>
  ...
</package>
```


 



  | 
    Parent Element | 
    Element Chain | 
  

  | 
    package | 
    element_package | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    description | 
    Describes or defines a component class or class-group combination. | 
    TaxonomyDescriptionType | 
    1..*  |
