---
id: "spec-package-element-package"
type: "concept"
domain: "pack"
title: "/package element: /package"
summary: "CMSIS-Pack version specification is inspired by the Semantic Versioning 2.0.0. Under this scheme, version numbers and the way they are incremented convey a meaning about the underlying content quality and the significance of changes from one version to the next."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html"
license: "Apache-2.0"
mode: "V"
---

| Parent Element | Element Chain |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| root | Document root |  |  |  |  |  |  |
| Attributes | Description | Type | Use |  |  |  |  |
| schemaVersion | CMSIS-PDSC schema version used for describing the software pack (for example, `"1.2"`). The version format is described in Version Type. | VersionType | required |  |  |  |  |
| xmlns:xs | Is set to: `"http://www.w3.org/2001/XMLSchema-instance"` to indicate compliance to the XML format. | xs:string | required |  |  |  |  |
| xs:noNamespaceSchemaLocation | Path and file name of the PACK.xsd Schema. For example, `"PACK.xsd"`. | xs:string | required |  |  |  |  |
| Dcore | Pack only used for a specific processor core. Use predefined values as listed in the table Device Cores. Note: do not apply for packs that define a device | DcoreEnum | optional |  |  |  |  |
| Dvendor | Pack only used for a specific silicon vendor of the device. Use predefined values as listed in the table Device Vendor. Note: do not apply for packs that define a device | DeviceVendorEnum | optional |  |  |  |  |
| Dname***** | Pack only used for a specific name of the device. Note: do not apply for packs that define a device | xs:string | optional |  |  |  |  |
| Tcompiler | Pack only used for a specific compiler toolchain (ARMCC, GCC, IAR, Tasking, ...). Use predefined values as listed in table Compiler Types. | CompilerEnumType | optional |  |  |  |  |
| Child Elements | Description | Type | Occurrence |  |  |  |  |
| name | Name of the software pack. Could be displayed by an installer. | xs:string | 1..1 |  |  |  |  |
| vendor | Name of the supplier or vendor of the software pack. | xs:string | 1..1 |  |  |  |  |
| description | Brief description of the software pack (maximum 256 characters, recommended 128 characters). | BriefDescType | 1..1 |  |  |  |  |
| `<ECCN>` | Section listing Export Control Classification Numbers (ECCN) for EU and US. | ECCNType | 0..1 |  |  |  |  |
| url | [URL](https://en.wikipedia.org/wiki/Uniform_resource_locator) (only [HTTPS](https://en.wikipedia.org/wiki/HTTPS) allowed) or [file URI](https://en.wikipedia.org/wiki/File_URI_scheme) location of the software pack. The URL can be used by installers for downloading, updating, or checking versions. If left empty, the Pack cannot be updated automatically from a server location. | xs:anyURI | 1..1 |  |  |  |  |
| supportContact | HTTPS URL or e-mail address for users to get support for the content of the Pack | xs:string | 0..1 |  |  |  |  |
| license | Path to a license document. | xs:string | 0..1 |  |  |  |  |
| licenseSets | Section listing one or more collections of license files which can be associated with one, multiple or all components | LicenseSetsType | 0..1 |  |  |  |  |
| dominate | A pack that has this element overrules other packs that provide identical device, API, or component definitions. | DominateType | 0..1 |  |  |  |  |
| requirements | Specifies other CMSIS-Packs, programming languages and compiler as well as their respective version or version range required by the components in this pack. | RequirementsType | 0..1 | create | !!! Deprecated, use cprj format instead !!! Use only when creating CMSIS software projects. | CreateType | 0..1 |
| repository | HTTPS URL of a public repository the pack originates from. | xs:anyURI | 0..1 |  |  |  |  |
| releases | Version release history with brief information about a software pack. | ReleasesGroup | 1..1 |  |  |  |  |
| changelogs | Section describing one or more changelog files which can be associated with one, multiple or all components and apis in the pack (default="true") | ChangelogsType | 0..1 |  |  |  |  |
| keywords | Defines keywords that might be used to find a software pack. Keywords may be also exported to web page to provide information for search engines, such as Google. | group | 0..1 |  |  |  |  |
| environments | Grouping element for environments information. Each inner environment element may be used to provide tool-specific information pertaining to the package as a whole. | group | 0..1 |  |  |  |  |
| generators | Specifies generator tools that have been used to create components. | GeneratorsType | 0..1 |  |  |  |  |
| devices | Defines the device family, the devices, and optionally variants (such as boards). | group | 0..1 |  |  |  |  |
| boards | Defines the development board support package. | BoardsType | 0..1 |  |  |  |  |
| parts | Defines the parts support package. | PartsType | 0..1 |  |  |  |  |
| taxonomy | Contains the description for a component class or for the combination between a component class and component group. | TaxonomyType | 0..1 |  |  |  |  |
| element_part-taxonomy "part-taxonomy" | Contains the description for a part class or for the combination between a part class and part group. | PartTaxonomyType | 0..1 |  |  |  |  |
| apis | Defines the API (Application Programming Interfaces) specifications contained in the software pack. | ApisType | 0..1 |  |  |  |  |
| conditions | Is a group that contains dependency definitions used within the Pack. These rules can describe dependencies on various levels: device attributes, components, or tools. Conditions are referenced by components and files. | ConditionsType | 0..1 |  |  |  |  |
| examples | Lists the examples that are included in the Pack. | group | 0..1 |  |  |  |  |
| csolution | Lists the clayer description files that are included in the Pack. | group | 0..1 |  |  |  |  |
| components | Lists the software components that are included in the Pack. | group | 0..1 |  |  |  |  |



***)** Wild-cards can be used to match names with the following definitions:
       - '*'  matches any substring
       - '?'  matches any single character
       - [abc] matches any character in the set (a,b,c)


 

 **Version Type**

CMSIS-Pack version specification is inspired by the Semantic Versioning 2.0.0.
Under this scheme, version numbers and the way they are incremented convey a meaning about the underlying content quality and the significance
of changes from one version to the next. A version consists of 3 mandatory and 2 optional sections:

```
MAJOR.MINOR.PATCH[-Pre Release][+Build Metadata]
```

1. **MAJOR:** increment MAJOR for backwards incompatible changes
  - non-negative integer
  - 0 indicates initial development, unstable and anything may change at any time
```
  ARM.CMSIS.0.9.0.pack  <  ARM.CMSIS.1.0.0.pack
```
2. **MINOR:** increment MINOR for backwards compatible additions and changes
  - non-negative integer
  - accepted:
    -- trailing zeros are accepted but effectively ignored for version comparison
```
    ARM.CMSIS.1.02.0.pack  equal to  ARM.CMSIS.1.2.0.pack
```
3. **PATCH:** increment PATCH for bug fixes not affecting compatibility
  - non-negative integer
  - accepted:
    - trailing zeros are accepted but effectively ignored for version comparison
    - a version ending after MINOR without specifying PATCH. In this case PATCH == 0 is assumed.
```
    ARM.CMSIS.1.1.pack equal to ARM.CMSIS.1.1.0.pack
```
4. _pre release:_ the optional pre-release string must start with a hyphen ('-') immediately after the _PATCH_ and consists of a series
   of dot separated ASCII alphanumerics and hyphen ([0-9A-Za-z-]).
  - accepted: the pre-release string immediately following the PATCH without a hyphen if the first item is a character.
```
  ARM.CMSIS.4.3.0-alpha.1
```
5. _build metadata:_ the optional build metadata must be denoted by appending a plus sign ('+') and a series of dot separated identifiers.
   Identifiers comprise only ASCII alphanumerics and hyphen [0-9A-Za-z-]+. Two versions that differ only in the build metadata, have the same precedence.
```
   ARM.CMSIS.4.3.0-alpha.1+build.102
```

The above is extending the recommendation that was given in previous version of this specification.:

Version types are used in:
- element_package (attribute: **schemaVersion)**
- element_release (attribute: **version)**
- element_api     (attribute: **Capiversion)**
- element_accept  (attributes: **Capiversion** and **Cversion)**
- element_bundle  (attribute: **Cversion)**
- element_component (attributes: **Capiversion** and **Cversion)**
- element_example (attribute: **version)**
- element_example_attribute_component (attribute: **Cversion)**

**Example:**
this example applies to element_release.
```
  <release version="1.4.2-RC2" ...>
```
