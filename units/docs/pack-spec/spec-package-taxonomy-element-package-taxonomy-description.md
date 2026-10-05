---
id: "spec-package-taxonomy-element-package-taxonomy-description"
type: "concept"
domain: "pack"
title: "/package/taxonomy element: /package/taxonomy/description"
summary: "This element describes a component class or the combination between a component class and a component group. Components are categorized by Cclass and Cgroup. The creator of a package can define names for Cclass and Cgroup."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_taxonomy.html"
license: "Apache-2.0"
mode: "V"
---

This element describes a component class or the combination between a component class and a component group.
Components are categorized by **Cclass** and **Cgroup.** The creator of a package can define names for **Cclass** and
**Cgroup.** Thus, configuration tools can display the set of available components. A document can be referenced using the
attribute **doc.** The attribute **generator** can be used to reference to a generator tool. The **id** of the generator
needs to be the same as specified in the element element_generator. The description itself is a string entered between
the opening and closing tags of the element **description.**

It is recommended to use an already agreed taxonomy for interchangeable components. For example, the combination of class `CMSIS`
and group `Startup` is defined for the device-specific CMSIS-Core (Cortex-M) files.


 

**Example:**
```
  <taxonomy>
    <description Cclass="Board Support">Generic Interfaces for Evaluation and Development Boards</description>
    <description Cclass="CMSIS" doc="CMSIS/Documentation/General/html/index.html">Cortex Microcontroller Software Interface Components</description>
    <description Cclass="Device" doc="CMSIS/Documentation/Core/html/index.html">Startup, System Setup</description>
    <description Cclass="CMSIS Driver" doc="CMSIS/Documentation/Driver/html/index.html">Unified Device Drivers compliant to CMSIS-Driver Specifications</description>
    <description Cclass="File System">File Drive Support and File System</description>
    <description Cclass="Graphics">Graphical User Interface</description>
    <description Cclass="Network">Network Stack using Internet Protocols</description>
    <description Cclass="USB">Universal Serial Bus Stack</description>
    <description Cclass="RTOS">Realtime Operating System</description>
  </taxonomy>
```

**Note:** You **must** **not** use Windows or Linux
reserved characters for
**Cclass,** **Cgroup,** and **Csub** names! Some development tools use these names to create a directory structure for the
software components in projects. Reserved characters are:
```
< (less than)
> (greater than)
: (colon)
" (double quote)
/ (forward slash)
\ (backslash)
| (vertical bar or pipe)
? (question mark)
(asterisk)
```


 



  | 
    Parent Element | 
    Element Chain | 
  

  | 
    taxonomy | 
    element_taxonomy | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    Cclass | 
    Component Class Name. Can be defined by the creator of the package. Predefined values can be used as listed in the table Component Classes. | 
    CclassType | 
    required | 
  

  | 
    Cgroup | 
    Component Group Name. Can be defined by the creator of the package. Predefined values can be used as listed in the table Component Groups. | 
    CgroupType | 
    optional | 
  

  | 
    doc | 
    Reference to documentation. | 
    xs:string  | 
    optional | 
  

  | 
    generator | 
    Reference to a generator. Enter the **id** value of the element element_generator. | 
    xs:string  | 
    optional | 
  

  | 
    public | 
    Set publishing permissions for the documentation. If \tagem{public} is `true`, then the vendor gives permission
        to extract the documentation from the pack and publish it on a web-page. Links to web pages are assumed to be public.
        The default value is `true` (this is also the basic assumption if the tag is missing). | 
    xs:boolean | 
    optional | 
  




 

 **Table: Component Classes**

Component Class names are strings with a minimum length of 3 characters and a maximum length of 32 characters.
Component class names are specified in the section element_taxonomyDescription.

These values can be used in the elements:
- element_accept
- element_require
- element_deny
- element_example_attribute_component
- element_component
- element_bundle
- element_api
- element_taxonomyDescription

**Example:**
```
  <... Cclass="CMSIS" ...>
```

 

The table lists predefined Component Classes.


  | 
    Cclass= | 
    Description | 
  

  | 
    Audio | 
	Software components for audio processing | 
  

  | 
    Board Support | 
	Components providing interfaces for Evaluation and Development Boards | 
  

  | 
    Board Part | 
    Drivers that support an external component available on an evaluation board | 
  

  | 
    Compiler | 
    Components implementing compiler specific interfaces (e.g. Retargeting) | 
  

  | 
    CMSIS | 
    Components defined by the Common Microcontroller Software Interface Standard (e.g. CMSIS-Core(M), CMSIS-Core(A), CMSIS-DSP and CMSIS-RTOS) | 
  

  | 
    CMSIS Driver | 
    Components implementing unified device drivers compliant to CMSIS-Driver (e.g. UART, SPI, USB, etc.)  | 
  

  | 
    Device | 
    Components containing device specific implementations of non-standard APIs (e.g. HAL drivers, CMSIS Startup files) | 
  

  | 
    Data Exchange | 
    Components implementing some kind of data exchange or data formatter | 
  

  | 
    Extension Board | 
    Drivers that support an extension board or shield | 
  

  | 
    File System | 
    Components implementing some kind of File Systems (e.g. Flash or RAM based file systems) | 
  

  | 
    Graphics | 
    Components implementing some kind of Display and Graphics Software | 
  

  | 
    IoT Client | 
    Components implementing some kind of IoT cloud client connector | 
  

  | 
    IoT Utility | 
    IoT specific software utility | 
  

  | 
    Network | 
    Components implementing some kind of network communications (e.g. TCP/IP Stack) | 
  

  | 
    RTOS | 
    Components implementing some kind of real-time operating system (e.g. FreeRTOS, Micrium Real Time Kernel) | 
  

  | 
    Security | 
    Components implementing some kind of encryption for secure communication or storage | 
  

  | 
    USB | 
    Components implementing some kind of USB interfaces (e.g. Host and Device interfaces) | 
  

  | 
    Utility | 
    Generic software utility components | 
  




 

 **Table: Component Groups**

Component Group names are specified by the element **Cgroup** and create categories within a Component Class specified by the element **Cclass**.
The creator of the Pack can define the names in the element element_taxonomyDescription.
A Component Group name is string with a length between 3 and 32 characters.

**Example:**
```
  <... Cgroup="RTOS" Cclass="CMSIS"...>
```

 

Component Groups can be used in the elements:
- element_accept
- element_require
- element_deny
- element_example_attribute_component
- element_component
- element_api
- element_taxonomyDescription

The following table lists predefined values for the Component Class **Cclass="CMSIS"**.


  | 
    Cgroup= | 
    Description | 
  

  | 
    CORE | 
    A component containing core support in accordance to the CMSIS-Core(M)
  or CMSIS-Core(A) specifications. | 
  

  | 
    DSP | 
    A component implementing the CMSIS-DSP API specification. | 
  

  | 
    NN Lib | 
    A component implementing the CMSIS-NN API specification. | 
  

  | 
    RTOS | 
    A component implementing the CMSIS-RTOS API specification. | 
  

  | 
    RTOS2 | 
    A component implementing the CMSIS-RTOS v2 API specification. | 
  



The following table lists predefined values for the Component Class **Cclass="Device"**.


  | 
    Cgroup= | 
    Description | 
  

  | 
    Startup | 
    A component containing the device support files system_device.c and startup_device.s/c in accordance to the CMSIS-Core(M)
  or CMSIS-Core(A) specifications (startup, system and device files). |
