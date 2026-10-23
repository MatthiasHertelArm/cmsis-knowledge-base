---
id: "devt-pack-checking-tool-rte-model-errors"
type: "concept"
domain: "pack"
title: "Pack Checking Tool: Error and Warning Messages / RTE Model Errors"
summary: "Pack Checking Tool: Error and Warning Messages / RTE Model Errors"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/packchk/README.md#rte-model-errors"
license: "Apache-2.0"
mode: "V"
---

_Part of: Error and Warning Messages_

| Message Number     | Type                | Message Text              | Action
|:------------------ |:------------------- |:------------------------- |:---------------------------------------------------------
| M500               | TEXT                | RTE Model reports: _'MSG'_| Error while preparing data. See massage for more details.
| M502               | TEXT                | RTE Model reports: #error _'NUM'_: _'NAME'_ : _'MSG'_ | Additional software components required.
| M504               | TEXT                | RTE Model reports: MISSING: – _SPACE_ _NAME_ | Add the missing component.

<!-- markdownlint-restore -->
