---
id: "spec-package-element"
type: "concept"
domain: "pack"
title: "/package element"
summary: "The basic package information captures the package vendor, the package name, a brief description of the package, and the schema version. Additional elements support the logistics of handling packages. The url (https required) specifies the origin of the description."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html"
license: "Apache-2.0"
mode: "V"
---

The basic package information captures the package vendor, the package name, a brief description of the package, and the schema version.
Additional elements support the logistics of handling packages. The url (https required) specifies the origin of the description. It may
be left empty if the pack will not be uploaded onto a web server. A license file might point to license agreements. A list of keywords
assists searching for packages. An optional environments element can be used to list environment-specific information.

**Example:**
```
<package schemaVersion="1.4" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="PACK.xsd">
  <vendor>ExampleVendor</vendor>
  <name>STM32F2xx_DFP</name>                                                       <!-- name of package -->
  <description>Device Family Package for STMicroelectronics STM32F2 Family of Arm Cortex-M3 based Microcontroller</description>
  <url></url>
  <supportContact>http://www.arm.com/support</supportContact>
  <license>./END_USER_LICENCE_AGREEMENT.rtf</license>
  <releases>
    <release version="1.0.0" date="2014-12-14">
      First Release version of STM32F2 Device Family Pack.
    </release>
    <release version="0.9.0">
      Beta version of STM32F2 Device Family Pack.
    </release>
  </releases>

  <keywords>                                                                  <!-- keywords for indexing -->
    <keyword>ST</keyword>
    <keyword>Device Support</keyword>
    <keyword>Device Family Package ST</keyword>
    <keyword>STM32F2</keyword>
    <keyword>STM32F2xx</keyword>
  </keywords>

  <environments>
    <environment name="tool-x">                                               <!-- tool-x specific information for the whole package -->
      ...
    </environment>
    <environment name="tool-y">                                               <!-- tool-y specific information for the whole package -->
      ...
    </environment>
  </environments>

  <taxonomy>                                                                  <!-- class and group descriptions -->
    <description Cclass="Board Support">
      Generic Interfaces and Templates for Evaluation and Development Boards
    </description>
  </taxonomy>
  ...
</package>
```
