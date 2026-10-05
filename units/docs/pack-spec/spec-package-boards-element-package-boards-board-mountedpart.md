---
id: "spec-package-boards-element-package-boards-board-mountedpart"
type: "concept"
domain: "pack"
title: "/package/boards element: /package/boards/board/mountedPart"
summary: "The element specifies the parts (any device other than the MCU) mounted on the board. The Hname attribute, togheter with the Hvendor and (eventually) the Hvariant, must uniquely specify the part."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/boards_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html"
license: "Apache-2.0"
mode: "V"
---

The element specifies the parts (any device other than the MCU) mounted on the board. The Hname attribute, togheter with the Hvendor and (eventually) the Hvariant, must uniquely specify the part.

**Example**
```
<mountedPart n="1" Hvendor="STMicroelectronics" Hname="STSAFE-A110" Hvariant="STSAFA110DFSPL02"/>
```

 		



| Parent | Chain |  |  |
|---|---|---|---|
| board | element_board |  |  |
| Attributes | Description | Type | Use |
| n | Number of the parts with the same name and vendor mounted on the board. | xs:string | required |
| Hvendor | Vendor name of the part specified by **Hname. | xs:string | required |
| Hname | The part name used by the part vendor to identify and group a specific set of parts. | xs:string | required |
| Hvariant | Specifies the exact part name (e.g. the commercial/selling name) in case the one indicated in the **Hname** is not enough to uniquely identify the part. | xs:string | optional |
| Hrevision | Revision of the part that is suited to be used. | xs:string | optional |
