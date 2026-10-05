---
id: "txmw-chapter-3-functional-components-of-media-description"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional components of FileX: Media Description"
summary: "FileX is a high-performance embedded file system that conforms to the FAT file system format. FileX views the physical media as an array of logical sectors."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter3.md#media-description"
license: "MIT"
mode: "V"
---

FileX is a high-performance embedded file system that conforms to the FAT file system format. FileX views the physical media as an array of logical sectors. How these sectors are mapped to the underlying physical media is determined by the I/O driver connected to the FileX media during the ***fx_media_open*** call.

### FAT12/16/32 Logical Sectors

The exact organization of the media's logical sectors is determined by the contents of the physical media's boot record. The general layout of the media's logical sectors is shown in Figure 1.

FileX logical sectors start at logical sector 1, which points to the first reserved sector of the media. Reserved sectors are optional, but when in use they typically contain system information such as boot code.

### FAT12/16/32 Media Boot Record

The exact sector offset of the other areas in the logical sector view of the media is derived from the contents of the *media boot record*. The location of the boot record is typically at sector 0. However, if the media has *hidden sectors*, the offset to the boot sector must account for them (they are located immediately BEFORE the boot sector). Table 1 lists the media's boot record components, and the components are described in the paragraphs.

- **Jump Instruction** The *jump instruction* field is a three-byte field that represents an Intel x86 machine instruction for a processor jump. This is a legacy field in most situations.

  (figure: FileX Media Logical Sector View)

  **FIGURE 1. FileX Media Logical Sector View**

- **OEM Name** The *OEM name* field is reserved for manufacturers to place their name or a name for the device.
- **Bytes Per Sector** The *bytes per sector* field in the media boot record defines how many bytes are in each sector—the fundamental element of the media.
- **Sectors Per Cluster** The *sectors per cluster* field in the media boot record defines the number of sectors assigned to a cluster. The cluster is the fundamental allocation element in an FAT compatible file system. All file information and subdirectories are allocated from the media's available clusters as determined by the File Allocation Table (FAT).

    **TABLE 1. FileX Media Boot Record**
    
    |Offset  |Field  |Number of Bytes|
    |----------|-----------|------------|
    |0x00|Jump Instruction (e9,xx,xx or eb,xx,90)|3|
    |0x03|OEM Name|8|
    |0x0B|Bytes Per Sector|2|
    |0x0D|Sectors Per Cluster|1|
    |0x0E|Number of Reserved Sectors|2|
    |0x10|Number of FATs|1|
    |0x11|Size of Root Directory|2|
    |0x13|Number of Sectors FAT-12 & FAT-16|2|
    |0x15|Media Type|1|
    |0x16|Number of Sectors Per FAT|2|
    |0x18|Sectors Per Track|2|
    |0x1A|Number of Heads|2|
    |0x1C|Number of Hidden Sectors|4|
    |0x20|Number of Sectors - FAT-32|4|
    |0x24|Sectors per FAT (FAT-32)|4|
    |0x2C|Root Directory Cluster|4|
    |0x3E|System Boot code|448
    |0x1FE|0x55AA|2|

- **Reserved Sectors** The *reserved sectors* field in the media boot record defines the number of sectors reserved between the boot record and the first sector of the FAT area. This entry is zero in most cases.
- **Number of FATs** The *number of FATs* entry in the media boot record defines the number of FATs in the media. There must always be at least one FAT in a media. Additional FATs are merely duplicate copies of the primary (first) FAT and are typically used by diagnostic or recovery software.
- **Root Directory Size** The *root directory size* entry in the media boot record defines the fixed number of entries in the root directory of the media. This field is not applicable to subdirectories and the FAT-32 root directory because they are both allocated from the media's clusters.
- **Number of Sectors FAT-12 & FAT-16** The *number of sectors* field in the media boot record contains the total number of sectors in the media. If this field is zero, then the total number of sectors is contained in the *number of sectors FAT-32* field located later in the boot record.
- **Media Type** The *media type* field is used to identify the type of media present to the device driver. This is a legacy field.
- **Sectors Per FAT** The *sectors per FAT* filed in the media boot record contains the number of sectors associated with each FAT in the FAT area. The number of FAT sectors must be large enough to account for the maximum possible number of clusters that can be allocated in the media.
- **Sectors Per Track** The *sectors per track* field in the media boot record defines the number of sectors per track. This is typically only pertinent to actual disk-type media. FLASH devices don't use this mapping.
- **Number of Heads** The *number of heads* field in the media boot record defines the number of heads in the media. This is typically only pertinent to actual disk-type media. FLASH devices don't use this mapping.
- **Hidden Sectors** The *hidden sectors* field in the media boot record defines the number of sectors before the boot record. This field is maintained in the **FX_MEDIA** control block and must be accounted for in FileX I/O drivers in all read and write requests made by FileX.
- **Number of Sectors FAT-32** The *number of sectors* field in the media boot record is valid only if the two-byte *number of sectors* field is zero. In such a case, this four-byte field contains the number of sectors in the media.
- **Sectors per FAT (FAT-32)** The *sectors per FAT (FAT-32)* field is valid only in FAT-32 format and contains the number of sectors allocated for each FAT of the media.
- **Root Directory Cluster** The *root directory cluster* field is valid only in FAT-32 format and contains the starting cluster number of the root directory.
- **System Boot Code** The *system boot code* field is an area to store a small portion of boot code. In most devices today, this is a legacy field.
- **Signature 0x55AA** The *signature* field is a data pattern used to identify the boot record. If this field is not present, the boot record is not valid.

### File Allocation Table (FAT)

The *File Allocation Table (FAT)* starts after the reserved sectors in the media. The FAT area is basically an array of 12-bit, 16-bit, or 32-bit entries that determine if that cluster is allocated or part of a chain of clusters comprising a subdirectory or a file. The size of each FAT entry is determined by the number of clusters that need to be represented. If the number of clusters (derived from the total sectors divided by the sectors per cluster) is less than or equal to 4,086, 12-bit FAT entries are used. If the total number of clusters is greater than 4,086 and less than 65,525, 16-bit FAT entries are used. Otherwise, if the total number of clusters is greater than or equal to 65,525, 32-bit FAT is used.

For FAT12/16/32, the FAT table not only maintains the cluster chain, it also provides information on cluster allocation: whether or not a cluster is available. 

### FAT Entry Contents

The first two entries in the FAT table are not used and typically have the following contents.

|FAT Entry |12-bit FAT|16-bit FAT|32-bit FAT|
|----------|-----------|------------|-------|
|Entry 0|0x0F0|0x00F0|0x000000F0|
|Entry 1|0xFFF|0xFFFF|0x0FFFFFFF|

FAT entry number 2 represents the first cluster in the media's data area. The contents of each cluster entry determines whether or not it is free or part of a linked list of clusters allocated for a file or a subdirectory. If the cluster entry contains another valid cluster entry, then the cluster is allocated and its value points to the next cluster allocated in the cluster chain.

Possible cluster entries are defined as follows.

|Meaning|12-bit FAT|16-bit FAT|32-bit FAT|
|----------|-----------|------------|-------|
|Free Cluster|0x000|0x0000|0x00000000|
|Not Used|0x001|0x0001|0x00000001|
|Reserved|0xFF0-FF6|0xFFF0-FFF6|0x0FFFFFF0-6|
|Bad Cluster|0xFF7|0xFFF7|0x0FFFFFF7|
|Reserved| - | - | - |
|Last Cluster| 0xFF8-FFF| 0xFFF8-FFFF| 0x0FFFFFF8-F|
|Cluster Link| 0x002-0xFEF| 0x0002-FFEF| 0x2-0x0FFFFFEF |

The last cluster in an allocated chain of clusters contains the Last Cluster value (defined above). The first cluster number is found in the file or subdirectory's directory entry.

### Internal Logical Cache

FileX maintains a *most-recently-used* logical sector cache for each opened media. The maximum size of the logical sector cache is defined by the constant **FX_MAX_SECTOR_CACHE** and is located in ***fx_api.h***. This is the first factor determining the size of the internal logical sector cache.

The other factor that determines the size of the logical sector cache is the amount of memory supplied to the ***fx_media_open*** call by the application. There must be enough memory for at least one logical sector. If more than **FX_MAX_SECTOR_CACHE** logical sectors are required, the constant must be changed in ***fx_api.h*** and the entire FileX library must be rebuilt.

> **Important:** *Each opened media in FileX may have a different cache size depending on the memory supplied during the open call.*

### Write Protect

FileX provides the application driver the ability to dynamically set write protection on the media. If write protection is required, the driver sets to FX_TRUE the *fx_media_driver_write_protect* field in the associated FX_MEDIA structure. When set, all attempts by the application to modify the media are rejected as well as attempts to open files for writing. The driver may also disable write protection by clearing this field.

### Free Sector Update

FileX provides a mechanism to inform the application driver when sectors are no longer in use. This is especially useful for FLASH memory managers that manage all logical sectors being used by FileX.

If notification of free sectors is required, the application driver sets to FX_TRUE the *fx_media_driver_free_sector_update* field in the associated FX_MEDIA structure. This assignment is typically done during driver initialization.

Setting this field, FileX makes a **FX_DRIVER_RELEASE_SECTORS** driver call indicating when one or more consecutive sectors become free.

### Media Control Block FX_MEDIA

The characteristics of each open media in FileX are contained in the media control block. This structure is defined in the file ***fx_api.h***.

The media control block can be located anywhere in memory, but it is most common to make the control block a global structure by defining it outside the scope of any function.

Locating the control block in other areas requires a bit more care, just like all dynamically allocated memory. If a control block is allocated within a C function, the memory associated with it is part of the calling thread's stack.

> [!WARNING]
>*In general, avoid using local storage for control blocks because after the function returns, all of its local variable stack space is released—regardless of whether it is still in use!*
