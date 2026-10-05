---
id: "spec-technical-background-software-components"
type: "concept"
domain: "pack"
title: "Technical background: Software Components"
summary: "A software component encapsulates a set of related functions. Software components can contain C/C++ source files, object code, assembler files, header files, or libraries."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_creation.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/cp_Packs.html"
license: "Apache-2.0"
mode: "V"
---

A software component encapsulates a set of related functions. Software components can contain C/C++ source files, object code,
assembler files, header files, or libraries. The interfaces of software components should be defined with APIs
to make them substitutable by other compatible components at design time. In addition, CMSIS software components
should contain documentation for the software component. They may provide user code templates that give a starting point for
the application developer, and can have optional debug view descriptions for debuggers. 

CMSIS software components can also refer to multiple interfaces of other software components. This could be also a hardware
abstraction layer for a device peripheral. 

Configuration files contain application specific parameters for a software component. These files are typically copied to the
user project workspace; all other files are not modified by the user and can remain in a separate location which avoids that
a project workspace is polluted by many source files that should be considered as “black-box” elements by the application
programmer.





### Component classification


A component lists the files that belong to it and that are relevant for a project. The component itself or each individual
file may refer to a condition that must resolve to true; if it is false, the component or file is
not applicable in the given context.

Each software component must have the following attributes that are used to identify the component:
  - Component Class (`Cclass):` A component class which is a top-level component name, for example **CMSIS,** **Device,**
    **File** **System**
  - Component Group (`Cgroup):` A component group name, for example **CMSIS:RTOS,** **Device:Startup,** **File** **System:CORE**
  - Component Version (`Cversion):` the version number of the software component.

Optionally, a software component may have additional attributes:
  - Component Sub-Group (`Csub):` A component sub-group that is used when multiple compatible implementations of a component
    are be available. For example **CMSIS:RTOS:MyRTOS,** **Device:Driver** **USBD:Full-speed**
  - Component Variant (`Cvariant):` A variant of the software component is typically used when the same implementation has
    multiple top-level configurations, like debug and release.
  - Component Vendor (`Cvendor):` the supplier of the software component.
  - Cbundle: allows to combine multiple software components into a software bundle. For example if a network stack is used,
    all interfaces must match to that component.
  - Instances: allow to deploy multiple instances of a software component. Each instance can have a separate configuration
    file.


The `Cclass,` `Cgroup,` `Csub,` `Cvariant` and `Cversion` attributes are used together with the vendor specified by the
pack to identify a component. A component vendor must ensure that the combination `Cclass,` `Cgroup,` `Csub` and
`Cversion` is unique and not used by multiple components within the same Pack. Advertise a set of attributes to be used by
other software components using the element_taxonomy.

For a list of established Cclasses, refer to pack_Cclass.

In case multiple interdependent components (belonging to the same `Cclass)` form part of a solution, these can be grouped
in a so called **bundle.** 

Use the following syntax to reference to software components and APIs:\n
**`<Vendor>`::`<Cclass>`:`<Cgroup>`:`<Csub>`**
  
**Examples:**
  - **\::CMSIS:RTOS (API)** - the CMSIS-RTOS API.
  - **ARM::CMSIS:DSP** - the CMSIS-DSP Library.
  - **\::File System:Drive:NOR** - the NOR Flash Drive of a file system.

Here is an example for the display of software components in a development tool:

 "Display of a software component in development tools"



### Software Component Files


Each software component consists of a certain number of files. Each file has at least the following attributes:
- `name:` File path, file name, and file extension in the format path/name.extension. The file path is relative to the root
  directory of the Pack. 
- `category:` Defines the purpose of the file. Select the predefined value as listed in the table
  File Categories.

Optionally, every file may have the following attributes:
- `attr:` Defines the special use and handling of a file. Select a predefined value as defined in the table
  File Attributes.
- `condition:` Enter the identifier (attribute ****id**)** of a condition. The element is used
  if the condition resolves to `true`.
- `select:` Brief description and purpose of the file. The **_select_** attribute is **required** when **_attr_**
  is set to `template` or `interface`. When multiple template files of a component have the same
  **_select_** string, they are treated as a single selectable template. This way, multiple template or interface files
  can be bundled.
- `src:` Path information. The path is specified relative to the Pack Description File (PDSC).
- `version:` File-specific version information. This is used particularly for files copied into the project workspace.
  Before a file gets copied, a version check avoids unnecessary copy actions. If a file does not have a version, then the
  component version is used.



### File naming


It is good practice to name software component files uniquely. This is especially important for user
configuration files that are copied into a project. The CMSIS-Pack run-time environment copies configuration files
by `\<Cclass>` into the directory structure. For example, `./RTE/BSP` stores all user editable files
of the `\<Cclass>` **BSP.** If the file name is not unique, clashes might occur with other software components of the same
`\<Cclass>` (for example when you name the configuration file `user_config.h).`

Recommended configuration file naming is as follows: `\`<vendor>`_\`<unique_component>`_config`

**Examples**
- MyVendor_MyBSP_config.h
- MyVendor_MyNetworkStack_config.h

**Note:**
Please be aware that you also need to make sure that your configuration files need to be uniquely named and versioned if
your software component consists of `\<Cvariants>` that differ in the configuration files. Otherwise, it might happen that
your toolchain is not able to resolve correctly and users might end up with unconfigurable components, especially when they
change the variant while developing the application.
