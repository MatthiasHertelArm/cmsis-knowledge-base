---
id: "spec-package-requirements-package-requirements-packages"
type: "concept"
domain: "pack"
title: "/package/requirements: /package/requirements/packages"
summary: "/package/requirements: /package/requirements/packages"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_requirements_pg.html"
license: "Apache-2.0"
mode: "V"
---

**Example** packages section:
```
<package xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="PACK.xsd"/>
  ...
  <requirements>
    <packages>
      <package name="STM32F4xx_DFP" vendor="Keil" version="2.8.0:2.8.0"/>
      <package name="CMSIS" vendor="ARM" version="6.1.0:7.0.0-0"/> <!-- restrict to major version 6 -->
    </packages>
  </requirements>
  ...
</package>
```

**/package**


  | 
    Parents | 
    Element Chain | 
  

  | 
    packages | 
    element_packages | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    vendor | 
    specify vendor of the package (e.g. "ARM") | 
    RestrictedString | 
    required | 
  

  | 
    name | 
    Name of the pack | 
    RestrictedString | 
    required | 
  

  | 
    version | 
    Version of the required software pack which can be:
       - Minimum version (higher versions are accepted).
       - Version range specified with _min_version_**:**_max_version_. _min_version_ must be lower or
         equal than _max_version_. For a version range that retains the major version, the _max_version_ is set
         to the next major version with minor, patch and release qualifier set to "0".
       - Fixed version is specified if _min_version_ and _max_version_ are equal.
       - If no version is specified, the latest available installed version is accepted and used.
     | 
    VersionType | 
    optional |
