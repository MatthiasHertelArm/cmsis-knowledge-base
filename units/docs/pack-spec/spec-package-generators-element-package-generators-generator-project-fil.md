---
id: "spec-package-generators-element-package-generators-generator-project-fil"
type: "concept"
domain: "pack"
title: "/package/generators element: /package/generators/generator/project_files"
summary: "The group project_files specifies all files that are required for the project setup. Only one such group can exist."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/generators_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html"
license: "Apache-2.0"
mode: "V"
---

The group **project_files** specifies all files that are required for the project setup. Only one such group can exist.

**Example**
```
  <generators>
    <generator id="STM32CubeMX" Gvendor="STMicroelectronics" Gtool="STM32CubeMX" Gversion="4.10.0">
      <description>STM32CubeMX Environment</description>
      <select Dname="STM32F746NGHx" Dvendor="STMicroelectronics:13"/>
      <exe>
        <command host = "win">MDK/CubeMX/STM32CubeMXLauncher.exe</command>
        <command host = "linux">MDK/CubeMX/STM32CubeMXLauncher</command>
        <argument>$P/RTE/MyGen/myGen.gpdsc</argument>
        <argument>$D.ioc</argument>
      </exe>
      <workingDir>$P/RTE/Device/STM32F746NGHx</workingDir>
      <project_files>
        <file category="source" name="STCubeGenerated/Src/main.c" />
        <file category="header" name="STCubeGenerated/Inc/stm32f7xx_it.h"/>
        <file category="source" name="STCubeGenerated/Src/stm32f7xx_it.c"/>
      </project_files>
    </generator>
  </generators>
```


 



| Parent | Element Chain |  |  |
|---|---|---|---|
| generator | element_generator |  |  |
| Child Elements | Description | Type | Occurrence |
| file | Frame for files created by the generator and used in a project. group | 0..1 |  |
