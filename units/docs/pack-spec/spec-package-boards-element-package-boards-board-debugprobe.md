---
id: "spec-package-boards-element-package-boards-board-debugprobe"
type: "concept"
domain: "pack"
title: "/package/boards element: /package/boards/board/debugProbe"
summary: "This element specifies an optional on-board debug probe."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/boards_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element specifies an optional on-board debug probe.



| Parent | Chain |  |  |
|---|---|---|---|
| board | element_board |  |  |
| Attributes | Description | Type | Use |
| deviceIndex |  | xs:string | optional |
| name | Type of on-board debug probe. | `CMSIS-DAP`, `DAP-Link`, `ST-Link`, `J-Link` or `JLink Server`. | required |
| version | Debug probe version. | xs:string | required |
| debugLink | Debug connection from probe to processor. | `jtag`, or `swd` | required |
| debugClock | Debug controller clock speed. | NonNegativeInteger | required |
| connector | String describing the debug connector. Usually one of these: `Mini-USB`, `Micro-USB`, `USB-C`. | xs:string | required |
