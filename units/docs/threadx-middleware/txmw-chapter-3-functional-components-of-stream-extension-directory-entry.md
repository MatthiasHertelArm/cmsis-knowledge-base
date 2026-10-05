---
id: "txmw-chapter-3-functional-components-of-stream-extension-directory-entry"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional components of FileX: **FAT12/16/32 Directory Description** / Stream Extension Directory Entry"
summary: "Part of: FAT12/16/32 Directory Description"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter3.md#stream-extension-directory-entry"
license: "MIT"
mode: "V"
---

_Part of: **FAT12/16/32 Directory Description**_

A description of Stream Extension Directory Entry and its contents is included in the following table.

**TABLE 7. Stream Extension Directory Entry**

|Offset|Field| Number of Bytes|
|------------|-----------|-------|
|0x00|Entry Type|1|
|0x01|Flags|1|
|0x02|Reserved 1|1|
|0x03|Name Length|1|
|0x04|Name Hash|2|
|0x06|Reserved 2|2|
|0x08|Valid Data Length|8|
|0x10|Reserved 3|4|
|0x14|First Cluster|4|
|0x18|Data Length|8|

- **Entry Type**

    The *entry type* field indicates the type of this entry. For streaming extension Directory Entry, this field must be 0xC0.

- **Flags**

    This field contains a series of bits that specify various properties:
    
    |Flag Bit|Meaning    |
    |-----------------|-----------|
    |0x01            |This field indicates whether or not allocation of clusters is possible. This field should be 1.|
    |0x02            |This field indicates whether or not the associated clusters are contiguous. A value 0 means the FAT entry is valid and FileX shall follow the FAT chain. A value 1 means the FAT entry is invalid and the clusters are contiguous.|
    |All other bits    |Reserved.|

- **Reserved 1**

    This field should be 0.

- **Name Length**

    The *name length* field contains the length of the unicode string in the file name directory entries collectively contain. The file name directory entries shall immediately follow this stream extension directory entry.

- **Name Hash**

    The *name hash* field is a 2-byte entry, containing the hash value of the up-cased file name. The hash value allows faster file/directory name lookup: if the hash values don't match, the file name associated with this entry is not a match.

- **Reserved 2**

    This field should be 0.

- **Valid Data Length**

    The *valid data length* field indicates the amount of valid data in the file.

- **Reserved 3**

    This filed should be 0.

- **First Cluster**

    The *first cluster* field contains index of the first cluster of the data stream.

- **Data Length**

    The *data length* field contains the total number of bytes in the allocated clusters.
