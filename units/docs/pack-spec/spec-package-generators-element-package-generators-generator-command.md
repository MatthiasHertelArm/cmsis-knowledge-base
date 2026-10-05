---
id: "spec-package-generators-element-package-generators-generator-command"
type: "concept"
domain: "pack"
title: "/package/generators element: /package/generators/generator/.../command"
summary: "This element describes a single command line for launching the generator. Arguments should be passed along with an argument."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/generators_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element describes a single command line for launching the generator. Arguments should be passed along with an
argument.

**Example**
```
<exe>
  <command host = "win">MyGen.bat</command>
  <command host = "linux">MyGen.script</command>
  <argument>$P/RTE/MyGen/myGen.gpdsc</argument>
  <argument host="linux" switch="--device=">$D</argument>
  <argument host="win"   switch="/device=">$D</argument>
</exe>
```


 



  | 
    Parent | 
    Element Chain | 
  

  | 
    exe | 
    element_gen_exe | 
  

  | 
    Current | 
    Description | 
    Type | 
  

  | 
    command | 
    generator command line | 
    xs:string | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    host | 
    Specifies the host operating system. Possible values are `all,` `win,` `linux,` `mac,` `other.` Only available
        with element exe. | 
    xs:string | 
    optional |
