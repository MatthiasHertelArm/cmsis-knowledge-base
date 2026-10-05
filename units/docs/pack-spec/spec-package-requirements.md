---
id: "spec-package-requirements"
type: "concept"
domain: "pack"
title: "/package/requirements"
summary: "There are the following requirement types: - The \\<packages\\> section lists CMSIS Packs that have been used to configure the project. This includes the specification of a version range to ensure compatibility."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_requirements_pg.html"
license: "Apache-2.0"
mode: "V"
---

There are the following requirement types:
 - The `\<packages\>` section lists CMSIS Packs that have been used to configure the project. This includes the specification
   of a `version` range to ensure compatibility. If no version is provided, the latest installed version is used. If not yet
   installed, the latest available version will be installed before resolving the configuration.
 - The `\<compilers\>` section specifies the toolchains that are supported by this example. The required compiler version is
   specified using the `version` element. If no compiler is specified, it is assumed that any toolchain will work.
 - The `\<languages\>` section allows to specify requirements regarding the programming language, for example C99 standard.
   If no language requirements are set, ANSI C is assumed.
 - The `\<targets\>` section allows to specify requirements regarding the device or device series.
   If no target requirements are set, the pack is listed as generic that works with any device, board, or processor.

**Example** requirements section:
```
<package xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="PACK.xsd"/>
  ...
  <requirements>
    <packages>
      <package name="STM32F4xx_DFP" vendor="Keil" version="2.8.0:2.8.0"/>
    </packages>
    <compilers>
      <compiler name="ARMCC" version="5.0.0:6.0.0-0"/>
    </compilers>
    <languages>
      <language name="C" version="99"/>
    </languages>
  </requirements>
  ...
</package>
```

**/requirements**


  | 
    Parents | 
    Element Chain | 
  

  | 
    package | 
    element_package | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    packages | 
    List of software packs required for the project to build. | 
    PackagesType | 
    <0..1> | 
  

  | 
    compilers | 
    List of compilers required for the project to build. Support for all compilers is assumed when not specified. | 
    CompilersType | 
    <0..1> | 
  

  | 
    languages | 
    List of language standards required for the project to build. Assuming ANSI C if not set. | 
    LanguagesType | 
    <0..1> | 
  

  | 
    targets | 
    Restrict a software pack to a list of devices, boards, or processor cores that are supported. | 
    TargetsType | 
    <0..1> |
