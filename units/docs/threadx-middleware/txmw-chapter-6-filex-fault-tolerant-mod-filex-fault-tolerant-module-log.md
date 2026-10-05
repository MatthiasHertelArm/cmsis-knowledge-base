---
id: "txmw-chapter-6-filex-fault-tolerant-mod-filex-fault-tolerant-module-log"
type: "concept"
domain: "rtos"
title: "Chapter 6 - FileX fault tolerant module: FileX Fault Tolerant Module Log"
summary: "The FileX fault tolerant log takes up one logical cluster in flash. The index to the starting cluster number of that cluster is recorded in the boot sector of the media, with an offset specified by the symbol FX_FAULT_TOLERANT_BOOT_INDEX."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter6.md#filex-fault-tolerant-module-log"
license: "MIT"
mode: "V"
---

The FileX fault tolerant log takes up one logical cluster in flash. The index to the starting cluster number of that cluster is recorded in the boot sector of the media, with an offset specified by the symbol **FX_FAULT_TOLERANT_BOOT_INDEX**. By default this symbol is defined to be 116. This location is chosen because it is marked as reserved in FAT12/16/32 specification.

Figure 5, "Log Structure Layout," shows the general layout of the log structure. The log structure contains three sections: Log Header, FAT Chain, and Log Entries.

> **Important:** *All multi-byte values stored in the log entries are in Little Endian format.*

(figure: Log Structure Layout)

**Figure 5. Log Structure Layout**

The Log Header area contains information that describes the entire log structure and explains each field in detail.

**TABLE 8. Log Header Area**

|Field|Size(in bytes)|Description|
|-----|--------------|-----------|
|ID|4|Identifies a FileX Fault Tolerant Log structure. The log structure is considered invalid if the ID value is not 0x46544C52.|
|Total Size|2|Indicates the total size (in bytes) of the entire log structure.|
|Header Checksum|2|Checksum that converts the log header area. The log structure is considered invalid if the header fields fail the checksum verification.|
|Version Number|2|FileX Fault Tolerant major and minor version numbers.|
|Reserved|2|For future expansion.|

The Log Header area is followed by the FAT Chain Log area. Figure 9 contains information that describes how the FAT chain should be modified. This log area contains information on the clusters being allocated to a file, the clusters being removed from a file, and where the insertion/deletion should be and describes each field in the FAT Chain Log area.

**TABLE 9. FAT Chain Log Area**

|Field|Size(in bytes)|Description|
|-----|--------------|-----------|
|FAT Chain Log Checksum|2|Checksum of the entire FAT Chain Log area. The FAT Chain Log area is considered invalid if the it fails the checksum verification.|
|Flag|1|Valid flag values are:
0x01 FAT Chain Valid|
|Reserved|1|Reserved for future use|
|Insertion Point – Front|4|The cluster (that belongs to the original FAT chain) where the newly created chain is going to be attached to.|
|Head Cluster of New FAT Chain|4|The first cluster of the newly created FAT Chain|
|Head Cluster of Original FAT Chain|4|The first cluster of the portion of the original FAT Chain that is to be removed.|
|Insertion Point – Back|4|The original cluster where the newly created FAT chain joins at.|
|Next Deletion Point|4|This field assists the FAT chain cleanup procedure.|

The Log Entries Area contains log entries that describe the changes needed to recover from a failure. There are three types of log entry supported in the FileX fault tolerant module: FAT Log Entry; Directory Log Entry.

The following three figures and three tables describe these log entries in detail.

(figure: FAT Log Entry)

**Figure 6. FAT Log Entry**

**TABLE 10. FAT Log Entry**

|Field|Size(in bytes)|Description|
|-----|--------------|-----------|
Type|2|Type of Entry, must be FX_FAULT_TOLERANT_FAT_LOG_TYPE|
|Size|2|Size of this entry|
|Cluster Number|4|Cluster number|
|Value|4|Value to be written into the FAT entry|

(figure: Directory Log Entry)

**Figure 7. Directory Log Entry**

**TABLE 11. Directory Log Entry**

|Field|Size(in bytes)|Description|
|-----|--------------|-----------|
|Type|2|Type of Entry, must be FX_FAULT_TOLERANT_DIRECTORY_LOG_TYPE|
|Size|2|Size of this entry|
|Sector Offset|4|Offset (in bytes) into the sector where this directory is located.|
|Log Sector|4|The sector where the directory entry is located|
|Log Data|Variable|Content of the directory entry|
