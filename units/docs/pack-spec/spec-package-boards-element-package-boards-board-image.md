---
id: "spec-package-boards-element-package-boards-board-image"
type: "concept"
domain: "pack"
title: "/package/boards element: /package/boards/board/image"
summary: "This element specifies the picture of a development board. Maximum one image element can be specified. None must be specified."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/boards_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element specifies the picture of a development board. Maximum one image element can be specified. None must be specified.
Four different picture types (`large`, `small`, `bottom` and `perspective`) can be specified for the same \tagem{image} element at the same time.
Attribute `large` displays the 'top' side of the board.

**Example:**
```
<image large="Images/board_image_1.png"
       bottom="https://images.vendor.com/Images/board_image_2.png"
       perspective="https://images.vendor.com/Images/board_image_3.png"
       small="Images/board_image_1_small.png"
/>
```

 		



| Parent | Chain |  |  |
|---|---|---|---|
| board | element_board |  |  |
| Attributes | Description | Type | Use |
| large | Specifies the path to a large image. The path is relative to the pack base directory or a link to an image on an external web site. Attribute 'large' displays the 'top' side of the board. | xs:string | optional |
| small | Specifies the path to a small image. The path is relative to the pack base directory or a link to an image on an external web site. Attribute 'small' displays the 'top' side of the board at a lower resolution than in 'large' attribute. | xs:string | optional |
| bottom | Specifies the path to a bottom image. The path is relative to the pack base directory or a link to an image on an external web site. | xs:string | optional |
| perspective | Specifies the path to a perspective image. The path is relative to the pack base directory or a link to an image on an external web site. | xs:string | optional |
| public | Set publishing permissions for the documentation. If \tagem{public} is `true`, then the vendor gives permission to extract the documentation from the Pack and publish it on a web-page. Links to web pages are assumed to be public. If no \tagem{public} tag is available, it is assumed that publishing is allowed (default value is `true`). | xs:boolean | optional |
