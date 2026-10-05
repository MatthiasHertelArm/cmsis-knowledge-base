---
id: "spec-package-boards-element-package-boards-board-debuginterface"
type: "concept"
domain: "pack"
title: "/package/boards element: /package/boards/board/debugInterface"
summary: "This element describes the debug interface of a board. All available debug interfaces specifying on-board adapters as well as hardware connectors for external debug adapter should be listed here."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/boards_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element describes the debug interface of a board. All available debug interfaces specifying on-board adapters as well
as hardware connectors for external debug adapter should be listed here. If a board has no device mounted or if the board
describes virtual hardware there maybe no debug entries listed.

**Example**
```
<debugInterface adapter="JTAG/SW" connector="20-pin Arm Standard JTAG Connector (0.1 inch connector)"/>
<debugInterface adapter="JTAG/SW" connector="10-pin Cortex Debug Connector (0.05 inch connector)"/>
<debugInterface adapter="JTAG/SW" connector="20-pin Cortex Debug + ETM Connector (0.05 inch connector)"/>
<debugInterface adapter="ST-Link" connector="Mini-USB"/>
```

 		



| Parent | Chain |  |  |
|---|---|---|---|
| board | element_board |  |  |
| Attributes | Description | Type | Use |
| adapter | String describing the debug adapter. Common adapters are: `JTAG/SW` (for all adapters supporting JTAG and Serial-Wire Debug), `CMSIS-DAP`, `OpenSDA`, `J-Link`, `ST-Link`, `Nu-Link`. | xs:string | optional |
| connector | String describing the debug connector. Usually one of these: `10-pin Cortex Debug Connector`, `20-pin Arm Standard JTAG Connector`, `20-pin Cortex Debug + ETM Connector`, `Mini-USB`, `Micro-USB`. | xs:string | optional |
