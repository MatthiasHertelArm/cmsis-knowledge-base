---
id: "txmw-chapter-3-functional-components-of-fat12-16-32-directory-description"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional components of FileX: **FAT12/16/32 Directory Description**"
summary: "FileX supports both 8.3 and Windows Long File Name (LFN) name formats."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter3.md#fat12-16-32-directory-description"
license: "MIT"
mode: "V"
---

FileX supports both 8.3 and Windows Long File Name (LFN) name formats. In addition to the name, each directory entry contains the entry's attributes, the last modified time and date, the starting cluster index, and the size in bytes of the entry. Table 3 shows the contents and size of a FileX 8.3 directory entry.

- **Directory Name**

    FileX supports file names ranging in size from 1 to 255 characters. Standard eight-character file names are represented in a single directory entry on the media. They are left justified in the directory name field and are blank padded. In addition, the ASCII characters that comprise the name are always capitalized.

    Long File Names (LFNs) are represented by consecutive directory entries, in reverse order, followed immediately by an 8.3 standard file name. The created 8.3 name contains all the meaningful directory information associated with the name. Table 4 shows the contents of the directory entries used to hold the Long File Name information, and Table 5 shows an example of a 39-character LFN that requires a total of four directory entries.

    > **Important:** *The constant **FX_MAX_LONG_NAME_LEN**, defined in **fx_api.h**, contains the maximum length supported by FileX.*

- **Directory Filename Extension**

    For standard 8.3 file names, FileX also supports the optional three-character *directory filename extension*. Just like the eight-character file name, filename extensions are left justified in the directory filename extension field, blank padded, and always capitalized.

    **TABLE 3. FileX 8.3 Directory Entry**

    |Offset|Field|Number of Bytes|
    |------------|-----------|------------|
    |0x00|Directory Entry Name|8|
    |0x08|Directory Extension|3|
    |0x0B|Attributes|1|
    |0x0C|NT (introduced by the long file name format and is reserved for NT [always 0])|1|
    |0x0D|Created Time in milliseconds ( introduced by the long file name format and represents the number of milliseconds when the file was created.)|1|
    |0x0E|Created Time in hours & minutes (introduced by the long file name format and represents the hour and minute the file was created )|2|
    |0x10|Created Date (introduced by the long file name format and represents the date the file was created.)|2|
    |0x12|Last Accessed Date ( introduced by the long file name format and represents the date the file was last accessed.)|2|
    |0x14|Starting Cluster (Upper 16 bits FAT-32 only)|2|
    |0x16|Modified Time|2|
    |0x18|Modified Date|2|
    |0x1A|Starting Cluster (Lower 16 bits FAT-32 or FAT-12 or FAT-16)|2|
    |0x1C|File Size|4|


- **Directory Attributes**

    The one-byte *directory attribute* field entry contains a series of bits that specify various properties of the directory entry. Directory attribute definitions are as follow:

    |Attribute Bit|Meaning|
    |------------|-----------|
    |0x01|Entry is read-only.|
    |0x02|Entry is hidden.|
    |0x04|Entry is a system entry.|
    |0x08|Entry is a volume label|
    |0x10|Entry is a directory.|
    |0x20|Entry has been modified.|

    Because all the attribute bits are mutually exclusive, there may be more than one attribute bit set at a time.

- **Directory Time**

    The two-byte *directory time* field contains the hours, minutes, and seconds of the last change to the specified directory entry. Bits 15 through 11 contain the hours, bits 10 through 5 contain the minutes, and bits 4 through 0 contain the half seconds. Actual seconds are divided by two before being written into this field.

- **Directory Date**

    The two-byte *directory date* field contains the year (offset from 1980), month, and day of the last change to the specified directory entry. Bits 15 through 9 contain the year offset, bits 8 through 5 contain the month offset, and bits 4 through 0 contain the day.

- **Directory Starting Cluster**

    This field occupies 2 bytes for FAT-12 and FAT-16. For FAT-32 this field occupies 4 bytes. This field contains the first cluster number allocated to the entry (subdirectory or file).

    > **Note:** *Note that FileX creates new files without an initial cluster (starting cluster field equal to zero) to allow users to optionally allocate a contiguous number of clusters for a newly created file. *

- **Directory File Size**

    The four-byte *directory* *file size* field contains the number of bytes in the file. If the entry is really a subdirectory, the size field is zero.
