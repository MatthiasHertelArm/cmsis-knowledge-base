---
id: "spec-package-examples-element-package-examples-example-project-environ"
type: "concept"
domain: "pack"
title: "/package/examples element: /package/examples/example/project/environment"
summary: "The environment element describes the name of the environment and the project file to be loaded."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/examples_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html"
license: "Apache-2.0"
mode: "V"
---

The environment element describes the name of the environment and the project file to be loaded.

**Example:**
```
<project>
  <environment name="uv" folder="./ARM" load="ARM/Blinky.uvproj"/>
  <environment name="iar" folder="./IAR" load="IAR/Blinky.ewarm" />
  <environment name="csolution" folder="./CMSIS/" load="CMSIS/Blinky.csolution.yml" />
</project>
```

```
<project>
  <environment name="STCube" folder="./ST" load="base_example.ioc" custom="test">
    <!-- **** ST vendor tools specific elements ***** -->
  </environment>
  <environment name="csolution" folder="./OpenCMSIS" load="base_example.csolution.yml">
    <!-- **** vendor tools specific elements ***** -->
  </environment>
</project>
```


 
  


  | 
    Parent | 
	Chain | 
  

  | 
    project | 
    element_example_project | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    name | 
    Identifier of the development tool (for example: `uv`, `iar`, `csolution`, etc.)
        targeted by the project file specified by the load attribute. | 
    xs:string | 
    required | 
  

  | 
    load | 
    Specifies the project file with extension. A path relative to **folder** attribute of the element
        element_example can be appended. | 
    xs:string | 
    required | 
  

  | 
    folder | 
    Specifies the subdirectory to be copied into the user's project folder relative to **folder** attribute of the element element_example.
	This attribute is used by example descriptions that support multiple tool-chains/IDEs, each stored in a separate folders. Note: for copying eclipse
	projects it is required that the .project file is located in the base directory and all	project files are located in the base directory or in one of the
	subdirectories. In this case even common files are required to be duplicated.
	 | 
    xs:string | 
    optional | 
  

  | 
    any | 
    Any attribute that is available for the specified development tool.

    xs:anyAttribute | 
    0..* | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    any | 
    Any element that is available for the specified development tool.

    xs:anyAttribute | 
    0..* |
