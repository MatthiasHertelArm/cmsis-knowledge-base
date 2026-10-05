---
id: "spec-package-components-element-package-environments"
type: "concept"
domain: "pack"
title: "/package/components element: /package/.../environments"
summary: "The group environments can appear in component element and in package element. This group is the frame for defining individual environment."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

The group **environments** can appear in component element and in package element. This group is the frame for defining individual environment.

**Example** #1:
```
<package>
  ...
  <components>
    <component Cclass="Device" Cgroup="Startup" Cversion="3.1.1" >
      <environments>
        ...
      </environments>
    </component>
  </components>
  ...
</package>
```

**Example** #2: describing "tool-x" and "tool-y" custom information applicable to the whole pack:
```
<package>
  <environments>
    <environment name="tool-x">
      ...
    </environment>
    <environment name="tool-y">
      ...
    </environment>
  </environments>
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
    package | 
    /package | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    environment | 
    Specify tool options.
    EnvironmentType | 
    1..* |
