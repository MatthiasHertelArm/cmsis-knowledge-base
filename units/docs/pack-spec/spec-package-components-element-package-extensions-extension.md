---
id: "spec-package-components-element-package-extensions-extension"
type: "concept"
domain: "pack"
title: "/package/components element: /package/.../extensions/extension"
summary: "The element extension is the mechanism to attach additional attributes to the software. This attribute is a key/value pair that is fully defined by the component designer. The possible values are not imposed by this specification."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

The element **extension** is the mechanism to attach additional attributes to the software.
This attribute is a key/value pair that is fully defined by the component designer.
The possible values are not imposed by this specification.


**Example:**
```
<package>
  ...
  <components>
    <component Cclass="Device" Cgroup="Startup" Cversion="3.1.1" >
      <extensions>
        <extension key="auxiliary" value="true"/>
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
    extensions | 
    /package/components/component/extensions | 
  

  | 
    extensions | 
    /package/components/bundle/component/extensions | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    key | 
    key identifying this extension. This must be unique per component. | 
    xs:string | 
    required | 
  

  | 
    value | 
    value associated to the key. | 
    xs:string | 
    optional |
