---
id: "spec-package-apis-element-package-apis-api"
type: "concept"
domain: "pack"
title: "/package/apis element: /package/apis/api"
summary: "Application Programming Interfaces (apis) are C/C++ interface specifications that allow components to inter-work by either implementing or using a set of functions, data types, and definitions. This element is mandatory and can exist multiple times."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/apis_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_apis_pg.html"
license: "Apache-2.0"
mode: "V"
---

Application Programming Interfaces (apis) are C/C++ interface specifications that allow components to inter-work
by either implementing or using a set of functions, data types, and definitions. This element is mandatory and can exist multiple times.

**Example:**
```
<apis>
  <api Cclass="Device" Cgroup="Driver UART" exclusive="0">
    <description>UART Driver API for the Cortex-M processor based devices</description>
    <files>
      <file category="doc" name="Driver/Doc/UART/html/index.html"/>
      <file category="header" name="Driver/Include/Driver_UART.h"/>
    </files>
  </api>
  <api Cclass="Device" Cgroup="Driver SPI" exclusive="0">
    <description>SPI Driver API for the Cortex-M processor based devices</description>
    <files>
      <file category="doc" name="Driver/Doc/SPI/html/index.html"/>
      <file category="header" name="Driver/Include/Driver_SPI.h"/>
    </files>
  </api>
  ...
</apis>
```


 



  | 
    Parent Element | 
    Element Chain | 
  

  | 
    apis | 
    /package/apis | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    Cclass | 
    Defines the component class to which this component belongs. This is a mandatory part of the component ID.
      Predefined values can be used as listed in the table Component Classes. | 
    CclassType | 
    required | 
  

  | 
    Cgroup | 
    Defines the component group to which this component belongs. This is a mandatory part of the component ID.
      Predefined values can be used as listed in the table Component Groups. | 
    CgroupType | 
    required | 
  

  | 
    exclusive | 
    Makes the selection of a component implementing the API exclusive. If set to `0`, then multiple components
      implementing the API can be selected concurrrently. Default is `1`. | 
    xs:boolean | 
    optional | 
  

  | 
    condition | 
    Enter the identifier (attribute ****id**)** of a condition. The element is used if the condition resolves to `true`.
      If the condition resolves to `false`, then the element will be ignored.
      For example, an API might be specific for a certain toolchain or processor instruction set. | 
    xs:string | 
    optional | 
  

  | 
    Capiversion | 
    Version of the api. Is a mandatory part of the api ID.  The version format is described in Version Type.
     | 
    VersionType | 
    optional | 
  

  | 
    licenseSet | 
    Reference to the licenseSet with the given identifier `ID` listed in the licenseSets section of the package description.
      A licenseSet describes one or more license files which in this case govern the api. | 
    xs:string | 
    optional | 
  

  | 
    changelog | 
    
      Reference to the `changelog` with the given identifier `ID` specified in the changelogs section of the package description.
      A changelog references a text file in the pack with a path relative to the pdsc containing changelog information for the api.
      The content of the referenced changelog file is not required to be exclusively used for a single api. | 
    xs:string | 
    optional | 
  


  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    description | 
    Brief summary about the purpose and scope of an API (maximum 256 characters, recommended 128 characters). | 
    BriefDescType | 
    0..1 | 
  

  | 
    files | 
    Grouping element for all file descriptions that are part of this API. At least one file child element is required. | 
    group | 
    1 |
