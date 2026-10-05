---
id: "spec-package-examples-element-package-examples-example-attributes-comp"
type: "concept"
domain: "pack"
title: "/package/examples element: /package/examples/example/attributes/component"
summary: "The component element specifies the Cclass to which the example belongs. This can be used to list all related components within an example."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/examples_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html"
license: "Apache-2.0"
mode: "V"
---

The component element specifies the Cclass to which the example belongs. 
This can be used to list all related components within an example.

**Example:**
```
<attributes>
  ...
  <component Cclass="CMSIS" Cgroup="Core"/>
  <component Cclass="Device" Cgroup="Startup"/>
  ...
</attributes>
```


 



  | 
    Parent | 
	Chain | 
  

  | 
    attribute | 
	element_example_attributes | 
  

  | 
    Attribute | 
    Description | 
    Type | 
    Use | 
  

  | 
    Cclass | 
    Free form string defining an example class. Predefined values can be used as listed in the table Component Classes. | 
    CclassType | 
    required | 
  

  | 
    Cgroup | 
    Free form string defining an example group. Predefined values can be used as listed in the table Component Groups. | 
    CgroupType | 
    optional | 
  

  | 
    Csub | 
    Free form string defining an example subgroup. The type is described in Component Subgroups. | 
    CsubType | 
    optional | 
  

  | 
    Cversion | 
    Free form string defining an example version.  The version format is described in Version Type. | 
    VersionType | 
    optional | 
  

  | 
    Cvendor | 
    Free form string defining the vendor of the example. | 
    xs:string | 
    optional |
