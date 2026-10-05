---
id: "spec-package-examples-element"
type: "concept"
domain: "pack"
title: "/package/examples element"
summary: "The element element_example describes fully defined examples contained in the Pack. An example lists the files that belong to an example."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/examples_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html"
license: "Apache-2.0"
mode: "V"
---

The element element_example describes fully defined examples contained in the Pack.
An example lists the files that belong to an example. The example itself and each individual file may
refer to a condition that must resolve to true; if it is false the example or file will be ignored.
The board element is used to reference to one or more board descriptions using the board vendor and name an example is targeted for.
Each example may optionally specify attributes e.g. providing a short list of the most significant components using Class (Cclass=), Group (Cgroup=), Subgroup (Csub) and a Version (Cversion=).

**Example**
```
  <examples>
    <example name="Blinky" folder="Boards/MCBSTM32F200/Blinky" doc="Abstract.txt" version="1.0">
      <description>This is a basic example demonstrating the development flow and letting the LED on the board blink</description>
      <board vendor="STMicroelectronics" name="32F429IDISCOVERY"/>
      <project>
        <environment name="uv"  folder="./ARM" load="ARM/Blinky.uvproj"/>
        <environment name="iar" folder="./IAR" load="IAR/Blinky.ewarm" />
      </project>
      <attributes>
        <component Cclass="CMSIS" Cgroup="Core"/>
        <component Cclass="Device" Cgroup="Startup"/>
        <keyword>Blinky</keyword>
        <keyword>Getting Started</keyword>
      </attributes>
    </example>
  </examples>  

```
