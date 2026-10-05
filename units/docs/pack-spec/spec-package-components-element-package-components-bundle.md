---
id: "spec-package-components-element-package-components-bundle"
type: "concept"
domain: "pack"
title: "/package/components element: /package/components/bundle"
summary: "A bundle describes a named collection of inter-operable components of the identical Cvendor, Cclass and Cversion. Components enclosed in a bundle must not specify any of the following attributes Cvendor, Cclass and Cversion."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

A bundle describes a named collection of inter-operable components of the identical **Cvendor,** **Cclass** and **Cversion.**
Components enclosed in a bundle must not specify any of the following attributes **Cvendor,** **Cclass** and **Cversion.**



  | 
    Parent | 
    Element Chain | 
  

  | 
    components | 
    element_components | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    Cbundle | 
    Defines the name of the bundle. It becomes a mandatory part of the component ID. | 
    xs:string | 
    required | 
  

  | 
    Cvendor | 
    Defines the component vendor all components of this bundle belong to. If not explicitly set the component vendor is
      derived from the package vendor. The component vendor is a mandatory part of the component ID. | 
    xs:string | 
    optional | 
  

  | 
    Cclass | 
    Defines the component class to which all components in the bundle belong. Is a mandatory part of the component ID.
      Predefined values can be used as listed in the table Component Classes.
     | 
    CclassType | 
    required | 
  

  | 
    Cversion | 
    Defines the component version inherited by all components contained in the bundle. The component version is a mandatory part of the component ID.
      The version format is described in Version Type. Note: components can redefine their version using the Cversion attribute
      of the component element.
     | 
    VersionType | 
    required | 
  

  | 
    licenseSet | 
    Reference to the `licenseSet` with the given identifier `ID` specified in the licenseSets section of the package description.
      A licenseSet describes one or more license files which in this case govern all components of this bundle. If the licenseSet is 
      different for different components in the bundle, the licenseSet attribute is required to be assigned on a component level. | 
    xs:string | 
    optional | 
  

  | 
    changelog | 
    Reference to the `changelog` with the given identifier `ID` specified in the changelogs section of the package description.
      A changelog references a text file in the pack with a path relative to the pdsc containing changelog information for all components of this bundle.
      If the changelog files differ for the components in the bundle, the changelog attribute is required to be set on a component level. | 
    xs:string | 
    optional | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    description | 
    Brief description of the bundle (maximum 256 characters, recommended 128 characters). | 
    BriefDescType | 
    1..1 | 
  

  | 
    doc | 
    Documentation for the bundle: File path, file name, and file extension in the format **path/name.extension.**
      The file path is relative to the root directory of the Pack.
    xs:string | 
    1..1 | 
  

  | 
    component | 
    Grouping element for components. | 
    ComponentType | 
    1..* |
