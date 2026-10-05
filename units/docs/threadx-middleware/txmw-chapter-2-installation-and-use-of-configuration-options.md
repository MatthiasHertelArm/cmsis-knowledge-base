---
id: "txmw-chapter-2-installation-and-use-of-configuration-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and use of FileX: Configuration Options"
summary: "There are several configuration options when building the FileX library and the application using FileX. The options below can be defined in the application source, on the command line, or within the fx_user.h include file."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter2.md#configuration-options"
license: "MIT"
mode: "V"
---

There are several configuration options when building the FileX library and the application using FileX. The options below can be defined in the application source, on the command line, or within the ***fx_user.h*** include file.

> **Important:** *Options defined in **fx_user.h** are applied only if the application and ThreadX library are built with ***FX_INCLUDE_USER_DEFINE_FILE*** defined.*
> When using FileX in Standalone mode (**FX_STANDALONE_ENABLE** must be defined), ThreadX files/libraries are not required.

The following list describes each configuration option in detail:

|Define|Meaning|
|----------    |-----------|
|FX_MAX_LAST_NAME_LEN        |This value defines the maximum file name length, which includes full path name. By default, this value is 256.|
|FX_DONT_UPDATE_OPEN_FILES    |Defined, FileX does not update already opened files.|
|FX_MEDIA_DISABLE_SEARCH_CACHE    |Defined, the file search cache optimization is disabled.|
|FX_MEDIA_DISABLE_SEARCH_CACHE    |Defined, the file search cache optimization is disabled.|
|FX_DISABLE_DIRECT_DATA_READ_CACHE_FILL |Defined, the direct read sector update of cache is disabled.|
|FX_MEDIA_STATISTICS_DISABLE |Defined, gathering of media statistics is disabled.|
|FX_SINGLE_OPEN_LEGACY |Defined, legacy single open logic for the same file is enabled.|
|FX_RENAME_PATH_INHERIT    |Defined, renaming inherits path information.|
|FX_DISABLE_ERROR_CHECKING    |Removes the basic FileX error checking API and results in improved performance (as much as 30%) and smaller code size.|
|FX_MAX_LONG_NAME_LEN    |Specifies the maximum file name size for FileX. The default value is 256, but this can be overridden with a command-line define. Legal values range between 13 and 256.|
|FX_MAX_SECTOR_CACHE|Specifies the maximum number of logical sectors that can be cached by FileX. The actual number of sectors that can be cached is lesser of this constant and how many sectors can fit in the amount of memory supplied at fx_media_open. The default value is 256. All values must be a power of 2.|
|FX_FAT_MAP_SIZE    |Specifies the number of sectors that can be represented in the FAT update map. The default value is 256, but this can be overridden with a command-line define. Larger values help reduce unneeded updates of secondary FAT sectors.|
|FX_MAX_FAT_CACHE    |Specifies the number of entries in the internal FAT cache. The default value is 16, but this can be overridden with a command-line define. All values must be a power of 2.|
|FX_FAULT_TOLERANT    |When defined, FileX immediately passes write requests of all system sectors (boot, FAT, and directory sectors) to the media's driver. This potentially decreases performance, but helps limit corruption to lost clusters. Note that enabling this feature does not automatically enable FileX Fault Tolerant Module, which is enabled by defining|
|FX_FAULT_TOLERANT_DATA    |When defined, FileX immediately passes all file data write requests to the media's driver. This potentially decreases performance, but helps limit lost file data. Note that enabling this feature does not automatically enable FileX Fault Tolerant Module, which is enabled by defining ***FX_ENABLE_FAULT_TOLERANT***|
|FX_NO_LOCAL_PATH|Removes local path logic from FileX, resulting in smaller code size.|
|FX_NO_TIMER|Eliminates the ThreadX timer setup to update the FileX system time and date. Doing so causes default time and date to be placed on all file operations.|
|FX_UPDATE_RATE_IN_SECONDS    |Specifies rate at which system time in FileX is adjusted. By default, value is 10, specifying that the FileX system time is updated every 10 seconds.|
|FX_UPDATE_RATE_IN_TICKS| Specifies the same rate as ***FX_UPDATE_RATE_IN_SECONDS*** (see above), except in terms of the underlying ThreadX timer frequency. The default is 1000, which assumes a 10ms ThreadX timer rate and a 10 second interval.|
|FX_SINGLE_THREAD|Eliminates ThreadX protection logic from the FileX source. It should be used if FileX is being used only from one thread or if FileX is being used without ThreadX.|
|FX_DRIVER_USE_64BIT_LBA|When defined, enables 64-bit sector addresses used in I/O driver. By default this option is not defined.|
|FX_ENABLE_FAULT_TOLERANT| When defined, enables FileX Fault Tolerant Module. Enabling Fault Tolerant automatically defines the symbol ***FX_FAULT_TOLERANT*** and ***FX_FAULT_TOLERANT_DATA***. By default this option is not defined.|
|FX_FAULT_TOLERANT_BOOT_INDEX|Defines byte offset in the boot sector where the cluster for the fault tolerant log is. By default this value is 116. This field takes 4 bytes. Bytes 116 through 119 are chosen because they are marked as reserved by FAT 12/16/32 specification.|
|FX_FAULT_TOLERANT_MINIMAL_CLUSTER|This symbol is deprecated. It is no longer being used by FileX Fault Tolerant.|
|FX_STANDALONE_ENABLE|Defined, enables FileX to be used in standalone mode (without Eclipse ThreadX). By default this symbol is not defined.|

> **Important:** When **FX_STANDALONE_ENABLE** is defined, Local path logic and ThreadX timer setup are disabled.
