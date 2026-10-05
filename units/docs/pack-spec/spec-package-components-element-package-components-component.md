---
id: "spec-package-components-element-package-components-component"
type: "concept"
domain: "pack"
title: "/package/components element: /package/components/.../component"
summary: "A component describes a collection of files (source, header, configuration, library) that can be versioned and categorized."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

A component describes a collection of files (source, header, configuration, library) that can be versioned and categorized.



| Parent | Element Chain |  |  |
|---|---|---|---|
| components | element_components |  |  |
| components | element_bundle |  |  |
| Attributes | Description | Type | Use |
| Cvendor | Defines the component vendor this component is shipped by. It is a mandatory part of the component ID and will be inherited from the package vendor if not specified. \n `Must not be specified for a component within a bundle.` | xs:string | optional |
| Cclass | Defines the component class to which the component belongs. This is a mandatory part of the component ID. Predefined values can be used as listed in the table Component Classes. \n `Must not be specified for a component within a bundle.` | CclassType | required |
| Cgroup | Defines the component group to whoch the component belongs. Is a mandatory part of the component ID. Predefined values can be used as listed in the table Component Groups. | CgroupType | required |
| Csub | Defines the component subgroup. Is an optional part of the component ID. The type is described in Component Subgroups. | CsubType | optional |
| Cvariant | Defines a variant of a component. Is an optional part of the component ID. The variant specifier is a brief string (for example: `release`, `debug`). Note: The selection of component variants is mutually exclusive. | xs:string [1..32] | optional |
| Cversion | Defines the version of this component. Is a mandatory part of the component ID. The version format is described in Version Type. VersionType | required |  |
| Capiversion | For components that are based on an API header files, it defines the version of the API used by this component. It ensures that the API header file with the same or higher version is acceptable for using that component. The version format is described in Version Type. | VersionType | optional |
| condition | Enter the **id** of a condition. The component is available and can be selected when the condition is true. | xs:string | optional |
| custom | When set to `true`, the component requires a custom implementation. This attribute should suppress the automatic component resolver, so it requires always manual selection. | xs:boolean | 0..1 |
| maxInstances | Maximum allowed instances of a component in a project. Default is `1` for one instance. The range is [`1..10`]. | xs:integer | optional |
| isDefaultVariant | Identifies this component variant to be the preferred variant for tool driven selection through an automated update algorithm [Version 1.4.0]. If in a new version of a component variants are introduced, the default variant is automatically selected if only the component without variant is specified. This variant is supposed to be the most compatible continuation of the previous component version. Note: It is the component vendor's responsibility to have only a single component variant having this attribute enabled. | xs:boolean | optional |
| generator | This links the component with a generator description located in the same file. If this component is selected by the run time configuration, the tool will test whether the configured gpdsc file does already exist or not. If the file is not present, then the command specified by the referenced generator section, will be invoked. If the gpdsc file already exists it will be included into the project | xs:string | optional |
| licenseSet | Reference to the `licenseSet` with the given identifier `ID` specified in the licenseSets section of the package description. A licenseSet describes one or more license files that govern the component. | xs:string | optional |
| view | Defines the user view of this component. A component may be hidden, for example when it is managed by a generator. | ViewType | optional |
| changelog | Reference to the `changelog` with the given identifier `ID` specified in the changelogs section of the package description. A changelog references a text file in the pack with a path relative to the pdsc containing changelog information for the component. The content of the referenced changelog file is not required to be exclusively used for a single component. | xs:string | optional |
| Child Elements | Description | Type | Occurrence |
| deprecated | When set to `true`, then the component is deprecated and no longer maintained. Default is `false` to indicate an actively maintained component. | xs:boolean | 0..1 |
| description | Brief description of the component (maximum 256 characters, recommended 128 characters). | BriefDescType | 1..1 |
| RTE_Components_h | Source code that is copied into the file RTE_Components_h when the component is selected by the run time environment configuration. | xs:string | 0..1 |
| Pre_Include_Global_h | Source code that is copied into the file Pre_Include_Global_h when the component is selected by the run time environment configuration. | xs:string | 0..1 |
| Pre_Include_Local_Component_h | Source code that is copied into the file Pre_Include_Local_Component_h \`<Cclass>`_\`<Component_name>`.h when the component is selected by the run time environment configuration. | xs:string | 0..1 |
| files | Grouping element for all files that are part of this component. | group | 1 |
| extensions | Grouping element for all extensions concerning this component. | group | 0..1 |
| environments | Grouping element for all environments concerning this component. | group | 0..1 |




 


 **View Type**

The ViewType defines the user view of a component in component selection windows (i.e. Manage Run-Time Environment or Manage Software Components) and command line tools for the component list command.

ViewType                | Description
:-----------------------|-----------------------------------
**always** (default) | Component is always presented to the user. It appears in component selection windows and is listed as available component.
**never**            | Component is never presented to the user as it contains supportive files, i.e. for a generator. However it can be explicitly requested by an user, i.e. with the `component:` node.
**maskable**         | It is the choice of the tool to hide this component. A tool may offer an option to show such components.

**Examples:**

1. Component **A** that requires sub-components **A1** and **A2**. These components may have the attribute view="maskable" as it makes no sense to select just **A1** or **A2**.

2. Component **B1**, **B2**, and **B3** all require component **B-core**, but **B-core** on it's own makes no sense. The component **B-core** may have the attribute view="maskable" as it makes no sense to select just it.

3. Component **G** contains files that are required by a generator, but does not contain any direct usable source files. The component **G** may have the attribute view="never" as it should be not user selectable.



 

 **Component Subgroups**

Component Subgroups are specified by the element **\b** Csub, and
create subcategories within Component Classes (**\b** Cclass) and Component Groups (**\b** Cgroup).
A **\b** Csub name is of type **xs:string** with a length between 3 and 32 characters.
No **\em** Csub names have been predefined.

Subgroups exists in the elements:
- element_accept
- element_require
- element_deny
- element_component
- element_example_attribute_component

**Example:**
```
  <... Csub="MyRTOS" Cgroup="RTOS" Cclass="CMSIS"...>
```
