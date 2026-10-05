---
id: "txmw-chapter-5-i-o-drivers-for-filex-i-o-driver-requests"
type: "concept"
domain: "rtos"
title: "Chapter 5 - I/O Drivers for FileX: I/O Driver Requests"
summary: "Because each I/O driver has a single entry function, FileX makes specific requests through the media control block. Specifically, the fx_media_driver_request member of FX_MEDIA is used to specify the exact driver request."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter5.md#i-o-driver-requests"
license: "MIT"
mode: "V"
---

Because each I/O driver has a single entry function, FileX makes specific requests through the media control block. Specifically, the  **fx_media_driver_request** member of **FX_MEDIA** is used to specify the exact driver request. The I/O driver communicates the success or failure of the request through the **fx_media_driver_status** member of **FX_MEDIA**. If the driver request was successful, **FX_SUCCESS** is placed in this field before the driver returns. Otherwise, if an error is detected, FX_IO_ERROR is placed in this field.

### Driver Initialization

Although the actual driver initialization processing is application specific, it usually consists of data structure initialization and possibly some preliminary hardware initialization. This request is the first made by FileX and is done from within the fx_media_open service.

If media write protection is detected, the driver fx_media_driver_write_protect member of FX_MEDIA should be set to FX_TRUE.

The following FX_MEDIA members are used for the I/O driver initialization request:

|FX_MEDIA member|Meaning|
|-----------|-----------|
|fx_media_driver_request|FX_DRIVER_INIT|

FileX provides a mechanism to inform the application driver when sectors are no longer being used. This is especially useful for FLASH memory managers that must manage all in-use logical sectors mapped to the FLASH.

If such notification of free sectors is required, the application driver simply sets the *fx_media_driver_free_sector_update* field in the associated **FX_MEDIA** structure to **FX_TRUE**. After set, FileX makes a ***FX_DRIVER_RELEASE_SECTORS*** I/O driver call indicating when one or more consecutive sectors becomes free.

### Boot Sector Read

Instead of using a standard read request, FileX makes a specific request to read the media's boot sector. The following **FX_MEDIA** members are used for the I/O driver boot sector read request:

|FX_MEDIA member|Meaning|
|-----------|-----------|
|fx_media_driver_request| FX_DRIVER_BOOT_READ|
|fx_media_driver_buffer| Address of destination for boot sector.|

### Boot Sector Write

Instead of using a standard write request, FileX makes a specific request to write the media's boot sector. The following **FX_MEDIA** members are used for the I/O driver boot sector write request:

|FX_MEDIA member|Meaning|
|-----------|-----------|
|fx_media_driver_request| FX_DRIVER_BOOT_WRITE|
|fx_media_driver_buffer| Address of source for boot sector.|

### Sector Read

FileX reads one or more sectors into memory by issuing a read request to the I/O driver. The following **FX_MEDIA** members are used for the I/O driver read request:

|FX_MEDIA member|Meaning|
|-----------|-----------|
|fx_media_driver_request| FX_DRIVER_READ|
|fx_media_driver_logical_sector|Logical sector to read|
|fx_media_driver_sectors|Number of sectors to read|
|fx_media_driver_buffer|Destination buffer for sector(s) read|
|fx_media_driver_data_sector_read|Set to FX_TRUE if a file data sector is requested. Otherwise, FX_FALSE if a system sector (FAT or directory sector) is requested.|
|fx_media_driver_sector_type|Defines the explicit type of sector requested, as follows:
FX_FAT_SECTOR (2)
FX_DIRECTORY_SECTOR (3)
FX_DATA_SECTOR (4)|

### Sector Write

FileX writes one or more sectors to the physical media by issuing a write request to the I/O driver. The following FX_MEDIA members are used for the I/O driver write request:

|FX_MEDIA member| Meaning|
|-----------|-----------|
|fx_media_driver_request|FX_DRIVER_WRITE|
|fx_media_driver_logical_sector|Logical sector to write|
|fx_media_driver_sectors|Number of sectors to write|
|fx_media_driver_buffer|Source buffer for sector(s) to write|
|fx_media_driver_system_write| Set to FX_TRUE if a system sector is requested (FAT or directory sector). Otherwise, FX_FALSE if a file data sector is requested.|
|fx_media_driver_sector_type|Defines the explicit type of sector requested, as follows:
 
FX_FAT_SECTOR (2) 
 FX_DIRECTORY_SECTOR (3) 
FX_DATA_SECTOR (4).|

### Driver Flush

FileX flushes all sectors currently in the driver's sector cache to the physical media by issuing a flush request to the I/O driver. Of course, if the driver is not caching sectors, this request requires no driver processing. The following FX_MEDIA members are used for the I/O driver flush request:

|FX_MEDIA member| Meaning|
|-----------|-----------|
|fx_media_driver_request|FX_DRIVER_FLUSH|

### Driver Abort

FileX informs the driver to abort all further physical I/O activity with the physical media by issuing an abort request to the I/O driver. The driver should not perform any I/O again until it is re-initialized. The following FX_MEDIA members are used for the I/O driver abort request:

|FX_MEDIA member| Meaning|
|-----------|-----------|
|fx_media_driver_request| FX_DRIVER_ABORT|

### Release Sectors

If previously selected by the driver during initialization, FileX informs the driver whenever one or more consecutive sectors become free. If the driver is actually a FLASH manager, this information can be used to tell the FLASH manager that these sectors are no longer needed. The following **FX_MEDIA** members are used for the I/O release sectors request:

|FX_MEDIA member| Meaning|
|-----------|-----------|
|fx_media_driver_request|FX_DRIVER_RELEASE_SECTORS|
|fx_media_driver_logical_sector|Start of free sector|
|fx_media_driver_sectors|Number of free sectors|

### Driver Suspension

Because I/O with physical media may take some time, suspending the calling thread is often desirable. Of course, this assumes completion of the underlying I/O operation is interrupt driven. If so, thread suspension is easily implemented with a ThreadX semaphore. After starting the input or output operation, the I/O driver suspends on its own internal I/O semaphore (created with an initial count of zero during driver initialization). As part of the driver I/O completion interrupt processing, the same I/O semaphore is set, which in turn wakes up the suspended thread.

### Sector Translation

Because FileX views the media as linear logical sectors, I/O requests made to the I/O driver are made with logical sectors. It is the driver's responsibility to translate between logical sectors and the physical geometry of the media, which may include heads, tracks, and physical sectors. For FLASH and RAM disk media, the logical sectors typically map directory to physical sectors. In any case, here are the typical formulas to perform the logical to physical sector
mapping in the I/O driver:

```c
media_ptr -> fx_media_driver_physical_sector =
    (media_ptr -> fx_media_driver_logical_sector % media_ptr -> fx_media_sectors_per_track) + 1;

media_ptr -> fx_media_driver_physical_head =
    (media_ptr -> fx_media_driver_logical_sector/ media_ptr ->
    fx_media_sectors_per_track) % media_ptr -> fx_media_heads;

media_ptr -> fx_media_driver_physical_track =(media_ptr ->
    fx_media_driver_logical_sector/ (media_ptr -> fx_media_sectors_per_track *
    media_ptr -> fx_media_heads)));
```

Note that physical sectors start at one, while logical sectors start at zero.

### Hidden Sectors

Hidden sectors resided prior to the boot record on the media. Because they are really outside the scope of the FAT file system layout, they must be accounted for in each logical sector operation the driver does.

### Media Write Protect

The FileX driver can turn on write protect by setting the fx_media_driver_write_protect field in the media control block. This will cause an error to be returned if any FileX calls are made in an attempt to write to the media.
