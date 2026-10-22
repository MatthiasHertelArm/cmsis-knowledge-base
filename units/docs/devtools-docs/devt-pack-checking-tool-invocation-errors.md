---
id: "devt-pack-checking-tool-invocation-errors"
type: "concept"
domain: "pack"
title: "Pack Checking Tool: Error and Warning Messages / Invocation Errors"
summary: "The errors in this category are issued because of an incorrect command-line input that prevents the packchk execution."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/packchk/README.md#invocation-errors"
license: "Apache-2.0"
mode: "V"
---

_Part of: Error and Warning Messages_

The errors in this category are issued because of an incorrect command-line input that prevents the `packchk`
execution.

| Message Number     | Type                | Message Text                                                              | Details and Actions
|:------------------ |:------------------- |:--------------------------------------------------------------------------|:---------------------------------------------------------
| M202               | ERROR               | No PDSC input file specified                                              | Correct the command line. **packchk** expects a *.pdsc file name as input.
| M203               | ERROR               | Error reading PDSC file _'PATH/FILENAME'!_                                | Verify the PDSC file for consistency.
| M204               | ERROR               | File not found: _'PATH'_                                                  | The specified PDSC file could not be found in the _PATH_ displayed in the message. Correct the path or the filename.
| M205               | ERROR               | Cannot create Pack Name file _'PATH'_                                     | Check the disk space or your permissions. Correct the path name.
| M206               | ERROR               | Multiple PDSC files found in package: _'FILES'_                           | Only one PDSC file is allowed in a package. Remove unnecessary PDSC files. The message lists all \*.pdsc files found.
| M207               | ERROR               | PDSC file name mismatch! Expected: _'PDSC1.pdsc'_ Actual : _'PDSC2.pdsc'_ | The PDSC file expected has not been found. Rename or exchange the PDSC file.
| M210               | ERROR               | Only one input file to be checked is allowed.                             | You can only check one PDSC file at a time.
| M218               | ERROR               | Cannot find the schema file specified by "--xsd".                         | CHeck whether the file exists.
