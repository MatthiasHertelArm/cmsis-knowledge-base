---
id: "spec-package-requirements-package-requirements-targets"
type: "concept"
domain: "pack"
title: "/package/requirements: /package/requirements/targets"
summary: "The targets section marks a pack device specific. Multiple targets can be listed to allow usage for several devices or device series. The indented usage is for installers and web pages to show packs only for specific devices."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_requirements_pg.html"
license: "Apache-2.0"
mode: "V"
---

The targets section marks a pack device specific. Multiple targets can be listed to allow usage for several devices or device series.
The indented usage is for installers and web pages to show packs only for specific devices.

It allows also to specify boards and processor cores, as overtime this element may simplify conditions. However, currently it has no impact on the
selection of pack content such as components. Therefore these attributes are experimental.

**Example** targets section:
```
<package xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="PACK.xsd"/>
  ...
  <requirements>
    <targets>
      <target Dvendor="STMicroelectronics:13" Dname="STM32H7*"/>    <!-- supports STM32H7 device series -->
      <target Dvendor="STMicroelectronics:13" Dname="STM32U585"/>   <!-- and supports STM32U585 device -->
    </targets>
  </requirements>
  ...
</package>
```

**/target**


  | 
    Parents | 
    Element Chain | 
  

  | 
    targets | 
    element_targets | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    Dvendor | 
    Specifies the silicon vendor of the device | 
    xs:string | 
    optional | 
  

  | 
    Dname | 
    Specifies the name of the device (wildcards possible) | 
    xs:string | 
    optional | 
  

  | 
    Dcore | 
    Specifies a processor core (experimental) | 
    xs:string | 
    optional | 
  

  | 
    Bvendor | 
    Specifies the board vendor (experimental) | 
    xs:string | 
    optional | 
  

  | 
    Bname | 
    Specifies the board name (experimental) | 
    xs:string | 
    optional | 
  

  | 
    Brevision | 
    Specifies the board revision (experimental) | 
    xs:string | 
    optional |
