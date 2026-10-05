---
id: "spec-package-parts-element-package-parts-part"
type: "concept"
domain: "pack"
title: "/package/parts element: /package/parts/part"
summary: "This element specifies a part. At least one part element must be specified per parts."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/parts_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_parts_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element specifies a part. At least one part element must be specified per parts.



| Parent | Chain |  |  |
|---|---|---|---|
| parts | element_parts |  |  |
| Attributes | Description | Type | Use |
| Hvendor | Defines the vendor this part is shipped by. It is a mandatory part of the part ID and will be inherited from the package vendor if not specified. | xs:string | optional |
| Hname | The part name used by the part vendor to identify and group a specific set of parts | xs:string | required |
| Hclass | Defines the part class to which the part belongs. | HclassType | optional |
| Hgroup | Defines the part group to which the part belongs. | HgroupType | optional |
| Hsub | Defines the part subgroup. | HsubType | optional |
| Hvariant | Specifies the exact part name (e.g. the commercial/selling name) in case the one indicated in the **Hname** is not enough to uniquely identify the part. | xs:string | optional |
| Hrevision | Revision of the part that is suited to be used. | xs:string | optional |
| Child Elements | Description | Type | Occurrence |
| description | Brief summary of the part (maximum 256 characters, recommended 128 characters). | BriefDescType | 0..1 |
| feature | Describes the features of the part. | DeviceFeatureType | 0..* |
| book | Specifies documents that are relevant for the part. | BookType | 0..* |
| image | Specifies the part pictures. | ComplexType | 0..1 |
| environment | Specifies tool specific settings. | EnvironmentType | 0..* |




 

 **Part Subgroups**

Part Subgroups are specified by the element **Hsub** and create subcategories within Part Classes (**Hclass)** and Part Groups (**Hgroup).**
A **Hsub** name is of type **HsubType,** that is a **xs:string** with a length between 3 and 32 characters.
No **Hsub** names have been predefined.

Part Subgroups can be used in element element_part

**Example:**
```
  <... Hclass="MEMS and Sensors" Hgroup="Environmental" Hsub="Temperature" ...>
```
