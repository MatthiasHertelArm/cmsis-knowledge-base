---
id: "spec-package-components-element-package-extensions"
type: "concept"
domain: "pack"
title: "/package/components element: /package/.../extensions"
summary: "The group extensions can appear in various Pack elements. This group is the frame for defining individual extensions."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

The group **extensions** can appear in various Pack elements. This group is the frame for defining individual extensions.

**Example:**
```
<package>
  ...
  <components>
    <component Cclass="Device" Cgroup="Startup" Cversion="3.1.1" >
      <extensions>
        ...
      </extensions>
    </component>
  </components>
  ...
</package>
```


 



  | 
    Parents | 
    Element Chain | 
  

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
    extension | 
    Frame for the individual extension of a component.
    group | 
    1..* |
