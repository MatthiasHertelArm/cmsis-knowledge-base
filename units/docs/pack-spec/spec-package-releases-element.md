---
id: "spec-package-releases-element"
type: "concept"
domain: "pack"
title: "/package/releases element"
summary: "Contains the release history of the Pack. This element is mandatory. No more than one such group can exist in a Pack. It contains the full release history of the Pack."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html"
license: "Apache-2.0"
mode: "V"
---

Contains the release history of the Pack. This element is mandatory. No more than one such group can exist in a Pack.
It contains the full release history of the Pack.

**Example:**
```
<package>
  ...
  <releases>
    ...
  </releases>
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
    Child Element | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    release | 
    Contains the version number of the release with some brief information about the main changes in that specific release. | 
    xs:string  | 
    1..*  |
