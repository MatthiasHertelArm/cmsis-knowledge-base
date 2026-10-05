---
id: "tbx-csolution-project-format-device-name-conventions"
type: "concept"
domain: "project"
title: "CSolution Project Format: Name Conventions / `device:` Name Conventions"
summary: "The device specifies multiple attributes about the target that range from the processor architecture to Flash algorithms used for device programming. The following syntax is used to specify a device: value in the .yml files."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#device-name-conventions"
license: "Apache-2.0"
mode: "V"
---

_Part of: Name Conventions_

The device specifies multiple attributes about the target that range from the processor architecture to Flash
algorithms used for device programming. The following syntax is used to specify a `device:` value in the `*.yml` files.

```yml
[ [ Dvendor:: ] Dname] [:Pname]
```

Element       |          | Description
:-------------|:---------|:---------------------
`Dvendor`     | Optional | Name (without enum field) of the device vendor-defined in `<devices><family>` element of the software pack.
`Dname`       | Optional | Device name (Dname attribute) or, when used, the variant name (Dvariant attribute) as defined in the \<devices\> element.
`Pname`       | Optional | Processor identifier (Pname attribute) as defined in the `<devices>` element.

!!! Note
    - All elements of a device name are optional, which allows supplying additional information, such as the `:Pname` at
      different stages of the project. However, the `Dname` itself is a mandatory element and must be specified in
      the context of the various project files.
    - `Dvendor::` must be used in combination with the `Dname`.

**Examples:**

```yml
device: NXP::LPC1768                       # The LPC1788 device from NXP
device: LPC1788                            # The LPC1788 device (vendor is evaluated from DFP)
device: LPC55S69JEV98                      # Device name (exact name as defined in the DFP)
device: LPC55S69JEV98:cm33_core0           # Device name (exact name as defined in the DFP) with Pname specified
device: :cm33_core0                        # Pname added to a previously defined device name (or a device derived from a board)
```
