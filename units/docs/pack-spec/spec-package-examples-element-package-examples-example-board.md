---
id: "spec-package-examples-element-package-examples-example-board"
type: "concept"
domain: "pack"
title: "/package/examples element: /package/examples/example/board"
summary: "This element specifies the board that can be used with the example project."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/examples_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element specifies the board that can be used with the example project. 

**Example:**
```
  <board name="MV1000A" vendor="MyVendor"/>
```


 		



| Parent | Chain |  |  |
|---|---|---|---|
| example | element_example |  |  |
| Attributes | Description | Type | Use |
| vendor | Vendor name of the board. | xs:string | required |
| name | Commercial name of the board. | xs:string | required |
| Dvendor | Vendor name of the device used on the board. Use predefined values as listed in the table Device Vendor. | DeviceVendorEnum | optional |
| Dfamily | Name of the target device family used on the board. This attribute is optional if either DsubFamily or Dname is already specified. \n **`Deprecated since version 1.1`** | xs:string | optional |
| DsubFamily | Name of the target device sub-family used on the board. This attribute is optional if either Dfamily or Dname is already specified. \n **`Deprecated since version 1.1`** | xs:string | optional |
| Dname | Name of the target device used on the board. This attribute is optional if either Dfamily or DsubFamily is already specified. \n **`Deprecated since version 1.1`**. | xs:string | optional |



**Note:**
Values for **`deprecated attributes`** are read from the board description element element_board_mountedDevice.
