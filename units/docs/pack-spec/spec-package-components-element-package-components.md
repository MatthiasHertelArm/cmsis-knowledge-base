---
id: "spec-package-components-element-package-components"
type: "concept"
domain: "pack"
title: "/package/components element: /package/components"
summary: "Grouping element containing a choice of at least one bundle or component. No more than one element components can exist in a Pack."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

Grouping element containing a choice of at least one bundle or component. No more than one element _components_ can exist in a Pack.



  | 
    Parent | 
    Element Chain | 
  

  | 
    package | 
    /package | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    generator | 
    Specifies the generator ID of the generator that has been used to generate all components within this section. | 
    xs:string | 
    optional | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    bundle | 
    Grouping element for a collection of inter-operable components belonging to the same Cclass.
      The components section must not be empty. At least one bundle or component is required. | 
    ComponentType | 
    0..* | 
  

  | 
    component | 
    component description element. The components section must not be empty. At least one component or bundle is required. | 
    ComponentType | 
    0..* |
