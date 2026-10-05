---
id: "spec-package-components-element-package-files"
type: "concept"
domain: "pack"
title: "/package/components element: /package/.../files"
summary: "The group files can appear in various Pack elements. This group is the frame for defining individual file properties."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

The group **files** can appear in various Pack elements. This group is the frame for defining individual file properties.

**Example:**
```
<package>
  ...
  <apis>
    <api Cclass="Device" Cgroup="Driver UART" exclusive="0">
      <files>
        ...
      </files>
    </api>
  </apis>
  ...
  <components>
    <component Cclass="Device" Cgroup="Startup" Cversion="3.1.1" >
      <files>
        ...
      </files>
    </component>
  </components>
  ...
</package>
```


 



  | 
    Parents | 
    Element Chain | 
  

  | 
    api | 
    /package/apis/api | 
  

  | 
    component | 
    /package/components/component | 
  

  | 
    component | 
    /package/components/bundle/component | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    file | 
    Frame for the individual file of a component.
    group | 
    1..* |
