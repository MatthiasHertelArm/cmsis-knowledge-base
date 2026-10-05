---
id: "spec-package-parts-element"
type: "concept"
domain: "pack"
title: "/package/parts element"
summary: "The element /package/parts describes a set of hardware parts (devices other than the MCUs) contained in a Part pack (like the element \\<components> is used to describe software components, the element \\ here defined is used to describe hardware components)."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/parts_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_parts_pg.html"
license: "Apache-2.0"
mode: "V"
---

The element **/package/parts** describes a set of hardware parts (devices other than the MCUs) contained in a Part 
pack (like the element \`<components>` is used to describe software components, the element \
 here defined
is used to describe hardware components).

A part must have a vendor (Hvendor=), a name (Hname=) and a class (Hclass=) which are used to identify the part. 
Optionally, a part may have a group (Hgroup=) and a sub-group (Hsub=) to add further categories, a revision (Hrevision=) in case 
different cuts of the same part exists, and a variant (Hvariant=). 
 
A part is therefore identified by a name and a class together with the vendor specified by the pack. 
A part vendor must ensure that the combination of name, revision, variant, class, group and sub-group is unique and not used by multiple parts.

**Example**
```
<package>
  ...
  
  <parts>

    <part Hvendor="STMicroelectronics" Hname="STSAFE-A110" Hvariant="STSAFA110DFSPL02" Hclass="Secure MCUs" Hgroup="Authentication">
      <description>Authentication, state-of-the-art security for peripherals and IoT devices</description>
      <feature type="Crypto" n="128.256" name="Authentication and security"/>
      <book name="Images/STSAFA110DFSPL02_UM.pdf" title="User Manual" public="true"/>
      <book name="Images/STSAFA110DFSPL02_DS.pdf" title="Datasheet" public="true"/>
      <image top="Images/STSAFA110DFSPL02_image.jpg" public="true">
      <environment name="SomeConfigTool">
        <file>STSAFA110DFSPL02_ConfigFile.cfg</file>
      </environment>
    </part>

    <part Hvendor="STMicroelectronics" Hname="STSAFE-A110" Hvariant="STSAFA110S8SPL02" Hclass="Secure MCUs" Hgroup="Authentication">
      <description>Authentication, state-of-the-art security for peripherals and IoT devices</description>
      <feature type="Crypto" n="128.256" name="Authentication and security"/>
      <book name="Images/STSAFA110S8SPL02_UM.pdf" title="User Manual" public="true"/>
      <book name="Images/STSAFA110S8SPL02_DS.pdf" title="Datasheet" public="true"/>
      <image top="Images/STSAFA110S8SPL02_image.jpg" public="true">
      <environment name="SomeConfigTool">
        <file>Descriptors/pinout/STSAFA110S8SPL02_ConfigFile.cfg</file>
      </environment>
    </part>

    ...

  </parts>

  ...
</package>
```
