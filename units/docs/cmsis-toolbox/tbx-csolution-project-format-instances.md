---
id: "tbx-csolution-project-format-instances"
type: "concept"
domain: "project"
title: "CSolution Project Format: Source File Management / `instances:`"
summary: "Allows to add multiple instances of a component and actually applies to configuration files. For a detailed description, refer to Open-CMSIS-Pack specification: Component Instances."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#instances"
license: "Apache-2.0"
mode: "V"
---

_Part of: Source File Management_

Allows to add multiple instances of a component and actually applies to configuration files.
For a detailed description, refer to [Open-CMSIS-Pack specification: Component Instances](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#Component_Instances).

**Example:**

```yml
  components:
    - component: USB:Device
      instances: 2
```

If the user selects multiple instances of the same component, all files with the attribute `config` in the `*.PDSC` file
will be copied multiple times to the project. The name of the component (for example config_mylib.h) will get a postfix
`_n` whereby `n` is the instance number starting with 0.

- Instance 0: `config_usb_device_0.h`
- Instance 1: `config_usb_device_1.h`

The availability of instances in a project can be made public in the `RTE_Components.h` file. The existing way to extend
the `%Instance%` with the instance number `n`.
