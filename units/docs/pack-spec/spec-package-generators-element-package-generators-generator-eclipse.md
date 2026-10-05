---
id: "spec-package-generators-element-package-generators-generator-eclipse"
type: "concept"
domain: "pack"
title: "/package/generators element: /package/generators/generator/eclipse"
summary: "This element contains information about the Eclipse based generation tool."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/generators_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element contains information about the Eclipse based generation tool.

**Example:**
```
<eclipse plugin="com.mygen.plugin" class="com.mygen.plugin.generator.launcher" method="launch" >
  <argument>$D</argument>
  <argument>$P/RTE/MyGen/myGen.gpdsc</argument>
</eclipse>
```

 



  | 
    Parent | 
    Chain | 
  

  | 
    generator | 
    element_generator | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    plugin | 
    Name of the plugin. | 
    xs:string | 
    required | 
  

  | 
    class | 
    Plugin's class name. | 
    xs:string | 
    required | 
  

  | 
    method | 
    Method used to launch the plugin. | 
    xs:string | 
    required | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    argument | 
    Arguments passed to the plugin. | 
    GeneratorCommandArgumentType | 
    1..* |
