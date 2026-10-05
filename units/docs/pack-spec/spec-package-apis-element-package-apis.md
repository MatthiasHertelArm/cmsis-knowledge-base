---
id: "spec-package-apis-element-package-apis"
type: "concept"
domain: "pack"
title: "/package/apis element: /package/apis"
summary: "This element is a grouping element for all application programming interfaces included in the software pack. The element itself is optional. Only one such section can exist in a package."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/apis_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_apis_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element is a grouping element for all application programming interfaces included in the software pack.
The element itself is optional. Only one such section can exist in a package.

**Example:**
```
<package>
  <apis>
    ...
  </apis>
</package>
```


 



  | 
    Parents  | 
    Element Chain | 
      | 
      | 
  

  | 
    package | 
    /package | 
      | 
      | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    api | 
    Named specification of an API containing a brief description, C/C++ header files and documentation | 
    ApiType | 
    1..* |
