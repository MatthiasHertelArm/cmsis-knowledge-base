---
id: "spec-package-components-element-component-instances"
type: "concept"
domain: "pack"
title: "/package/components element: Component Instances"
summary: "Modern microcontrollers often have multiple instances of the same peripheral interface (for example UART, SPI, USB, etc.). To be able to have separate configuration files for each of these instances, Software Components can have multiple instances as well."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

Modern microcontrollers often have multiple instances of the same peripheral interface (for example UART, SPI, USB, etc.).
To be able to have separate configuration files for each of these instances, Software Components can have multiple instances
as well. The attribute **maxInstances** declares the maximum number of instances that can be used in a project for a certain
Software Component.

If the user selects for example two instances of the same component, all files with the attribute `"config"` will be copied
twice to the project. The name of the component (for example `config_mylib.h)` will be expanded with an `_\%Instance%`
number:
  -# Instance: config_mylib__0_.h
  -# Instance: config_mylib__1_.h

The availability of instances in a project can be made public in the `RTE_Components.h` file. This can be used to check for
the availability of a certain instance in the user application code:

```
        <RTE_Components_h>
          <!-- the following content goes into file 'RTE_Components.h' -->
          #define RTE_FileSystem_Drive_NOR_%Instance%      /* File System NOR Flash Drive %Instance% */
        </RTE_Components_h>
```
\n
  "Component instances in PDSC file and in development tools"
