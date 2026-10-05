---
id: "txmw-chapter-3-functional-components-of-long-file-name-directory"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional components of FileX: **FAT12/16/32 Directory Description** / Long File Name Directory"
summary: "Part of: FAT12/16/32 Directory Description"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter3.md#long-file-name-directory"
license: "MIT"
mode: "V"
---

_Part of: **FAT12/16/32 Directory Description**_

- **Ordinal**

    The one-byte *ordinal* field that specifies the number of the LFN entry. Because LFN entries are positioned in reverse order, the ordinal values of the LFN directory entries comprising a single LFN decrease by one. In addition, the ordinal value of the LFN directly before the 8.3 file name must be one.

    **TABLE 4. Long File Name Directory Entry**

    | Offset | Field | Number of Bytes |
    |------------|-----------|------------|
    | 0x00 | Ordinal Field | 1 |
    | 0x01 | Unicode Character 1 | 2 |
    | 0x03 | Unicode Character 2 | 2 |
    | 0x05 | Unicode Character 3 | 2 |
    | 0x07 | Unicode Character 4 | 2 |
    | 0x09 | Unicode Character 5 | 2 |
    | 0x0B | LFN Attributes | 1 |
    | 0x0C | LFN Type (Reserved always 0) | 1 |
    | 0x0D | LFN Checksum | 1 |
    | 0x0E | Unicode Character 6 | 2 | 
    | 0x10 | Unicode Character 7 | 2 |
    | 0x12 | Unicode Character 8 | 2 |
    | 0x14 | Unicode Character 9 | 2 |
    | 0x16 | Unicode Character 10 | 2 |
    | 0x18 | Unicode Character 11 | 2 |
    | 0x1A | LFN Cluster (unused always 0) | 2 |
    | 0x1C | Unicode Character 12 | 2 |
    | 0x1E | Unicode Character 13 | 2 |

- **Unicode Character**

    The two-byte *Unicode Character* fields are designed to support characters from many different languages. Standard ASCII characters are represented with the ASCII character stored in the first byte of the Unicode character followed by a space character.

- **LFN Attributes**

    The one-byte *LFN Attributes* field contains attributes that identify the directory entry as an LFN directory entry. This is accomplished by having the read-only, system, hidden, and volume attributes all set.

- **LFN Type**

    The one-byte *LFN Type* field is reserved and is always 0.

- **LFN Checksum**

    The one-byte *LFN Checksum*
field represents a checksum of the 11 characters of the associated MSDOS 8.3 file name. This checksum is stored in each LFN entry to help ensure the LFN entry corresponds to the appropriate 8.3 file name.

- **LFN Cluster**

    The two-byte *LFN Cluster* field is unused and is always 0.

    **TABLE 5. Directory Entries Comprising a 39-Character LFN**

    |Entry|Meaning|
    |------------|-----------|
    |1|LFN Directory Entry 3|
    |2|LFN Directory Entry 2|
    |3|LFN Directory Entry 1|
    |4|8.3 Directory Entry (ttttt~n.xx)|
