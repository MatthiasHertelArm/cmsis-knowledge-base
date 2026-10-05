---
id: "spec-package-examples-element-package-examples-example-project"
type: "concept"
domain: "pack"
title: "/package/examples element: /package/examples/example/project"
summary: "Different development tools store project information in tool specific file formats. A single example may include project files for multiple tools or environments."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/examples_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html"
license: "Apache-2.0"
mode: "V"
---

Different development tools store project information in tool specific file formats. A single example
may include project files for multiple tools or environments.
Therefore the project element is a sequence of one or more **environment** elements that describe the name of the environment and the project file to be loaded by the respective development tool.

**Example:**
```
<project>
  <environment ... />
  <environment ... />
</project>
```


 



  | 
    Parent | 
	Chain | 
  

  | 
    example | 
	element_example | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    environment | 
	Specifies the environment and project file with extension. | 
	xs:complexType | 
	1..* |
