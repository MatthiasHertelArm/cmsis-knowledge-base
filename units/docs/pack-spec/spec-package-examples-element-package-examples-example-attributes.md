---
id: "spec-package-examples-element-package-examples-example-attributes"
type: "concept"
domain: "pack"
title: "/package/examples element: /package/examples/example/attributes"
summary: "/package/examples element: /package/examples/example/attributes"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/examples_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html"
license: "Apache-2.0"
mode: "V"
---

**Example:**
```
<example>
  <attributes>
    <category>Example Project</category>
    <category>For a specific board</category>
	...
    <component Cclass="CMSIS" Cgroup="Core"/>
    <component Cclass="Device" Cgroup="Startup"/>
	...
	<keyword>Blinky</keyword>
	<keyword>Getting Started</keyword>
  </attributes>
</example>
```


 



| Parent | Chain |  |  |
|---|---|---|---|
| example | element_example |  |  |
| Child Elements | Description | Type | Occurrence |
| category | Free form string defining an example category. A category can be used to filter examples in an example browser. | xs:string | 0..* |
| component | Group for defining the components used in the example. | ComponentCategoryType | 0..* |
| keyword | Free form string defining a keyword that relates to the example. A keyword can be used to search for examples. | xs:string | 0..* |
