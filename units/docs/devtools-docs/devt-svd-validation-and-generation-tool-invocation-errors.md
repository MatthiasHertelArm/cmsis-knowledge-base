---
id: "devt-svd-validation-and-generation-tool-invocation-errors"
type: "concept"
domain: "pack"
title: "SVD Validation and Generation Tool: Error and Warning Messages / Invocation errors"
summary: "SVD Validation and Generation Tool: Error and Warning Messages / Invocation errors"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/svdconv/SVDConv/README.md#invocation-errors"
license: "Apache-2.0"
mode: "V"
---

_Part of: Error and Warning Messages_

| Message Number |  Type |  Message Text |  Action|
|----------------|---------|---------------|--------|
| M101 |  ERROR |  Unknown error! |  Please contact support.|
| M102 |  ERROR |  MFC initialization failed |  Please contact support.|
| M103 |  ERROR |  Internal Error: 'REF' |  Please contact support.|
| M104 |  CRITICAL |  'MSG' |  Please contact support.|
| M105 |  ERROR |  Cannot add Register to group sorter: 'NAME' |  |
| M106 |  ERROR |  Command 'NAME' failed: 'NUM': 'MSG' |  |
| M107 |  ERROR |  Lost xml file stream. |  Check SVD file.|
| M108 |  ERROR |  SfrDis not supported.Disassembly not supported. |  |
| M109 |  ERROR |  Cannot find 'NAME' |  Check specified file.|
| M111 |  PROGRESS |  'NAME' failed |  Check specified file.|
| M120 |  ERROR |  Invalid arguments! |  Provide a list of valid arguments.|
| M121 |  ERROR |  File not found 'NAME' Check specified file. |  |
| M122 |  ERROR |  Name of command file should follow '@' |  Check specified command.|
| M123 |  ERROR |  File not found: 'PATH'! |  Check speficied path.|
| M124 |  ERROR |  Cannot execute SfrCC2: 'PATH'!" |  Check path to SfrCC2.|
| M125 |  WARNING |  SfrCC2 report: 'MSG' SfrCC2 report end. |  |
| M126 |  WARNING |  SfrDis: 'MSG' |  |
| M127 |  ERROR |  SfrCC2 reports errors! |  Check SVD file.|
| M128 |  WARNING |  SfrCC2 reports warnings! |  Check SVD file.|
| M129 |  ERROR |  Option unknown: 'OPT' |  Check given option 'OPT'.|
| M130 |  ERROR |  Cannot create file 'NAME' |  Check user rights.|
| M132 |  ERROR |  SfrCC2 report: 'MSG' SfrCC2 report end." |  |
| M133 |  ERROR |  SFR generation is only supported on Windows (requires SfrCC2.exe). | Generate SFR output on Windows with SfrCC2.exe installed alongside SVDConv, or use `--generate=sfd` for SFD output. |
