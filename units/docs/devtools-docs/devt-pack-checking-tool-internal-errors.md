---
id: "devt-pack-checking-tool-internal-errors"
type: "concept"
domain: "pack"
title: "Pack Checking Tool: Error and Warning Messages / Internal Errors"
summary: "The errors in this category are issued because of an internal error in the packchk utility."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/packchk/README.md#internal-errors"
license: "Apache-2.0"
mode: "V"
---

_Part of: Error and Warning Messages_

The errors in this category are issued because of an internal error in the `packchk` utility.

| Message Number     | Type                | Description               | Details and Actions
|:------------------ |:--------------------|:--------------------------|:------------------------------
| M101               | ERROR               | Unknown error!            | Contact Arm for clarifications
| M103               | ERROR               | Internal Error: 'REF'     | Contact Arm for clarifications
| M104               | ERROR               | Path empty when searching for other PDSC files | Execute the check in verbose mode and try to identify the PDSC file intended for use. Correct the PDSC.
| M108               | TEXT                | Reading PDSC File failed! | XML parsing of the PDSC file failed. Verify syntax of the PDSC file.
| M109               | TEXT                | Constructing Model failed!| Contact Arm for clarifications
| M110               | TEXT                | Verifying Model failed    | Contact Arm for clarifications
