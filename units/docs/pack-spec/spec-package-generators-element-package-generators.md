---
id: "spec-package-generators-element-package-generators"
type: "concept"
domain: "pack"
title: "/package/generators element: /package/generators"
summary: "Grouping element for generators. Only one such group can exist in a Pack."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/generators_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html"
license: "Apache-2.0"
mode: "V"
---

Grouping element for **generators.** Only one such group can exist in a Pack.



  | 
    Parent | 
    Chain | 
  

  | 
    package | 
    /package | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    generator | 
    Description of the generator and the related files | 
    GeneratorType | 
    1..*  | 
  

 

 The following variables can be used in the elements `\<command>,` `\<workingDir>,` `\<argument>,` `\<gpdsc>:`



  | 
    Variable | 
    Description | 
  

  | 
    $P | 
    PATH to current project | 
  

  | 
    \#P | 
    PATH and name of the current project | 
  

  | 
    $S | 
    PATH to Pack folder containing the Device description used by the current project | 
  

  | 
    $D | 
    Name of the device configured in the current project | 
  

  | 
    $B | 
    Name of the board configured in the current project | 
  

  | 
    $G | 
    Absolute PATH to the generator input file describing the project and component context. 
        Note $G is only available in the `\<command>` and `\<argument>` elements |
