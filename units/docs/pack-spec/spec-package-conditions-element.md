---
id: "spec-package-conditions-element"
type: "concept"
domain: "pack"
title: "/package/conditions element"
summary: "The grouping element element_conditions contains all conditions defined for the software pack."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/conditions_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html"
license: "Apache-2.0"
mode: "V"
---

The grouping element element_conditions contains all conditions defined for the software pack.

A condition describes dependencies on device, processor, and tool attributes as well as the presence of other components.
The **conditions** are used to define AND and OR rules used to make components conditional and therefore only available under certain circumstances,
e.g. for specific devices or processors. The conditions are also used to express dependencies between components.

Each condition has an **id** that is unique within the scope of a the description. An **id** can be referenced in the condition attribute of components, apis,
examples, files and other conditions to become conditional. If a condition resolves to false during the processing of the description, the respective element will
be ignored.

**Example:**
```
  <conditions>
    <condition id="CM4">                           <!-- defines the condition with the ID "CM4" -->
      <description>True if the active device has a Cortex-M4 processor</description>
      <require Dcore="Cortex-M4"/>                 <!-- device has a Cortex-M4 processor -->
    </condition>

    <condition id="Cortex-M">                      <!-- defines the condition with the ID "Cortex-M" -->
      <description>True if the active device has a Cortex-M0 or Cortex-M0+ or Cortex-M3 or Cortex-M4 or SC000 or SC3000 processor </description>
      <accept Dcore="Cortex-M0"/>                  <!-- any of the following cores will make the condition resolve to true -->
      <accept Dcore="Cortex-M0+"/>
      <accept Dcore="Cortex-M23"/>
      <accept Dcore="Cortex-M3"/>
      <accept Dcore="Cortex-M33"/>
      <accept Dcore="Cortex-M4"/>
      <accept Dcore="SC000"/>
      <accept Dcore="SC300"/>
    </condition>

    <condition id="CMSIS-Core">                     <!-- defines the condition with the ID "CMSIS-Core" -->
      <description>True if the component Device Startup is selected and the device has a Cortex-M processor</description>
      <require Cclass="Device" Cgroup="Startup"/>   <!-- needs a software component Device Startup AND ... -->
      <require condition="Cortex-M"/>               <!-- ... needs that condition with ID=Cortex-M to be true. -->
    </condition>

    <condition id="CMSIS-DSP">                      <!-- defines the condition with the ID "CMSIS-DSP" -->
      <description>True if CMSIS-Core == TRUE and either GCC or ARMCC and device running in little-endian byte ordering</description>
      <require condition="CMSIS-Core"/>             <!-- needs a software component Device Startup AND ... -->
      <accept Tcompiler="GCC"/>                     <!-- ... works either with the GCC compiler OR ... -->
      <accept Tcompiler="ARMCC"/>                   <!-- ... the ARMCC compiler AND ... -->
      <require Dendian="Little-endian"/>            <!-- ... requires a device running in little-endian byte ordering -->
    </condition>

    <condition id="No STM32">                       <!-- defines the condition with ID "No STM32" -->
      <description>False if the device is from ST and the device name starts with "STM32"</description>
      <deny Dvendor="STMicroelectronics:13" Dname="STM32*"/>  <!-- device name must not start with STM32 and be from vendor ST-->
    </condition>

    <condition id="HTS221 Part">                    <!-- defines the condition with ID "HTS221 Part" -->
      <description>True if the target part is the HTS221TR</description>
      <require Hvendor="STMicroelectronics" Hname="HTS221TR"/>  <!-- part name must be HTS221TR and be from vendor ST-->
    </condition>
  </conditions>
```
