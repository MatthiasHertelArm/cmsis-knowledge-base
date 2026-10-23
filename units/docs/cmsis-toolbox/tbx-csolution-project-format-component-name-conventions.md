---
id: "tbx-csolution-project-format-component-name-conventions"
type: "concept"
domain: "project"
title: "CSolution Project Format: Name Conventions / `component:` Name Conventions"
summary: "The csolution Project Manager uses the following syntax to specify the component: names in the .yml files."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#component-name-conventions"
license: "Apache-2.0"
mode: "V"
---

_Part of: Name Conventions_

The **`csolution` Project Manager** uses the following syntax to specify the `component:` names in the `*.yml` files.

```yml
[Cvendor::] Cclass [&Cbundle] :Cgroup [:Csub] [&Cvariant] [@[>=]Cversion]
```

Components are defined using the [Open-CMSIS-Pack: `<component>` element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component). Several parts of a `component` are optional.  For example, it is possible to just define a component using the `Cclass` and `Cgroup` names. All elements of a component name are summarized in the following table.

Element    |              | Description
:----------|:-------------|:---------------------
`Cvendor`  |   Optional   | Name of the component vendor as defined in `<components>` element or by the package vendor of the software pack.
`Cclass`   | **Required** | Component class name as defined in `<components>` element of the software pack.
`Cbundle`  |   Optional   | Bundle name of the component class as defined in `<bundle>` element of the software pack.
`Cgroup`   | **Required** | Component group name as defined in `<components>` element of the software pack.
`Csub`     |   Optional   | Component sub-group name as defined in `<components>` element of the software pack.
`Cvariant` |   Optional   | Component variant name as defined in `<components>` element of the software pack.
`Cversion` |   Optional   | Version number of the component, with `@1.2.3` that must exactly match, or `@>=1.2.3` that allows any version higher or equal.

**Partly defined components**

A component can be partly defined in *csolution project files* (`*.cproject.yml`, `*.clayer.yml`, `*.genlayer.yml`) by omitting `Cvendor`, `Cvariant`, and `Cversion`, even when these are part of the `components` element of the software pack. The component select algorithm resolves this to a fully defined component by:

- when a partly specified component resolves to several possible choices, the tool selects:
    - (a) the default `Cvariant` of the component as defined in the PDSC file.
    - (b) the component with the higher `Cversion` value.
    - (c) an error message is issued when two identical components are defined by multiple vendors and `Cvendor` is not specified.
- the partly specified component is extended by:
    - version information from the software pack.
    - default variant definition from the software pack.

The fully resolved component name is shown in the [`*.cbuild.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/YML-CBuild-Format.md) output file.

!!! Note
    Before CMSIS-Toolbox 2.7, a component that omitted `Csub` resolved to the first matching component. Installing additional software packs could therefore change component selection. When a component is defined with `Csub` it is now required to specify it.

**Multiple component definitions are rejected**

- A component can only be added once in the *csolution project files*; duplicates cause an error.
- For components with a `Cvariant` only one variant of that component may be selected in the *csolution project files*; multiple variants cause an error.
- When selecting components with a `Cbundle`, all components of the same `Cclass` in the *csolution project files* must belong to the same bundle; violation of the bundle consistency cause an error.

**Examples:**

```yml
- component: CMSIS:CORE                               # CMSIS Core component (vendor selected by `csolution` ARM)
- component: ARM::CMSIS:CORE                          # CMSIS Core component from vendor ARM (any version)
- component: ARM::CMSIS:CORE@5.5.0                    # CMSIS Core component from vendor ARM (with version 5.5.0)
- component: ARM::CMSIS:CORE@>=5.5.0                  # CMSIS Core component from vendor ARM (with version 5.5.0 or higher)

- component: Device:Startup                           # Device Startup component from any vendor

- component: CMSIS:RTOS2:Keil RTX5                    # CMSIS RTOS2 Keil RTX5 component with default variant (any version)
- component: ARM::CMSIS:RTOS2:Keil RTX5&Source@5.5.3  # CMSIS RTOS2 Keil RTX5 component with variant 'Source' and version 5.5.3

- component: Keil::USB&MDK-Pro:CORE&Release@6.15.1    # USB CORE component from bundle MDK-Pro in variant 'Release' and version 6.15.1
```
