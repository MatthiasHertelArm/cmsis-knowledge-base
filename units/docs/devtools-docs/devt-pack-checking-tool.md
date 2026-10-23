---
id: "devt-pack-checking-tool"
type: "concept"
domain: "pack"
title: "Pack Checking Tool"
summary: "The utility packchk assists the validation of a CMSIS-Pack. It operates on the unzipped content of the Software Pack. It distributed as part of the CMSIS-Toolbox."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/packchk/README.md"
license: "Apache-2.0"
mode: "V"
---

The utility `packchk` assists the validation of a CMSIS-Pack. It operates on
the unzipped content of the Software Pack. It distributed as part of
the [CMSIS-Toolbox](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/installation.md).

`packchk` performs the following operations:

- Checks the `*.pdsc` file against the PACK.xsd schema file in the installation path.
- Reads the content of the specified `*.pdsc` file. The path to this `*.pdsc`  file is considered as root directory of
  the Software Pack.
- Verifies the existence of all files in the Software Pack that are referenced  in the `*.pdsc` file.
- Checks for presence and correctness of mandatory elements such as `<vendor>`,  `<version>`, etc. - Optionally, reads
  other `*.pdsc` files to resolve dependencies on `<apis>`,  `<boards>`, and `<conditions>`.
- Optionally, verifies the element `<url>`.
- Optionally, composes the versioned pack ID from the information contained in the PDSC:
  `package:vendor.package:name.release.latest:version`
- Sets the exit status reflecting the validation result to:
  - 0 : no errors detected
  - 1 : errors during validation detected
